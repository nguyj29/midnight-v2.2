# Brief: placing one unlabelled track in the user's order

You are predicting where the user would rank one blind instrumental track (`<id>`) among the 18 tracks they have
already ranked. You can't hear audio; you work from written listening notes.

## Hard rules
- Do NOT read `private/`, `tracks/`, `blind/`, `eval/crosscheck/models.*` or anything outside `/home/user/repo`.
  Don't try to identify the song or artist (no web lookups, no recognition attempts). If you think you recognise
  it anyway, write one line "**Recognition.** I think this may be … (not used)" and ignore it.
- Write exactly one file: `eval/placements/<id>.md`. Change nothing else.
- Everything you write is read by the user, who has **no music-theory background**. Use listener terms (mood,
  energy, catchiness, build, variety, texture, sound). No chord names, keys, scale or mode names in your prose.
  "The chords turn darker" is fine; "moves to C minor" is not.

## Read, in this order
1. `eval/taste_profile.md`: the user's taste, as a checklist. It's the basis for your judgement.
2. `eval/crosscheck/track_table.md`: one line per track. Labelled tracks come first in the user's order
   (S1 = favourite … B4 = least liked).
3. `eval/packets/<id>/listening_notes.md`: your track. Focus on "In plain words", "How it develops" and
   "What's striking/weak".
4. The listening notes of the six **anchors** (top and bottom of each tier):
   S1 t68bc6fa5, S7 tc8f1d0c8, A1 tac555977, A7 t21aaeadf, B1 t61233098, B4 t8d54bfc3.
5. Then find your track's likely slot and read the notes of the labelled tracks on **both sides** of it (2–4
   tracks), plus any labelled track that is obviously the same kind of music. Useful helpers:
   `python3 eval/tools/placement_kit.py neighbors --labels labels.csv --position "between A2 and A3" --k 2`
   `python3 eval/tools/placement_kit.py slot-score --labels labels.csv --position "between A2 and A3"`
   (run from `/home/user/repo`).

## How to decide
- Compare your track with each anchor, then with the neighbours around your chosen slot. For **each comparison**,
  say which piece the user would probably prefer and **why**, citing a specific moment in both (e.g. "the drop at
  0:27 in S1 vs the flat loop from 0:40 here").
- Settle on a slot: "between X and Y", "above X" or "below X", where X/Y are labels such as S3 or A5. If the slot
  straddles a tier boundary, append " in S", " in A" or " in B". Get the point score from `slot-score`.
- Give an **80% range** (low–high on the 0–100 scale; bands S 82–98, A 52–74, B 12–44). In validation the typical
  honest range was about ±10 points. Widen it toward the other side when two taste patterns disagree (e.g. a
  mood that says S but a flat loop that says A). Confidence: high / medium / low.

## Output file `eval/placements/<id>.md` (about 300–500 words)
```
# <id> — predicted <slot> (<tier>, score N, 80% range L–H)

**What it sounds like.** 2–3 plain sentences.

**Against the anchors.** One short bullet per anchor (six bullets): better or worse for this user, and why.

**Against its neighbours.** 2–4 bullets for the tracks just above and below the chosen slot, same format.

**Why here.** 3–5 sentences tying it to the taste profile patterns (name them, e.g. "impact", "breathes",
"sweet vs immersive"), including what pulls it up and what pulls it down.

**Uncertainty.** What could move it, and in which direction.

**Rationale (two sentences).** Exactly two sentences, for predictions.csv.
```

## Final reply
Reply with ONLY one JSON line, no other text:
`{"id": "<id>", "position": "<slot>", "tier": "S|A|B", "score": N, "score_low": L, "score_high": H, "confidence": "high|medium|low", "rationale": "<the two sentences>"}`
