"""Rank all 35 tracks from the blind pairwise judgements and slot the unlabelled ones into the user's order.

Inputs: eval/pairwise/results/*.jsonl (blind verdicts on alias pairs), eval/pairwise/aliases.json, ../labels.csv.

1. Bradley-Terry strengths for all 35 tracks from every verdict. Soft outcomes by margin:
   slight 0.65, clear 0.80, strong 0.95, tie 0.5. Small ridge prior keeps strengths finite.
2. Judge check: agreement of blind verdicts with the user's own order on labelled-vs-labelled pairs.
3. Slot for each unlabelled track U: the gap in the user's order (19 gaps) that minimises the expected number of
   pairwise disagreements, sum_{L above gap} P(U beats L) + sum_{L below gap} P(L beats U), with P from the
   Bradley-Terry fit. Score = slot score (lib/scale via placement_kit.slot_score). Tracks sharing a slot are
   ordered by strength and spread evenly inside the gap.
4. 80% range: bootstrap over verdicts (resample with replacement, refit, re-slot), 10th-90th percentile.

Writes eval/pairwise/strengths.csv, eval/pairwise/summary.md and eval/placements/pairwise.jsonl
(placement lines for tools/assemble.py).
"""
from __future__ import annotations

import csv
import json
import random
import sys
from pathlib import Path

import numpy as np

EVAL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(EVAL))
sys.path.insert(0, str(EVAL / "tools"))

from lib.scale import anchored_scores, read_labels, tier_of  # noqa: E402

MARGIN = {"slight": 0.65, "clear": 0.80, "strong": 0.95}
PW = EVAL / "pairwise"


def load():
    amap = json.loads((PW / "aliases.json").read_text())
    inv = {a: t for t, a in amap.items()}
    out = []
    for f in sorted((PW / "results").glob("*.jsonl")):
        for line in f.read_text().splitlines():
            if not line.strip():
                continue
            r = json.loads(line)
            a, b, w = inv[r["a"]], inv[r["b"]], r["winner"]
            p = 0.5 if w == "tie" else MARGIN.get(r.get("margin", "clear"), 0.8)
            if w == r["b"]:
                p = 1 - p
            out.append((a, b, p, r))
    return out


def fit_bt(ids, obs, lam=0.05, iters=400):
    idx = {t: i for i, t in enumerate(ids)}
    s = np.zeros(len(ids))
    A = np.array([idx[a] for a, _, _, _ in obs])
    B = np.array([idx[b] for _, b, _, _ in obs])
    P = np.array([p for _, _, p, _ in obs])
    lr = 0.5
    for _ in range(iters):
        q = 1 / (1 + np.exp(-(s[A] - s[B])))
        g = np.zeros_like(s)
        np.add.at(g, A, P - q)
        np.add.at(g, B, q - P)
        g -= lam * s
        s += lr * g / max(1, len(obs) / len(ids))
        s -= s.mean()
    return dict(zip(ids, s))


def best_slot(u, strength, order):
    """order: labelled ids best-first. Return gap index k (0 = above first, len = below last)."""
    pu = [1 / (1 + np.exp(-(strength[u] - strength[l]))) for l in order]
    costs = []
    for k in range(len(order) + 1):
        costs.append(sum(pu[:k]) + sum(1 - x for x in pu[k:]))
    return int(np.argmin(costs)), costs


def gap_score(k, order, sc, frac=0.5):
    """Score inside gap k; frac 0 = next to the track above, 1 = next to the track below."""
    hi = sc[order[k - 1]] if k > 0 else 100.0
    lo = sc[order[k]] if k < len(order) else 0.0
    if k == 0:
        hi = min(100.0, sc[order[0]] + 2)
    if k == len(order):
        lo = max(0.0, sc[order[-1]] - 4)
    if k > 0 and k < len(order) and order_tier(order[k - 1]) != order_tier(order[k]):
        hi, lo = sc[order[k - 1]], sc[order[k]]
    return hi - (hi - lo) * (0.2 + 0.6 * frac)


_TIERS: dict[str, str] = {}


def order_tier(t):
    return _TIERS[t]


def main():
    labels = read_labels(EVAL.parent / "labels.csv")
    sc = anchored_scores(labels)
    pos = {r["id"]: f"{r['tier']}{r['rank_within_tier']}" for r in labels}
    _TIERS.update({r["id"]: r["tier"] for r in labels})
    order = [r["id"] for r in labels]
    obs = load()
    ids = sorted({t for a, b, _, _ in obs for t in (a, b)})
    unl = [t for t in ids if t not in sc]
    st = fit_bt(ids, obs)

    # judge check on labelled pairs
    rank = {t: i for i, t in enumerate(order)}
    agree = cross = cross_ok = n = 0
    for a, b, p, _ in obs:
        if a in rank and b in rank and p != 0.5:
            n += 1
            ok = (p > 0.5) == (rank[a] < rank[b])
            agree += ok
            if _TIERS[a] != _TIERS[b]:
                cross += 1
                cross_ok += ok
    from scipy.stats import spearmanr
    rho = spearmanr([st[t] for t in order], [-rank[t] for t in order])[0]

    def place(strength):
        res = {}
        slots = {}
        for u in unl:
            k, _ = best_slot(u, strength, order)
            slots.setdefault(k, []).append(u)
        for k, us in slots.items():
            us.sort(key=lambda t: -strength[t])
            for i, u in enumerate(us):
                frac = 0.5 if len(us) == 1 else i / (len(us) - 1)
                res[u] = (k, gap_score(k, order, sc, frac))
        return res

    main_pl = place(st)
    # bootstrap
    random.seed(7)
    boots = {u: [] for u in unl}
    for _ in range(200):
        samp = [random.choice(obs) for _ in obs]
        b = place(fit_bt(ids, samp, iters=200))
        for u in unl:
            boots[u].append(b[u][1])

    def slot_text(k, score):
        if k == 0:
            return f"above {pos[order[0]]}"
        if k == len(order):
            return f"below {pos[order[-1]]}"
        a, b = pos[order[k - 1]], pos[order[k]]
        return f"between {a} and {b}" + (f" in {tier_of(score)}" if a[0] != b[0] else "")

    lines = []
    for u in sorted(unl, key=lambda t: -main_pl[t][1]):
        k, s = main_pl[u]
        tier = tier_of(s)
        if k > 0 and k < len(order) and _TIERS[order[k - 1]] != _TIERS[order[k]]:
            tier = tier_of(s)
        lo, hi = np.percentile(boots[u], [10, 90])
        lo, hi = min(lo, s - 3), max(hi, s + 3)
        wins = [(p if a == u else 1 - p) for a, b, p, _ in obs if u in (a, b)]
        lines.append({"id": u, "position": slot_text(k, s), "tier": tier, "score": round(s, 1),
                      "score_low": round(max(0, lo), 1), "score_high": round(min(100, hi), 1),
                      "strength": round(st[u], 3), "win_share": round(float(np.mean(wins)), 3),
                      "boot_same_tier": round(float(np.mean([tier_of(x) == tier for x in boots[u]])), 2)})
    (EVAL / "placements" / "pairwise.jsonl").write_text("".join(json.dumps(l) + "\n" for l in lines))

    with open(PW / "strengths.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "status", "strength", "user_position"])
        for t in sorted(ids, key=lambda t: -st[t]):
            w.writerow([t, "labelled" if t in sc else "unlabelled", round(st[t], 3), pos.get(t, "")])

    tiers = {"S": 0, "A": 0, "B": 0}
    for l in lines:
        tiers[l["tier"]] += 1
    md = ["# Blind pairwise tournament: summary", "",
          f"- verdicts: {len(obs)} (of 595 pairs)",
          f"- judge agreement with the user on labelled-vs-labelled pairs: {agree}/{n} = {agree / max(n, 1):.0%}"
          f" (cross-tier pairs only: {cross_ok}/{cross} = {cross_ok / max(cross, 1):.0%})",
          f"- Spearman between blind strength and the user's order (18 labelled): {rho:.2f}",
          f"- predicted tiers for the 17: S {tiers['S']} / A {tiers['A']} / B {tiers['B']}"
          " (a random 50/50 split would give about 7 / 7 / 4)", ""]
    md += ["| id | slot | tier | score | 80% range | same tier in bootstrap |", "|---|---|---|---|---|---|"]
    md += [f"| {l['id']} | {l['position']} | {l['tier']} | {l['score']} | {l['score_low']}–{l['score_high']} |"
           f" {l['boot_same_tier']:.0%} |" for l in lines]
    (PW / "summary.md").write_text("\n".join(md) + "\n")
    print("\n".join(md))


if __name__ == "__main__":
    main()
