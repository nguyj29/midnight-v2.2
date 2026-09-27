# Brief: blind pairwise judgements

You judge pairs of instrumental tracks for one listener. You can't hear audio; each track is described in a
listening note. Tracks are known only by codes (p01…p35).

## Rules
- Read ONLY: this brief, `eval/pairwise/TASTE.md`, your batch file, and the notes `eval/pairwise/notes/pXX.md`
  your batch needs. Do NOT read anything else in the repo: no `labels.csv`, `packets/`, `crosscheck/`,
  `placements/`, `tiers*`, `report.md`, `taste_profile.md`, `validation/`, `predictions.csv`, `combined_order.md`
  or `pairwise/aliases.json`. The point is that you don't know how the listener ranked anything.
- Don't try to identify songs or artists.
- Write exactly one file, `eval/pairwise/results/<batch>.jsonl`. Change nothing else.

## Task
For each line "pA vs pB" in your batch file: which of the two would this listener rather hear again, judging the
whole listen by `TASTE.md`? Decide every pair; a real toss-up is allowed but should be rare. Judge each pair on
its own merits, and don't try to make your answers add up to a neat ranking. The order within a line means nothing.

Output one JSON object per pair, one per line, in batch order:
`{"a": "pA", "b": "pB", "winner": "pA|pB|tie", "margin": "slight|clear|strong", "why": "<one plain sentence citing a specific moment in each>"}`

## Final reply
Reply with only: `done <batch> <number of pairs>`.
