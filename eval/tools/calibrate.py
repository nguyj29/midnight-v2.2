"""Calibrate the side-by-side placements to the random 50/50 split.

The 35 tracks were split into labelled/unlabelled at random, so the unlabelled 17 should spread over the user's
scale the way the labelled 18 do (about 7 S / 7 A / 4 B). The side-by-side judges lean low: a judge knows which
labelled tracks the user loves, so close calls go to the labelled track. Validation round 1 showed the same lean.

This script keeps the side-by-side ORDER of the unlabelled tracks (what the comparisons measure) and replaces
their positions by quantile matching: the k-th best unlabelled track gets the score at the same quantile of the
labelled scores. The 80% range keeps its half-widths around the new score. The raw side-by-side values are kept
in fields `sbs_*`.

Usage: python3 eval/tools/calibrate.py eval/placements/placements.jsonl > eval/placements/calibrated.jsonl
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

EVAL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(EVAL))

from lib.scale import anchored_scores, read_labels, tier_of  # noqa: E402


def quantile_score(q: float, desc: list[float]) -> float:
    """Score at quantile q (0 = top) of the labelled scores, linear between order statistics."""
    pos = min(max(q * len(desc) - 0.5, 0.0), len(desc) - 1.0)
    i = int(pos)
    j = min(i + 1, len(desc) - 1)
    return desc[i] + (desc[j] - desc[i]) * (pos - i)


def position(score: float, labs: list[tuple[str, float]]) -> str:
    above = [p for p, s in labs if s > score]
    below = [p for p, s in labs if s < score]
    if not above:
        return f"above {below[0]}"
    if not below:
        return f"below {above[-1]}"
    slot = f"between {above[-1]} and {below[0]}"
    return slot + (f" in {tier_of(score)}" if above[-1][0] != below[0][0] else "")


def main(path: str):
    rows = [json.loads(l) for l in Path(path).read_text().splitlines() if l.strip()]
    rows.sort(key=lambda r: -float(r["score"]))
    labels = read_labels(EVAL.parent / "labels.csv")
    sc = anchored_scores(labels)
    labs = sorted(((f"{r['tier']}{r['rank_within_tier']}", sc[r["id"]]) for r in labels), key=lambda x: -x[1])
    desc = [s for _, s in labs]
    n = len(rows)
    for k, r in enumerate(rows):
        new = round(quantile_score((k + 0.5) / n, desc), 1)
        lo_w, hi_w = float(r["score"]) - float(r["score_low"]), float(r["score_high"]) - float(r["score"])
        out = dict(r)
        out.update({f"sbs_{f}": r[f] for f in ("position", "tier", "score", "score_low", "score_high")})
        out.update({"score": new, "tier": tier_of(new), "position": position(new, labs),
                    "score_low": round(max(0.0, new - lo_w), 1), "score_high": round(min(100.0, new + hi_w), 1)})
        first = r["rationale"].split(". ")[0].rstrip(".") + "."
        out["sbs_rationale"] = r["rationale"]
        out["rationale"] = (f"{first} Side by side it ranked {k + 1} of {n} among the unlabelled tracks, which after "
                            f"calibrating to the random 50/50 split puts it {out['position']}.")
        print(json.dumps(out, ensure_ascii=False))


if __name__ == "__main__":
    main(sys.argv[1])
