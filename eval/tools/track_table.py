#!/usr/bin/env python3
"""Compact one-row-per-track table (features + one-line gist) used by the taste profile, validation and placement.

usage: python3 eval/tools/track_table.py  ->  writes eval/crosscheck/track_table.md and .csv
Labels are joined only if eval/labeled_scores.csv exists.
"""
import csv
import json
from pathlib import Path

EVAL = Path(__file__).resolve().parents[1]
GIST = json.loads((EVAL / "tools" / "gists.json").read_text())


def row(tid):
    m = json.loads((EVAL / "packets" / tid / "features.json").read_text())
    q, h, g, mel = m["quality"], m["harmony"], m["global"], m["melody"]
    key = (m["key_from_chroma"][0][1] if m["key_from_chroma"] else "?")
    drums = m["drums"]["active_bar_frac"]
    return {
        "id": tid, "dur_s": m["duration_s"], "bpm": m["tempo_bpm_median"], "meter": m["beats_per_bar_mode"],
        "key": key, "mode": "min" if "minor" in key else "maj",
        "lufs": q["integrated_lufs"], "lra": q["loudness_range_lu"], "crest": q["crest_db"],
        "bandwidth_khz": round(q["bandwidth_hz"] / 1000, 1), "true_peak": q["true_peak_dbtp"],
        "pulse": m["pulse_clarity"], "drums_frac": drums,
        "distinct_chords": h.get("distinct_chords"), "chg_per_bar": h.get("chord_changes_per_bar"),
        "same8": h.get("same_chord_8_bars_later"),
        "melody_frac": round(mel.get("bars_with_melody", 0) / max(m["n_bars"], 1), 2),
        "bright_hz": g["bright_hz_median"], "ons_s": g["onsets_per_s"],
        "sections": len(m["sections"]), "section_letters": len({s["letter"] for s in m["sections"]}),
        "gist": GIST.get(tid, ""),
    }


def main():
    ids = sorted(p.name for p in (EVAL / "packets").iterdir() if (p / "features.json").exists())
    rows = [row(t) for t in ids]
    lab = {}
    f = EVAL / "labeled_scores.csv"
    if f.exists():
        lab = {r["id"]: r for r in csv.DictReader(open(f))}
    for r in rows:
        r["label"] = lab[r["id"]]["position"] if r["id"] in lab else ""
        r["score"] = lab[r["id"]]["score"] if r["id"] in lab else ""
    rows.sort(key=lambda r: (r["label"] == "", -float(r["score"] or 0), r["id"]))
    cols = list(rows[0].keys())
    with open(EVAL / "crosscheck" / "track_table.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)
    short = ["label", "id", "dur_s", "bpm", "mode", "lufs", "lra", "pulse", "drums_frac", "distinct_chords", "same8",
             "melody_frac", "bright_hz", "gist"]
    L = ["# Track table", "", "Labelled tracks first in the user's order, then unlabelled. lufs = integrated loudness; "
         "lra = loudness range (LU); pulse = beat clarity; drums_frac = share of bars with drums; same8 = share of bars "
         "whose chord equals the chord 8 bars earlier (loopiness); melody_frac = share of bars with a skyline melody.", "",
         "| " + " | ".join(short) + " |", "|" + "---|" * len(short)]
    for r in rows:
        L.append("| " + " | ".join(str(r[c]) for c in short) + " |")
    (EVAL / "crosscheck" / "track_table.md").write_text("\n".join(L) + "\n")
    print(f"wrote {len(rows)} rows")


if __name__ == "__main__":
    main()
