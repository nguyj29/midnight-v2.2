# Brief: placing one unlabelled track by holistic side-by-side comparison (pass 2)

You are predicting where the user would rank one blind instrumental track (`<id>`) among the 18 tracks they have
already ranked. You can't hear audio; you work from written listening notes. The user asked for a **holistic,
side-by-side** method: compare your track directly with **every one** of their 18 ranked tracks, judging each
pair on the whole listen, and slot it where the verdicts flip. Don't reason from a few fixed reference tracks.

## Hard rules
- Do NOT read `private/`, `tracks/`, `blind/`, `eval/crosscheck/models.*`, `eval/placements/` (other tracks'
  placements) or anything outside `/home/user/repo`. Don't try to identify the song or artist. If you think you
  recognise it anyway, write one line "**Recognition.** I think this may be … (not used)" and ignore it.
- Write exactly one file: `eval/placements/<id>.md` (overwrite it). Change nothing else.
- The user has **no music-theory background**. Use listener terms (mood, energy, catchiness, build, variety,
  texture, sound). No chord names, keys, scale or mode names in your prose.

## Read
1. `eval/taste_profile.md`: background on what this user seems to like. Use it to inform your ear, but judge
   each pair **as a whole**: "if they put these two on back to back, which would they rather hear again?"
2. `eval/crosscheck/track_table.md`: one line per track. Labelled tracks come first in the user's order
   (S1 = favourite … B4 = least liked).
3. `eval/packets/<id>/listening_notes.md`: your track, in full.
4. The listening notes of **all 18** labelled tracks (`eval/packets/<labelled id>/listening_notes.md`). Focus on
   "In plain words", "How it develops" and "What's striking/weak".

## Method
1. For each of the 18 labelled tracks, in the user's order (S1 … B4), give a side-by-side verdict: **theirs**
   (the user would prefer the labelled track), **this** (they'd prefer yours) or **even**. Add one sentence of
   why, citing a specific moment in each where it matters.
2. If the user's taste is consistent, the verdicts read "theirs … theirs, this … this" down the list. Slot your
   track at the flip. If the verdicts aren't clean, choose the slot with the fewest verdicts that disagree
   with it, and name those disagreements; they're the uncertainty.
3. Write the slot as "between X and Y", "above S1" or "below B4" (X/Y = S3, A5, …). If it straddles a tier
   boundary, append " in S", " in A" or " in B". Get the point score from
   `python3 eval/tools/placement_kit.py slot-score --labels labels.csv --position "<slot>"` (run in
   `/home/user/repo`).
4. **80% range** on the 0–100 scale (bands: S 82–98, A 52–74, B 12–44). Base it on the verdicts: a clean flip
   gives about ±10 points, while disagreements or "even" verdicts widen it toward where they point.
   Confidence: high / medium / low.

## Output file `eval/placements/<id>.md` (about 400–600 words)
```
# <id> — predicted <slot> (<tier>, score N, 80% range L–H)

**What it sounds like.** 2–3 plain sentences.

**Side by side with all 18.**
| # | track | verdict | why |
|---|---|---|---|
| S1 | short description | theirs / this / even | one sentence |
… (all 18 rows)

**Where it flips.** Where the verdicts turn, and any disagreements.

**Why here.** 3–5 sentences: the overall impression that decides it, what pulls it up and what pulls it down.

**Uncertainty.** What could move it, and in which direction.

**Rationale (two sentences).** Exactly two sentences, for predictions.csv.
```

## Final reply
Reply with ONLY one JSON line, no other text:
`{"id": "<id>", "position": "<slot>", "tier": "S|A|B", "score": N, "score_low": L, "score_high": H, "confidence": "high|medium|low", "disagreements": <count>, "rationale": "<the two sentences>"}`
