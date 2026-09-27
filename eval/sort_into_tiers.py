#!/usr/bin/env python3
"""Sort the 35 blind tracks into S / A / B folders, in ranked order.

Usage (from the folder that holds your audio, e.g. the one with labeled/ and unlabeled/):
    python sort_into_tiers.py                 # dry run: shows what it would do, changes nothing
    python sort_into_tiers.py --go            # copies files into ./tiers_sorted/S, A, B
    python sort_into_tiers.py --go --move     # moves instead of copying
    python sort_into_tiers.py --src PATH --out PATH --go

Each file is named "N - <id>.mp3" (N = place inside its tier, 1 = top). Predicted tracks get
" (predicted)". Files are found by id anywhere under --src (any audio extension). Nothing is overwritten.
Needs only Python 3 (Windows, macOS, Linux).
"""
import argparse
import shutil
import sys
from pathlib import Path

# Final order (blind pairwise tournament). (id, predicted?)
TIERS = {
    "S": [("t68bc6fa5", False), ("t8aca41eb", False), ("t5fe4a915", False), ("t0d513ac8", False), ("t052c16ae", True), ("td816798a", True), ("ted929feb", True), ("t6ce48b07", True), ("t77478144", False), ("t9d4d0c39", False), ("tc8f1d0c8", False)],
    "A": [("t728b4b03", True), ("tee211b9a", True), ("tac555977", False), ("t3c988896", True), ("t0a1b3f2b", True), ("t511aa9f7", True), ("td83c7b30", True), ("t949d0c28", True), ("t9fb064e8", False), ("t94fd0413", False), ("t47e13f42", True), ("t3b9d70c1", False), ("tde35730e", False), ("td231b399", False), ("t21aaeadf", False)],
    "B": [("t61233098", False), ("te0e7d7c7", True), ("td5b1c789", True), ("ted20dc6f", False), ("tf4ea87ef", True), ("tb20bad3c", False), ("t709e8ec1", True), ("t8d54bfc3", False), ("t2e8079b2", True)],
}
AUDIO = {".mp3", ".wav", ".flac", ".m4a", ".ogg", ".aac", ".opus", ".aiff", ".aif"}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--src", default=".", help="folder to search for the audio (default: current folder)")
    ap.add_argument("--out", default="tiers_sorted", help="output folder (default: tiers_sorted)")
    ap.add_argument("--go", action="store_true", help="actually copy/move (default is a dry run)")
    ap.add_argument("--move", action="store_true", help="move files instead of copying")
    a = ap.parse_args()

    src, out = Path(a.src).resolve(), Path(a.out).resolve()
    wanted = {tid for tier in TIERS.values() for tid, _ in tier}
    found = {}
    for p in src.rglob("*"):
        if p.is_file() and p.suffix.lower() in AUDIO and out not in p.parents and p.stem in wanted:
            found.setdefault(p.stem, []).append(p)

    missing = sorted(wanted - found.keys())
    dupes = {k: v for k, v in found.items() if len(v) > 1}
    verb = "move" if a.move else "copy"
    print(f"{'DRY RUN - ' if not a.go else ''}{verb} {len(found)} of {len(wanted)} tracks into {out}")
    for tid, paths in dupes.items():
        print(f"  note: {tid} found {len(paths)} times, using {paths[0]}")

    for tier, items in TIERS.items():
        d = out / tier
        if a.go:
            d.mkdir(parents=True, exist_ok=True)
        for n, (tid, pred) in enumerate(items, 1):
            if tid not in found:
                continue
            s = found[tid][0]
            dst = d / f"{n} - {tid}{' (predicted)' if pred else ''}{s.suffix.lower()}"
            print(f"  {tier}/{dst.name}  <-  {s}")
            if a.go:
                if dst.exists():
                    print(f"    skipped: {dst} already exists")
                    continue
                (shutil.move if a.move else shutil.copy2)(str(s), str(dst))

    if missing:
        print(f"\nnot found under {src} ({len(missing)}): {', '.join(missing)}")
    if not a.go:
        print("\nNothing changed. Run again with --go to do it.")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
