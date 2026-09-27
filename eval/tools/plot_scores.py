"""Render every track's score (with its 80% range) against the S/A/B tier bands.

Usage:
    eval/.venv/bin/python eval/tools/plot_scores.py [--labeled PATH] [--pred PATH] [--out PATH]

Defaults: eval/labeled_scores.csv, eval/predictions.csv -> eval/scores.png.
Either input may be missing (a warning is printed); at least one must exist.
"""
from __future__ import annotations

import argparse
import csv
import math
import sys
from pathlib import Path

EVAL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(EVAL))

import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402
from matplotlib.patches import Patch  # noqa: E402

from lib.scale import BANDS, TIER_ORDER  # noqa: E402

# Palette (validated categorical slots 1-2, light mode) + neutral ink/surface tokens.
SURFACE = "#fcfcfb"
TEXT_PRIMARY = "#0b0b0b"
TEXT_SECONDARY = "#52514e"
TEXT_MUTED = "#8a8984"
GRID = "#e4e3df"
BAND_FILL = "#eeede8"
LABELED_COLOR = "#2a78d6"  # slot 1, blue
PRED_COLOR = "#eb6834"  # slot 2, orange


def _num(v) -> float:
    try:
        v = (v or "").strip()
        return float(v) if v else math.nan
    except (TypeError, ValueError):
        return math.nan


def load(path: Path, kind: str) -> list[dict]:
    if not path.exists():
        print(f"warning: {path} not found; skipping {kind} tracks", file=sys.stderr)
        return []
    out = []
    with open(path, newline="") as f:
        for r in csv.DictReader(f):
            score = _num(r.get("score"))
            if math.isnan(score):
                print(f"warning: {kind} row {r.get('id')!r} has no score; skipped", file=sys.stderr)
                continue
            out.append({
                "id": (r.get("id") or "").strip(),
                "kind": kind,
                "position": (r.get("position") or "").strip(),
                "score": score,
                "low": _num(r.get("score_low")),
                "high": _num(r.get("score_high")),
            })
    return out


def plot(rows: list[dict], out: Path) -> None:
    # Descending by score, top to bottom; ties: labeled first, then id.
    rows = sorted(rows, key=lambda r: (-r["score"], r["kind"] != "labeled", r["id"]))
    n = len(rows)
    height = max(5.0, 0.28 * n + 2.4)

    plt.rcParams.update({
        "font.size": 10,
        "axes.edgecolor": GRID,
        "axes.labelcolor": TEXT_SECONDARY,
        "xtick.color": TEXT_SECONDARY,
        "ytick.color": TEXT_PRIMARY,
    })
    fig, ax = plt.subplots(figsize=(10, height), dpi=120)
    fig.patch.set_facecolor(SURFACE)
    ax.set_facecolor(SURFACE)

    # Tier bands as vertical spans; the unshaded gaps between them stay visible.
    for tier in TIER_ORDER:
        hi, lo = BANDS[tier]
        ax.axvspan(lo, hi, color=BAND_FILL, zorder=0, lw=0)
        ax.text((hi + lo) / 2, -0.9, f"{tier}  ({lo:g}–{hi:g})", ha="center", va="bottom",
                fontsize=11, fontweight="bold", color=TEXT_SECONDARY)

    # Recessive row guides + vertical grid.
    for y in range(n):
        ax.axhline(y, color=GRID, lw=0.6, zorder=1)
    ax.set_xticks(range(0, 101, 10))
    ax.grid(axis="x", color=GRID, lw=0.6, zorder=1)
    ax.set_axisbelow(True)

    for y, r in enumerate(rows):
        labeled = r["kind"] == "labeled"
        color = LABELED_COLOR if labeled else PRED_COLOR
        lo_, hi_ = r["low"], r["high"]
        has_range = not (math.isnan(lo_) or math.isnan(hi_))
        if has_range:
            ax.plot([lo_, hi_], [y, y], color=color, lw=2, alpha=0.55,
                    solid_capstyle="round", zorder=2)
            ax.plot([lo_, lo_], [y - 0.22, y + 0.22], color=color, lw=1.5, alpha=0.7, zorder=2)
            ax.plot([hi_, hi_], [y - 0.22, y + 0.22], color=color, lw=1.5, alpha=0.7, zorder=2)
        ax.plot(r["score"], y, marker="o" if labeled else "D", ms=8 if labeled else 7,
                color=color, mec=SURFACE, mew=1.5, zorder=3, ls="none")
        # Direct label to the right of the range (or the point): score, plus position.
        right = hi_ if has_range else r["score"]
        text = f"{r['score']:.0f}"
        if r["position"]:
            text += f"  {r['position']}" if labeled else f"  ~{r['position']}"
        ax.text(right + 1.6, y, text, va="center", ha="left", fontsize=8.5,
                color=TEXT_PRIMARY if labeled else TEXT_SECONDARY,
                fontweight="bold" if labeled else "normal", zorder=4, clip_on=False)

    ax.set_yticks(range(n))
    ax.set_yticklabels([r["id"] for r in rows], fontsize=9)
    for tick, r in zip(ax.get_yticklabels(), rows):
        if r["kind"] == "labeled":
            tick.set_fontweight("bold")
        else:
            tick.set_color(TEXT_SECONDARY)
    ax.tick_params(axis="y", length=0, pad=6)
    ax.tick_params(axis="x", length=0)
    ax.set_ylim(n - 0.4, -1.0)
    ax.set_xlim(0, 100)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)

    ax.set_xlabel("Score (0–100 anchored scale)")
    ax.set_ylabel("Track (sorted by score)")
    n_lab = sum(r["kind"] == "labeled" for r in rows)
    ax.set_title(f"Track scores with 80% ranges — {n_lab} labeled, {n - n_lab} predicted",
                 loc="left", fontsize=13, color=TEXT_PRIMARY, pad=22)

    handles = [
        Line2D([], [], marker="o", ls="none", ms=8, color=LABELED_COLOR, mec=SURFACE,
               label="Labeled (anchored; position e.g. S3)"),
        Line2D([], [], marker="D", ls="none", ms=7, color=PRED_COLOR, mec=SURFACE,
               label="Predicted (~estimated position)"),
        Line2D([], [], color=TEXT_MUTED, lw=2, label="80% range"),
        Patch(facecolor=BAND_FILL, edgecolor="none", label="Tier band"),
    ]
    # Legend sits below the x axis so it can never cover a data row.
    leg = ax.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.5, -0.045 * 12 / height),
                    ncol=4, frameon=False, fontsize=9, handlelength=1.8, columnspacing=1.6)
    for t in leg.get_texts():
        t.set_color(TEXT_PRIMARY)

    fig.tight_layout()
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, dpi=120, facecolor=SURFACE)
    plt.close(fig)
    print(f"wrote {out} ({n} tracks)")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--labeled", type=Path, default=EVAL / "labeled_scores.csv")
    ap.add_argument("--pred", type=Path, default=EVAL / "predictions.csv")
    ap.add_argument("--out", type=Path, default=EVAL / "scores.png")
    a = ap.parse_args()
    rows = load(a.labeled, "labeled") + load(a.pred, "predicted")
    if not rows:
        sys.exit("error: no rows to plot (both inputs missing or empty)")
    plot(rows, a.out)


if __name__ == "__main__":
    main()
