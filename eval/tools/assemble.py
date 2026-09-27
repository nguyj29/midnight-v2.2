"""Assemble predictions.csv, the combined order and the tiers/ folders from the per-track placements.

Usage: python3 eval/tools/assemble.py placements.jsonl

Input: one JSON line per unlabelled track, as returned by the placement subagents
({id, position, tier, score, score_low, score_high, confidence, rationale}), after review.
Outputs (in eval/):
  predictions.csv       one row per unlabelled track (columns per the brief)
  combined_order.md     labelled + predicted tracks in one order, numbered within each tier
  tiers.txt             the same order as plain text
  tiers/{S,A,B}/        'N - <id>' relative symlinks (predicted ones 'N - <id> (predicted)'); the
                        target is the track's MP3 when the user's audio folders exist
                        (../labeled/<id>.mp3, ../unlabeled/<id>.mp3 or blind/{labeled,unlabeled}/),
                        otherwise its packet folder
"""
from __future__ import annotations

import csv
import json
import os
import shutil
import sys
from pathlib import Path

EVAL = Path(__file__).resolve().parents[1]
ROOT = EVAL.parent
sys.path.insert(0, str(EVAL))

from lib.scale import TIER_ORDER, anchored_scores, read_labels, tier_of  # noqa: E402

AUDIO_DIRS = [ROOT / "labeled", ROOT / "unlabeled", EVAL / "blind" / "labeled", EVAL / "blind" / "unlabeled",
              ROOT / "blind" / "labeled", ROOT / "blind" / "unlabeled"]


def model_tiers() -> dict[str, str]:
    m = json.loads((EVAL / "crosscheck" / "models.json").read_text())["ridge_all7"]
    return m["unlabeled_tier"]


def knn() -> dict[str, str]:
    with open(EVAL / "crosscheck" / "neighbors.csv", newline="") as f:
        rows = list(csv.DictReader(f))
    key = [k for k in rows[0] if k not in ("id", "track", "split")][0]
    idk = "id" if "id" in rows[0] else "track"
    return {r[idk]: " ".join(r[key].split(";")[:3]) for r in rows}


def audio_target(tid: str) -> Path:
    for d in AUDIO_DIRS:
        hits = sorted(d.glob(f"{tid}.*")) if d.is_dir() else []
        if hits:
            return hits[0]
    return EVAL / "packets" / tid


def main(path: str):
    preds = [json.loads(l) for l in Path(path).read_text().splitlines() if l.strip()]
    labels = read_labels(ROOT / "labels.csv")
    lscore = anchored_scores(labels)
    mt, nn = model_tiers(), knn()

    # combined order: sort by score; labelled tracks keep their user order (their scores are strictly decreasing)
    items = [{"id": r["id"], "score": lscore[r["id"]], "tier": r["tier"], "pred": False,
              "label": f"{r['tier']}{r['rank_within_tier']}"} for r in labels]
    for p in preds:
        tier = p["tier"].upper()
        assert tier == tier_of(float(p["score"])) or "in " + tier in p["position"], p
        items.append({"id": p["id"], "score": float(p["score"]), "tier": tier, "pred": True, "p": p})
    # stable ordering: tier first, then score; ties keep labelled before predicted
    items.sort(key=lambda x: (TIER_ORDER.index(x["tier"]), -x["score"], x["pred"]))
    for t in TIER_ORDER:
        n = 0
        for x in items:
            if x["tier"] == t:
                n += 1
                x["n"] = n
        u = 0
        for x in items:
            if x["tier"] == t and x["pred"]:
                u += 1
                x["urank"] = u

    cols = ["id", "predicted_tier", "estimated_rank_within_tier", "position", "score", "score_low", "score_high",
            "confidence", "nearest_neighbors", "model_tier", "rationale"]
    with open(EVAL / "predictions.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for x in items:
            if not x["pred"]:
                continue
            p = x["p"]
            w.writerow([p["id"], x["tier"], x["urank"], p["position"], p["score"], p["score_low"], p["score_high"],
                        p["confidence"], nn.get(p["id"], ""), mt.get(p["id"], ""), p["rationale"]])

    lines = ["# Combined order (labelled + predicted)", "",
             "| tier | # | id | score | status |", "|---|---|---|---|---|"]
    for x in items:
        status = f"predicted ({x['p']['position']}, 80% {x['p']['score_low']}–{x['p']['score_high']})" \
            if x["pred"] else f"labelled {x['label']}"
        lines.append(f"| {x['tier']} | {x['n']} | {x['id']} | {x['score']:.1f} | {status} |")
    (EVAL / "combined_order.md").write_text("\n".join(lines) + "\n")

    txt = ["Tiers in order (1 = top of tier). (predicted) = placed by the model; the others are the user's own ranking."]
    for t in TIER_ORDER:
        txt += ["", f"{t} tier:"] + [f"{x['n']} - {x['id']}" + (" (predicted)" if x["pred"] else "")
                                      for x in items if x["tier"] == t]
    (EVAL / "tiers.txt").write_text("\n".join(txt) + "\n")

    tiers = EVAL / "tiers"
    for t in TIER_ORDER:
        d = tiers / t
        if d.exists():
            shutil.rmtree(d)
        d.mkdir(parents=True)
    for x in items:
        tgt = audio_target(x["id"])
        name = f"{x['n']} - {x['id']}" + (" (predicted)" if x["pred"] else "") + (tgt.suffix if tgt.is_file() else "")
        os.symlink(os.path.relpath(tgt, tiers / x["tier"]), tiers / x["tier"] / name)
    print((EVAL / "combined_order.md").read_text())


if __name__ == "__main__":
    main(sys.argv[1])
