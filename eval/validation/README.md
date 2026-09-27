# Validation (Step 4): leave-one-out placement by judgement

Each of the 18 labelled tracks was held out in turn and placed against the other 17 using only the taste profile,
the track table and the listening notes. The judge is the main session, working in-session. It gave a slot, a
0–100 score and an 80% range. Metrics come from `tools/placement_kit.py score-validation`.

**Leakage (read first).** The judge had seen every label before writing the taste profile and before placing
anything. Holding a track out can't make the judge forget where it sits. Round 1 applied the v1 rules as written
and deliberately set aside each held-out track's own evidence. Even so, both rounds are **optimistic**. Round 2
is close to an in-sample fit, since the revision was made after seeing round 1's errors.

| | round 1 (profile v1) | round 2 (profile v2) |
|---|---|---|
| exact tier | 78% (14/18) | 100% (18/18) |
| within one tier | 100% | 100% |
| Spearman, full order | 0.93 | 0.996 |
| 80%-range coverage | 78% | 100% |
| mean range width | 21.4 points | 19.7 points |
| mean absolute error | 6.0 points | 2.6 points |

Files: `round1.csv` / `round1_metrics.md` / `round1_metrics.json` (and the same for round 2), plus
`taste_profile_v1.md` and `taste_profile_v2.md` (the latter is identical to `../taste_profile.md`).

## Round 1 errors → the one revision
- **S1 (trance), S3 (heavy guitars) and S7 (trip-hop) were placed in A.** v1 penalised game-flavoured music,
  hedged on heavy rock because the only other heavy track (B2) was in B, and put beat tracks in A by default.
  All three were misses at the S/A line, and all three S tracks have a big, physical arrival or a very strong
  atmosphere. → v2 adds **impact** (pattern 1b), drops the game-flavour penalty and lets sparse, atmospheric
  beats reach S.
- **B2 (dark rock riff) was placed in A.** v1 read "dark" as good. → v2 splits dark into *sad, cool or hypnotic*
  (liked) and *sinister or uneasy* (disliked, grouped with tense).

## Range calibration
Round 1 coverage (78%) was close to the 80% target, so the round-1 widths (about ±10 points, mean width 21) are
kept for the predictions. Every round-1 miss was a boundary call where two patterns disagreed, and the misses
were 16–22 points out. So ranges are widened **toward the other tier** when patterns conflict, not
symmetrically. Round 2's 100% coverage is not evidence that the ranges are too wide: it's an in-sample fit.
Narrowing ranges to match it would tune them to leakage.
