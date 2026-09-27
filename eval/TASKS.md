# TASKS

## Setup
- [x] `.claude/settings.json` denies reads of `private/**` and `tracks/**` (already present; left unchanged)
- [x] Isolated Python 3.12 env inside `eval/` (uv-managed; caches + temp files in eval/.cache; setup_env.sh)
- [x] Check current versions + licenses of tools; record in README (draft by subagent; finalise at end)

## Step 1 — Packets
- [x] Packet pipeline end to end on one track (t0d513ac8; fixed velocity, bleed gates, grid smoothing, triplet check)
- [x] Batch: packets for all 35 tracks
- [x] listening_notes.md for all 35 tracks (written before reading labels)

## Step 2 — Cross-checks
- [x] Pretrained embeddings for all tracks + nearest labeled neighbours for unlabeled (CLAP; tags written into packets)
- [x] Small regularized linear model, leave-one-out evaluation

## Step 3 — Taste profile
- [x] Read labels.csv (notes column empty for all tracks)
- [x] Write taste_profile.md
- [x] Loudness/mastering/audio-quality confound check
- [x] Anchored scores in labeled_scores.csv

## Step 4 — Validation
- [x] Round 1 leave-one-out validation by judgment
- [x] Revise taste profile once
- [x] Round 2 validation; report both

## Step 5 — Prediction
- [x] One subagent per unlabeled track, anchor comparisons
- [x] Review each subagent's reasoning; reconcile with cross-checks
- [x] predictions.csv

## Step 6 — Report
- [x] scores.png
- [x] report.md
- [x] README.md explains how pieces fit
- [ ] `python eval/run.py` runs clean (needs the local venv + audio; not possible in the cloud session: re-run locally)

## Found along the way
- [x] `laion/larger_clap_music` gives collapsed embeddings under transformers 5.17 (audio-audio sim 0.98, logit scale 0.027); switched to `laion/larger_clap_music_and_speech` (verified sane). Record in README.
- [x] Per-track placement reasoning saved as eval/placements/<id>.md (user asked for analysis of why each track is placed where it is)
- [x] After predictions.csv is locked: add "Artist/track guesses" section to report.md (sounds-like per track; specific guesses only where the music points to one; not used in any placement). Agreed with user 2026-09-27.
- [x] Listening notes split across subagents at user's request (brief: eval/tools/NOTES_BRIEF.md); review each
- [x] Code review of packet pipeline (subagent) -> act on confirmed findings
- [x] Chart script eval/tools/plot_scores.py (subagent; reviewed sample render)
- [x] (kept full position text; readable at this size) plot_scores.py: compact "between A2 and A3" position labels (e.g. "A2–A3") once real predictions exist
- [x] t61233098 notes reviewed (subagent) — chord cycle verified against chords.md
- [x] README limitations: key-from-notes can be skewed by a repeated pedal/ostinato note (t61233098: C#m vs true F#m); section boundaries can sit one bar off true phrase lines
- [x] t68bc6fa5 notes reviewed (subagent) — Am–F–E loop verified
- [x] BUG (found by notes subagent): header tempo from median of 20 ms-quantised beat intervals (140 BPM read as 142.9). Fixed: tempo from smoothed grid.
- [x] (done in session 1; notes were re-checked against v4) After batch: rerun analysis stage for all packets (cached stems/notes/chords reused) and correct tempo mentions in notes written so far (t3b9d70c1, t68bc6fa5, t5fe4a915)
- [x] Blindness guard: label-reading LOO models only run once all 35 tracks have listening_notes.md (raised by README subagent)
- [x] Validation/placement tooling eval/tools/placement_kit.py (subagent; verified anchors/slot-score/score-validation on synthetic labels)
- [x] t77478144 notes reviewed (subagent) — G/D/F#m/Em loop and A7 at bars 69–70 verified
- [x] BUG (found by notes subagent): trailing fragment bar got absurd bpm/onset rate (t77478144 bar 113: 1363 BPM). Fixed: drop last bar if < half a typical bar. Needs the analysis rerun.
- [x] Code review (subagent) confirmed 6 bugs; all fixed (packet v4): Basic Pitch onset-frame mapping (confidence decayed with time), drum onsets ~21 ms late, edge-bar bpm, ambiguous score beat positions, accent profile dropping anticipated downbeats, swing window including 16th "a". Batch stopped, transcription caches cleared, batch restarted.
- [x] Re-check the 7 notes written on v3 packets against v4 numbers (confidence %, tempo, drum timing, any inference drawn from them): t0d513ac8 t21aaeadf t3b9d70c1 t5fe4a915 t61233098 t68bc6fa5 t77478144
- [x] t8aca41eb notes reviewed (subagent) — Bb↔Am loop verified
- [x] README limitations: section mean dB understates fades (t8aca41eb E1); a stem can be "active" by level from bleed while having 0 notes
- [x] The ranker has no music-theory knowledge (user, 2026-09-27): taste profile + report must explain in listener terms (mood, energy, catchiness, build, variety, sound quality); theory only as evidence for audible effects. Add "In plain words" to notes written before this (8 tracks).
- [x] t8d54bfc3 notes reviewed (subagent) — mostly-C harmony verified; fixed score '@4 in 3/4' display (early notes before next downbeat); needs analysis rerun at end
- [x] t94fd0413 notes reviewed (subagent) — beat-3 drum gap checked in raw hits (real, flagged uncertain); fixed '5.00' labels for hits just before a downbeat
- [x] t9d4d0c39 notes reviewed (subagent); section energy label now absolute (dB below track max: high >-4, mid >-10, low) instead of tertiles — needs analysis rerun
- [x] t9fb064e8 notes reviewed (subagent)
- [x] tac555977 notes reviewed (subagent)
- [x] tb20bad3c notes reviewed (subagent); meter flagged uncertain (3/4 vs 6/8)
- [x] tc8f1d0c8 notes reviewed (subagent); local tempo glitches at 4 bars (tracker), bass stem weak
- [x] td231b399 notes reviewed (subagent); 12-bar cycle verified
- [x] tde35730e notes reviewed (subagent); beat tracker switches tempo octave mid-track (140→70 at bar 20)
- [x] README limitations: beat tracker can switch tempo octave mid-track (tde35730e), which invalidates tempo-CV/drift/microtiming for that track
- [x] ted20dc6f notes reviewed (subagent)
- [x] t052c16ae notes reviewed (subagent)
- [x] t0a1b3f2b notes reviewed (subagent)
- [x] t2e8079b2 notes reviewed (subagent)
- [x] t3c988896 notes reviewed (subagent); tempo likely double (150 vs felt 75), key ambiguous Am/Em — flagged in note
- [x] t47e13f42 notes reviewed (subagent)
- [x] t511aa9f7 notes reviewed (subagent) — amended: evidence favours picked guitar + live kit (post/math-rock) over harp/bells
- [x] t6ce48b07 notes reviewed (subagent)
- [x] README limitations: drum-vs-grid mean offset varies −18 to +5 ms across tracks (median ≈ −1 ms); a single track's offset can't be split into feel vs beat-grid placement
- [x] t709e8ec1 notes reviewed (subagent)
- [x] t728b4b03 notes reviewed (subagent); tempo level switch at bar 51 (2/3 ratio) flagged
- [x] t949d0c28 notes reviewed (subagent)
- [x] td5b1c789 notes reviewed (subagent)
- [x] td816798a notes reviewed (subagent)
- [x] td83c7b30 notes reviewed (subagent); local grid slips flagged
- [x] te0e7d7c7 notes reviewed (subagent)
- [x] report.md: playlist name ideas must be ONE WORD each (user, 2026-09-27)
- [x] ted929feb notes reviewed (subagent); real ritardando at end
- [x] On reading labels: ONLY create empty folders eval/tiers/S, eval/tiers/A, eval/tiers/B (user: no categorizing yet)
- [x] Only once the full combined order exists (labeled + predictions slotted in): fill eval/tiers/{S,A,B} with 'N - <id>' entries (symlinks to packets), predicted ones marked '(predicted)'
- [x] tee211b9a notes reviewed (subagent)
- [x] tf4ea87ef notes reviewed (subagent) — all 35 tracks have listening notes
- [x] Handoff for a cloud session written: eval/HANDOFF.md
- [x] Prediction subagents ran on Opus (user allowed it, 2026-09-27) instead of Sonnet
- [ ] When the user's labeled/unlabeled audio folders arrive: re-run tools/assemble.py so tiers/ links point to the MP3s
