# Handoff — state at 2026-09-27 ~03:50 (session 1 → session 2)

Read this first, then `TASKS.md` (checklist, with open items) and `README.md` (pipeline, tools, limitations).
The original task brief is the user's first message in session 1; its requirements are summarised in `TASKS.md`.

## Done
- Step 1 complete: 35 packets (pipeline v4, all rebuilt after 8 bugs were fixed; analysis rerun with late display fixes),
  35 `packets/<id>/listening_notes.md` (4 written by the main session, 31 by subagents following
  `tools/NOTES_BRIEF.md`, each reviewed/spot-checked; several corrected). Every note ends with an experiential
  **In plain words** section.
- Step 2: CLAP embeddings + neighbours (`crosscheck/neighbors.md`), zero-shot tags in each packet. `run.py` cross-check
  step (ridge LOO + CLAP kNN → `crosscheck/models.md/json`) was launched after all notes existed; check it finished
  (`logs/crosscheck.log`). Model features were fixed *before* labels were read (see `lib/crosscheck.py: FEATURES`).
- Labels read (after all notes): `labeled_scores.csv` written (S 98→82, A 74→52, B 44→12, even spacing).
  The user left the note column EMPTY for every track — the taste profile rests on the music only.
- `crosscheck/track_table.md/.csv`: one compact row per track (features + one-line gist from `tools/gists.json`),
  labelled tracks first in the user's order. Use this instead of whole packets wherever possible.
- `tools/placement_kit.py`: anchors / neighbours / slot→score / redact / score-validation (tested on synthetic data).
- `tools/plot_scores.py`: renders `scores.png` from `labeled_scores.csv` + `predictions.csv` (reviewed).
- Empty folders `tiers/S`, `tiers/A`, `tiers/B` exist.

## User's order (labels.csv)
S: t68bc6fa5, t8aca41eb, t5fe4a915, t0d513ac8, t77478144, t9d4d0c39, tc8f1d0c8
A: tac555977, t9fb064e8, t94fd0413, t3b9d70c1, tde35730e, td231b399, t21aaeadf
B: t61233098, ted20dc6f, tb20bad3c, t8d54bfc3

## Remaining (Steps 3–6) and how the user wants them done
1. `taste_profile.md` — explain in LISTENER terms (the user has no music-theory background): mood, energy, catchiness,
   build/variety, texture, sound quality; theory only as evidence for audible effects. Mark strong vs one-or-two-example
   patterns; explicitly check loudness/mastering/quality confounds (LUFS, LRA, bandwidth, clipping are in the table).
   Early hypotheses (NOT yet checked against data): bright/sunny/cute/playful tracks sit low (B3, B4, A7);
   dark/moody/immersive-texture tracks sit high; theatrical "epic/tense" pieces without groove sit low (B1, B2).
   The S tier is stylistically diverse (EDM, house, heavy guitars, breakbeat, cinematic, downtempo, trip-hop).
2. Validation (Step 4): leave-one-out placement of each labelled track against the other 17, by judgment, two rounds
   with one profile revision between. To conserve usage, do it in-session from the track table + notes (not 36
   subagents). Report exact-tier, within-one-tier, Spearman, 80% range coverage; `placement_kit.py score-validation`.
   Disclose leakage: the judge has seen all labels.
3. Predictions (Step 5): one subagent per unlabelled track (17), as the brief requires, but LEAN: give each the taste
   profile, the track table, its own notes, and the anchor list; use model "sonnet" to save usage; each compares
   against S/A/B top+bottom anchors then nearest neighbours in the order, citing specific moments. Review each.
   Save each reasoning to `placements/<id>.md` (the user asked for per-track "why placed here" analysis).
   Output `predictions.csv` (columns per brief; position like "between A2 and A3").
4. Then fill `tiers/S|A|B/` ONLY when the full combined order exists: entries `N - <id>` (symlinks to packets) with the
   unlabelled tracks slotted INTO the user's order and renumbered; predicted ones named `N - <id> (predicted)`.
5. Report (Step 6): plain language; playlist names must be ONE WORD each; after predictions are locked add an
   "Artist/track guesses" section (sounds-like; specific guesses only if the music points to one; not used for placement).
   Show `scores.png`. End the final chat message with headings: Blocked on me, Changed, Found.
6. `python eval/run.py` must run clean end to end (it does for packets; re-verify after everything).

## Things to disclose in "Found"
- Two labels (t0d513ac8 S4, t21aaeadf A7) were seen by accident at the very start (`head -3 labels.csv`); their notes
  carry a disclosure line.
- `laion/larger_clap_music` is broken under transformers 5.17 (collapsed embeddings); switched to
  `laion/larger_clap_music_and_speech`.
- 8 pipeline bugs found by subagent review/notes (see TASKS.md) — all fixed, packets rebuilt, notes corrected.
- A user process `private/rank_server.py` was visible in `ps`; never touched.
- No song was recognised by any note writer.

## User preferences (also in memory)
- No music theory in anything written for the user; experiential "from memory" paraphrases were well received.
- Conserve usage: short chat updates; no long pastes unless asked.

## Cross-check result (read before relying on the models)
`crosscheck/models.md`: every ridge variant scores Spearman ≈ −0.86 to −0.94 in leave-one-out with a huge chosen
alpha (~600). That is the known LOO artefact of a model that predicts ≈ the training mean (dropping a high track
lowers the mean, so predictions anti-correlate with truth) → the 7 features carry essentially no usable signal.
CLAP kNN-3 is weak (−0.29). Treat both as near-uninformative; say so in the report. The single-feature Spearman
list at the bottom of models.md is still useful for the loudness/quality confound check.

## Moving to a cloud session
- Only Steps 3–6 remain; they need the text artefacts only: `labels.csv`, `eval/` minus `.venv`, `.cache`, `.uv`,
  `.bootstrap` and `packets/*/stems/`. Audio (`blind/`) is not needed for Steps 3–6.
- Keep `private/` OUT of the upload (it holds the encrypted key; blindness). Commit `.claude/settings.json` (deny rules).
- `~/.claude` memory does not travel; this file is the source of truth.
- In the cloud, `pip install numpy scipy matplotlib` is enough for `tools/placement_kit.py`, `tools/plot_scores.py`,
  `tools/track_table.py`. `python eval/run.py` (the "done" check) needs the local venv + audio: re-run it locally at
  the end (packets are cached, so it only redoes analysis + cross-checks, ~15 min on CPU).
