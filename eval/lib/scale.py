"""Anchored 0-100 score scale derived from the labelled order.

Tier bands (fixed, with gaps of 8 points between tiers):
    S: 82-98    A: 52-74    B: 12-44
Within a tier, ranks are spaced evenly from the top of the band to the bottom (a single track sits mid-band).
"""
from __future__ import annotations

import csv
from pathlib import Path

BANDS = {"S": (98.0, 82.0), "A": (74.0, 52.0), "B": (44.0, 12.0)}
TIER_ORDER = ["S", "A", "B"]


def read_labels(path: Path) -> list[dict]:
    with open(path, newline="") as f:
        rows = [r for r in csv.DictReader(f)]
    for r in rows:
        r["rank_within_tier"] = int(r["rank_within_tier"])
        r["note"] = (r.get("note") or "").strip()
    rows.sort(key=lambda r: (TIER_ORDER.index(r["tier"]), r["rank_within_tier"]))
    return rows


def anchored_scores(rows: list[dict]) -> dict[str, float]:
    out = {}
    for tier in TIER_ORDER:
        tr = [r for r in rows if r["tier"] == tier]
        hi, lo = BANDS[tier]
        n = len(tr)
        for i, r in enumerate(tr):
            out[r["id"]] = round((hi + lo) / 2 if n == 1 else hi - i * (hi - lo) / (n - 1), 1)
    return out


def tier_of(score: float) -> str:
    """Map a score to a tier using the midpoints of the gaps between bands."""
    if score >= (BANDS["S"][1] + BANDS["A"][0]) / 2:
        return "S"
    if score >= (BANDS["A"][1] + BANDS["B"][0]) / 2:
        return "A"
    return "B"


def position_label(rows: list[dict]):
    """Global order labels like S1..Sn, A1.., B1.."""
    return {r["id"]: f"{r['tier']}{r['rank_within_tier']}" for r in rows}
