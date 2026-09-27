#!/usr/bin/env python3
"""Print the first N bars of each section from a packet's score.md (a compact read of the whole piece).

usage: python3 eval/tools/skim.py <id> [bars_per_section=3] [max_line_chars=230]
"""
import sys
from pathlib import Path

tid = sys.argv[1]
n = int(sys.argv[2]) if len(sys.argv) > 2 else 3
w = int(sys.argv[3]) if len(sys.argv) > 3 else 230
text = (Path(__file__).resolve().parents[1] / "packets" / tid / "score.md").read_text().splitlines()
count = 0
for line in text:
    if line.startswith("## "):
        print(line)
        count = 0
    elif line.startswith("**bar"):
        count += 1
        if count <= n:
            print(line[:w])
    elif line.startswith("    ") and count <= n and count > 0:
        print(line[:w])
