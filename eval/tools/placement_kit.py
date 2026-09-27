"""Placement kit: express a track's placement as a slot in the labelled order and score it.

The labelled tracks form one order S1..Sn, A1..An, B1..Bn. Anchored scores always come from
the FULL label set (lib/scale.py); --exclude ID drops a held-out track from the order shown,
while the other tracks keep their original labels (gaps allowed, e.g. "between A2 and A4").

Positions: "above X", "below X", "between X and Y", "at X" (tied), where X/Y are position
labels (S1, A3, ...) or track ids. A slot between two tiers (e.g. "between S5 and A1") scores
at the band-gap midpoint with a warning; append " in S" / " in A" to pick a side. "above X" with X not at the top means the slot between
X's predecessor and X (likewise "below").

Subcommands (run with eval/.venv/bin/python eval/tools/placement_kit.py <cmd> -h):
    order            markdown table of the (remaining) order with anchored scores
    anchors          top/bottom track of each tier among the remaining tracks
    neighbors        the k tracks on each side of a slot
    slot-score       convert a position into a point score + tier (JSON)
    redact           copy a markdown file without any line/bullet/table row mentioning an id
    score-validation metrics for leave-one-out predictions against the labels
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

EVAL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(EVAL))

from lib.scale import BANDS, TIER_ORDER, anchored_scores, read_labels, tier_of  # noqa: E402


def die(msg: str):
    sys.exit(f"error: {msg}")


def load(path: str, exclude: str | None = None):
    """Return (remaining rows in order, full anchored scores, label map id->'A3')."""
    rows = read_labels(Path(path))
    scores = anchored_scores(rows)
    labels = {r["id"]: f"{r['tier']}{r['rank_within_tier']}" for r in rows}
    if exclude and exclude not in scores:
        die(f"--exclude id {exclude!r} not in labels")
    return [r for r in rows if r["id"] != exclude], scores, labels


def md_table(header: list[str], body: list[list]) -> str:
    fmt = lambda v: f"{v:.1f}" if isinstance(v, float) else str(v).replace("|", "\\|")
    lines = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    return "\n".join(lines + ["| " + " | ".join(fmt(v) for v in row) + " |" for row in body])


def row_cells(r, scores, labels):
    return [labels[r["id"]], r["id"], scores[r["id"]], r["note"]]


def resolve(ref: str, rows, labels) -> int:
    """Index in `rows` of a position label (case-insensitive) or track id."""
    for i, r in enumerate(rows):
        if ref == r["id"] or ref.upper() == labels[r["id"]]:
            return i
    die(f"{ref!r} is not a remaining track (held out, or no such label/id)")


def parse_slot(position: str, rows, labels):
    """Return (kind, left_idx, right_idx); left is the higher-ranked side, None = open end."""
    p = position.strip()
    if m := re.fullmatch(r"between\s+(\S+)\s+and\s+(\S+)", p, re.I):
        a, b = sorted((resolve(m[1], rows, labels), resolve(m[2], rows, labels)))
        if a == b:
            die("between X and X: use 'at X'")
        if b - a > 1:
            skipped = ", ".join(labels[r["id"]] for r in rows[a + 1:b])
            print(f"warning: {m[1]} and {m[2]} are not adjacent (skips {skipped}); "
                  "using the midpoint anyway", file=sys.stderr)
        return "between", a, b
    if m := re.fullmatch(r"(above|below|at)\s+(\S+)", p, re.I):
        i = resolve(m[2], rows, labels)
        kind = m[1].lower()
        if kind == "at":
            return "at", i, i
        if kind == "above":
            return "above", (i - 1 if i > 0 else None), i
        return "below", i, (i + 1 if i + 1 < len(rows) else None)
    die(f"cannot parse position {position!r} (use above X / below X / between X and Y / at X)")


def edge_pad(rows, scores) -> float:
    gaps = [scores[a["id"]] - scores[b["id"]] for a, b in zip(rows, rows[1:]) if a["tier"] == b["tier"]]
    return max(2.0, (sum(gaps) / len(gaps)) / 2 if gaps else 2.0)


def slot_score(position: str, rows, scores, labels) -> dict:
    """Point score for a slot. A cross-tier slot takes an optional ' in T' suffix choosing a side."""
    m = re.fullmatch(r"(.*?)\s+in\s+([SAB])", position.strip(), re.I)
    chosen = m[2].upper() if m else None
    kind, li, ri = parse_slot(m[1] if m else position, rows, labels)
    left, right = (rows[li] if li is not None else None), (rows[ri] if ri is not None else None)
    out = {}
    if kind == "at":
        score = scores[left["id"]]
    elif left is None:
        score = min(100.0, scores[right["id"]] + edge_pad(rows, scores))
    elif right is None:
        score = max(0.0, scores[left["id"]] - edge_pad(rows, scores))
    elif left["tier"] != right["tier"]:
        lt, rt = left["tier"], right["tier"]
        adjacent = TIER_ORDER.index(rt) - TIER_ORDER.index(lt) == 1
        sl, sr = scores[left["id"]], scores[right["id"]]
        # side scores: halfway from the neighbour to its own band edge
        sides = {lt: round((sl + BANDS[lt][1]) / 2, 1), rt: round((sr + BANDS[rt][0]) / 2, 1)}
        out["side_scores"] = sides
        if chosen in sides:
            score = sides[chosen]
        else:
            if chosen:
                die(f"'in {chosen}' is not a side of this slot ({lt}/{rt})")
            score = (BANDS[lt][1] + BANDS[rt][0]) / 2 if adjacent else (sl + sr) / 2
            out["warning"] = (f"slot straddles tiers {lt}/{rt}: {score:.1f} is the gap midpoint; choose a "
                              f"side by appending ' in {lt}' ({sides[lt]}) or ' in {rt}' ({sides[rt]})")
    else:
        score = (scores[left["id"]] + scores[right["id"]]) / 2
    if chosen and "side_scores" not in out:
        die(f"'in {chosen}' only applies to a slot between two tiers")
    side = lambda r: None if r is None else {"label": labels[r["id"]], "id": r["id"], "score": scores[r["id"]]}
    return {"score": round(score, 1), "tier": tier_of(score), "left": side(left), "right": side(right), **out}


def cmd_order(a):
    rows, scores, labels = load(a.labels, a.exclude)
    print(md_table(["pos", "id", "score", "note"], [row_cells(r, scores, labels) for r in rows]))


def cmd_anchors(a):
    rows, scores, labels = load(a.labels, a.exclude)
    body, seen = [], set()
    for t in TIER_ORDER:
        tr = [r for r in rows if r["tier"] == t]
        for name, r in (("top", tr[0]), ("bottom", tr[-1])) if tr else ():
            if r["id"] not in seen:
                seen.add(r["id"])
                body.append([f"{t} {name}"] + row_cells(r, scores, labels))
    print(md_table(["anchor", "pos", "id", "score", "note"], body))


def cmd_neighbors(a):
    rows, scores, labels = load(a.labels, a.exclude)
    kind, li, ri = parse_slot(a.position, rows, labels)
    if kind == "at":
        above_end, below_start = li, li + 1
    else:
        above_end = 0 if li is None else li + 1
        below_start = len(rows) if ri is None else ri
    body = [["above"] + row_cells(r, scores, labels) for r in rows[max(0, above_end - a.k):above_end]]
    body.append([f"**slot: {a.position}**"] + (row_cells(rows[li], scores, labels) if kind == "at" else [""] * 4))
    body += [["below"] + row_cells(r, scores, labels) for r in rows[below_start:below_start + a.k]]
    print(md_table(["side", "pos", "id", "score", "note"], body))


def cmd_slot_score(a):
    rows, scores, labels = load(a.labels, a.exclude)
    out = slot_score(a.position, rows, scores, labels)
    if "warning" in out:
        print(f"warning: {out['warning']}", file=sys.stderr)
    print(json.dumps(out, indent=2))


def cmd_redact(a):
    lines = Path(a.text).read_text().splitlines(keepends=True)
    kept, removed, drop_indent = [], 0, None
    for line in lines:
        indent = len(line) - len(line.lstrip())
        bullet = re.match(r"\s*([-*+]|\d+[.)])\s", line)
        if drop_indent is not None:  # continuation lines of a removed bullet
            if line.strip() and indent > drop_indent:
                removed += 1
                continue
            drop_indent = None
        if a.id.lower() in line.lower():
            removed += 1
            drop_indent = indent if bullet else None
            continue
        kept.append(line)
    text = "".join(kept)
    if a.out:
        Path(a.out).write_text(text)
    else:
        sys.stdout.write(text)
    print(f"redact: removed {removed} line(s) mentioning {a.id}", file=sys.stderr)


def cmd_score_validation(a):
    from scipy.stats import kendalltau, spearmanr

    rows, scores, labels = load(a.labels)
    tier_true = {r["id"]: r["tier"] for r in rows}
    with open(a.results, newline="") as f:
        res = [r for r in csv.DictReader(f) if r.get("id")]
    unknown = [r["id"] for r in res if r["id"] not in scores]
    if unknown:
        die(f"result ids not in labels: {unknown}")
    per, pred, true = [], [], []
    for r in res:
        tid, s, lo, hi = r["id"], float(r["score"]), float(r["score_low"]), float(r["score_high"])
        tt, pt = tier_true[tid], r["predicted_tier"].strip().upper()
        pos, pos_score = (r.get("position") or "").strip(), None
        if pos:
            rem = [x for x in rows if x["id"] != tid]
            pos_score = slot_score(pos, rem, scores, labels)["score"]
        per.append({"id": tid, "true_pos": labels[tid], "true_score": scores[tid], "true_tier": tt,
                    "pred_tier": pt, "score": s, "low": lo, "high": hi, "position": pos,
                    "position_score": pos_score, "tier_hit": pt == tt,
                    "within_one": abs(TIER_ORDER.index(pt) - TIER_ORDER.index(tt)) <= 1,
                    "in_range": lo <= scores[tid] <= hi, "abs_err": round(abs(s - scores[tid]), 1)})
        pred.append(s)
        true.append(scores[tid])
    n = len(per)
    mean = lambda xs: round(sum(xs) / len(xs), 3) if xs else None
    rho, rho_p = spearmanr(pred, true) if n >= 3 else (float("nan"), float("nan"))
    tau, tau_p = kendalltau(pred, true) if n >= 3 else (float("nan"), float("nan"))
    clean = lambda v: None if v != v else float(f"{v:.4g}")
    conf = {t: {p: sum(1 for x in per if x["true_tier"] == t and x["pred_tier"] == p) for p in TIER_ORDER}
            for t in TIER_ORDER}
    metrics = {"n": n, "tier_accuracy": mean([x["tier_hit"] for x in per]),
               "within_one_tier": mean([x["within_one"] for x in per]),
               "spearman_rho": clean(rho), "spearman_p": clean(rho_p),
               "kendall_tau": clean(tau), "kendall_p": clean(tau_p),
               "range80_coverage": mean([x["in_range"] for x in per]),
               "mean_range_width": mean([x["high"] - x["low"] for x in per]),
               "mae_points": mean([x["abs_err"] for x in per]),
               "confusion_true_by_pred": conf, "per_track": per}
    out = Path(a.results).with_name(Path(a.results).stem + "_metrics.json")
    out.write_text(json.dumps(metrics, indent=2))
    yn = lambda b: "hit" if b else "miss"
    print("## Validation metrics\n")
    print(md_table(["metric", "value"], [[k, "n/a" if v is None else str(v)] for k, v in metrics.items()
                                          if k not in ("per_track", "confusion_true_by_pred")]))
    print("\n## Per track\n")
    print(md_table(["id", "true pos", "true score", "pred tier", "pred score", "80% range", "position",
                    "pos score", "tier", "range", "abs err"],
                   [[x["id"], x["true_pos"], x["true_score"], x["pred_tier"], x["score"],
                     f"{x['low']:.1f}-{x['high']:.1f}", x["position"] or "-",
                     "-" if x["position_score"] is None else x["position_score"],
                     yn(x["tier_hit"]), yn(x["in_range"]), x["abs_err"]] for x in per]))
    print("\n## Tier confusion (rows = true, cols = predicted)\n")
    print(md_table(["true \\ pred"] + TIER_ORDER, [[t] + [conf[t][p] for p in TIER_ORDER] for t in TIER_ORDER]))
    print(f"\nwrote {out}", file=sys.stderr)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    def add(name, fn, help_, labels=True, exclude=True, position=False):
        p = sub.add_parser(name, help=help_, description=help_)
        if labels:
            p.add_argument("--labels", required=True, help="labels CSV (id,tier,rank_within_tier,note)")
        if exclude:
            p.add_argument("--exclude", metavar="ID", help="held-out track id to drop from the order")
        if position:
            p.add_argument("--position", required=True,
                           help='"above X" | "below X" | "between X and Y" | "at X" (X = S1/A3/... or id)')
        p.set_defaults(fn=fn)
        return p

    add("order", cmd_order, "Print the order (pos, id, anchored score, note) as markdown.")
    add("anchors", cmd_anchors, "Print top/bottom track of each tier among remaining tracks.")
    add("neighbors", cmd_neighbors, "Print the k tracks on each side of a slot.",
        position=True).add_argument("--k", type=int, default=2, help="tracks per side (default 2)")
    add("slot-score", cmd_slot_score, "Convert a position into a point score; prints JSON "
        "{score, tier, left, right}. Cross-tier slots return the band-gap midpoint with a warning.",
        position=True)
    p = add("redact", cmd_redact, "Copy a markdown file dropping every line, bullet (with its "
            "continuation lines) and table row mentioning ID; count goes to stderr.",
            labels=False, exclude=False)
    p.add_argument("--text", required=True, help="input markdown file")
    p.add_argument("--id", required=True, help="track id to redact (case-insensitive substring)")
    p.add_argument("--out", help="output file (default stdout)")
    p = add("score-validation", cmd_score_validation, "Score leave-one-out predictions; prints markdown "
            "and writes <results-stem>_metrics.json next to the results.", exclude=False)
    p.add_argument("--results", required=True,
                   help="CSV: id,predicted_tier,score,score_low,score_high[,position]")
    a = ap.parse_args(argv)
    a.fn(a)


if __name__ == "__main__":
    main()
