# eval/ — blind instrumental taste prediction

## Purpose

35 instrumental MP3s, identified only by random ids (`blind/labeled/*.mp3`: 18, `blind/unlabeled/*.mp3`: 17).
The user ranked the labelled half into tiers **S / A / B** (with a rank inside each tier) in `../labels.csv`.
The goal is to predict where the unlabelled 17 would land, without hearing the audio and without knowing what the
tracks are.

The assistant cannot listen, so each track gets a **packet**: stems, transcriptions, beats, chords, sections and
plots that let a text/image reader perceive the music. The work then runs in this order:

1. packets for all 35 tracks (`run.py`)
2. `listening_notes.md` for every track, written **before** reading labels
3. cross-checks (CLAP neighbours, small leave-one-out models)
4. taste profile from labels + notes, validation, per-track placements, predictions, report

Everything runs on CPU. All code, models, caches and temp files stay inside `eval/`.

## Blindness safeguards

- `../.claude/settings.json` denies `Read(./private/**)`, `Read(./tracks/**)` and `Read(~/blind-test-archive/**)`.
  The pipeline only reads `blind/` and (for the models step only) `labels.csv`.
- Nothing outside the project folder is read or written. No web lookups, fingerprinting or other attempts to
  identify tracks or artists. If a packet makes a reader think they recognise a piece, the notes say so in one
  marked line that is not used in any judgment.
- Listening notes are written from the packet alone, before `labels.csv` is read. Note writers are also barred
  from `eval/crosscheck/` (see `tools/NOTES_BRIEF.md`), because `crosscheck/models.*` holds label-derived scores.
- `run.py`'s cross-check stage reads `labels.csv` itself (only `lib/crosscheck.py: loo_models`) and writes the
  results to `crosscheck/models.{md,json}`. It is gated: it only runs once every track has a
  `listening_notes.md`, so a normal `run.py` can't produce label-derived output during the blind stage.
- **Disclosure:** the labels of two tracks, `t0d513ac8` and `t21aaeadf`, were seen by accident early on via
  `head -3 labels.csv`. Both tracks' `listening_notes.md` start with a disclosure line; treat those two notes, and
  any validation that uses them, as possibly biased.

## Quick start

Requires system `python3`, `git` (for madmom) and `ffmpeg`/`ffprobe` on `PATH` (tested with ffmpeg 8.1.2).

```bash
bash eval/setup_env.sh          # one-time: builds eval/.venv (Python 3.12 via uv), ~6 GB of caches once models download
python eval/run.py              # all packets (cached stages reused) + cross-checks
python eval/run.py --only t0d513ac8 t21aaeadf   # just these packets; cross-checks are skipped
python eval/run.py --skip-packets               # cross-checks only
python eval/run.py --skip-crosschecks           # packets only
python eval/run.py --force      # delete each packet's stems/ and data/ and recompute everything
```

`run.py` can be started with any Python: if it isn't already running inside `eval/.venv` it re-execs itself
there. It sets `HF_HOME`, `TORCH_HOME`, `MPLCONFIGDIR`, `NUMBA_CACHE_DIR` and `XDG_CACHE_HOME` to `eval/.cache/…`
and `TMPDIR` to `eval/.cache/tmp`. Logs go to the console and `eval/logs/run.log`. It exits 1 if any packet fails.

Layout created by setup: `.bootstrap/` (a small venv that only holds `uv`), `.uv/python/` (the Python 3.12
interpreter), `.venv/`, `.cache/{pip,uv,huggingface,torch,…}`.

Helper: `python3 eval/tools/skim.py <id> [bars_per_section=3] [max_chars=230]` prints the first N bars of every
section from `score.md`, a compact way to read a whole piece.

## Pipeline stages and caching

`lib/packet.py: build_packet` runs five stages per track. Stages 1–4 are expensive and cached. Stage 5 is cheap
and always reruns, rewriting every text file and image.

| # | stage | tool | cache file (in `packets/<id>/`) |
|---|---|---|---|
| 1 | source separation | Demucs `htdemucs_6s`, shifts=1, overlap 0.25 | `stems/{drums,bass,other,vocals,guitar,piano}.mp3` (160 kbps) |
| 2 | beats + downbeats | beat_this `final0` + madmom DBN (falls back to minimal peak picking, then librosa, then a synthetic 60 BPM grid) | `data/beats.json` |
| 3 | transcription | Basic Pitch per pitched stem; 3-band onset detection on the drum stem | `data/notes_{bass,other,vocals,guitar,piano,drums}.json` |
| 4 | chords | madmom DeepChroma + chord recogniser on the sum of the pitched stems (the "drumless mix") | `data/chords_raw.json` (10 fps chroma + segments) |
| 5 | analysis | librosa, numpy, custom code, ffmpeg `ebur128` | all other packet files; `data/DONE` holds the packet version (3) |

- A stage is skipped whenever its cache file exists; to recompute one, delete that file. `--force` deletes
  `stems/` and `data/` for the tracks being processed.
- Once cached, stems are decoded from the MP3s, so reruns analyse the lossy stems and not the float Demucs output.
  Stem levels can shift by a fraction of a dB between the first run and later runs.
- Before transcription, a stem whose 95th-percentile RMS is below −50 dBFS is marked `silent`. Notes are also
  dropped where the stem sits more than 35 dB below its own p95 (with a floor of −48 dBFS), which removes bleed.
- The cross-checks are cached separately: `crosscheck/clap_embeddings.npz` is reused while the track list is
  unchanged, and `--force` does not clear it. Delete the file to recompute the embeddings.

## Packet file guide (`packets/<id>/`)

Recommended reading order: `summary.md` → `clap_tags.md` → `mel.png`/`energy.png` → `skim.py` → targeted
lookups in `score.md` / `bars.md` / `chords.md`.

| file | what it is / how to read it |
|---|---|
| `summary.md` | One-page overview. Duration, bars × beats/bar, median BPM with beat-interval CV and pulse clarity (mean beat activation at the beats, 0–1). Top-2 Krumhansl–Kessler keys from transcribed notes and from chroma (r = correlation). Loudness: integrated LUFS, LRA, true peak, crest, per-bar RMS p10/p90. Source-file quality: codec, bitrate, bandwidth, clipping, side/mid, noise floor. A **Stems** table (share of active bars, note count, range, median pitch, mean confidence, share of notes with confidence < 0.35, velocity median/sd, polyphony, median duration in beats). Then **Sections**, **Harmony** (change rate, repetition 4/8 bars later, common 4-bar progressions, chord qualities fitted from notes), **Melody** (skyline stats and recurring motifs) and **Microtiming & groove**. |
| `sections.md` | Section map from checkerboard novelty on a bar-level self-similarity matrix (chroma + MFCC timbre + stem levels + loudness; minimum 4 bars). Labels such as `A1`, `A2`, `B1`: the same letter means the sections are similar (mean similarity above the 70th percentile). The letters are **not** verse/chorus. Columns: bars, time, energy (low/mid/high = loudness tercile), mean dB, BPM, active stems, brightness, onsets/s, and a chord summary (`loop[…] xN` = repeating cycle, `C(3)` = chord held 3 bars). |
| `chords.md` | Per bar: `madmom` chord (maj/min/N only; `X > Y` = two chords in the bar in time order), `from notes` (best template fit to transcribed pitch classes: 7/maj7/m7/sus/dim/6/add9/9/power `5`, `/X` = bass note, `?` = no good fit), `pcs` (strongest pitch classes). Ends with the raw madmom segments in seconds. |
| `bars.md`, `bars.csv` | Per-bar table: start, duration, local BPM, mix RMS dB, `rel` (dB below the loud bars, p98), brightness (spectral centroid, Hz), onsets/s, active stems (letters D B O V G P; a stem counts as active above −48 dBFS and within 20 dB of the mix), both chord columns, pcs, section. The CSV has the same data; commas inside fields become `;`. |
| `score.md` | Multi-stem per-bar "notation", one block per bar, with a `##` header at each section. Header line: `**bar N** time madmom/notes-chord (dB, active)`. **Drums:** `K:`/`S:`/`H:` rows, one group per beat with 4 steps (16ths) or 6 steps (16th triplets, used when the subdivision test says triplet); `X` strong (≥0.6), `x` medium (≥0.3), `o` soft, `.` none. **Pitched stems:** `note@beat` (1-based within the bar), `[A B]` = struck together, `~n` = held n beats (shown when ≥ 0.9), `?` = confidence < 0.35, `(+n more)` after 18 onset groups. |
| `notes/<stem>.txt` | Full note lists. Pitched: `note  bar:beat  dur(beats)  velocity  confidence`. Bar 000 = pickup. Velocity is the CQT level at the note's pitch relative to the stem's loudest notes, so it is often 110–127. Confidence = √(frame posterior × onset posterior); treat < 0.35 as doubtful. Drums: `kick/snare/hat  bar:beat  strength(0–1)`, with bands kick < 150 Hz, snare 150 Hz–4 kHz, hat > 5 kHz. Long files: search them, don't dump them. |
| `midi/` | `<stem>.mid` per pitched stem (GM programs: bass 33, other 81, vocals 65, guitar 26, piano 0), `drums.mid` (kick 36, snare 38, hat 42) and `all.mid`. Times are in seconds, with the tempo set to the median BPM. |
| `beats.csv` | `time_s, bar, beat_in_bar, tracked`. `tracked=0` marks beats extrapolated before or after the tracker's output. Times come from the smoothed grid. |
| `features.json` | Everything behind `summary.md` in machine-readable form (sections, stem stats, drum hit counts, microtiming, melody, harmony, quality, global levels). This is the input to the cross-check models. |
| `stems/*.mp3` | Demucs stems, for spot checks. The names are the model's guesses (see limitations). |
| `mel.png` | Mel spectrogram with dashed section boundaries and labels. |
| `chroma.png` | Bar-synchronous DeepChroma of the drumless mix (rows C…B) with section boundaries. |
| `energy.png` | Top panel: mix RMS per bar with brightness. Bottom panel: per-stem RMS per bar. Shows arrangement, builds and drops. |
| `clap_tags.md` | CLAP zero-shot tags for style, instrument, mood and production. `top` = highest raw text–audio cosine; `stands out` = highest z-score against the other 34 tracks (usually more informative). Weak evidence at style level. Written by the cross-check stage. |
| `listening_notes.md` | Written by the assistant (not generated), following `tools/NOTES_BRIEF.md`. Bold sections: What it is / How it develops / What's striking / What's weak / What I can't tell / Packet reliability / Style tags. |
| `data/` | Cached raw stage outputs (see above). |

### How the custom analysis works (`lib/packet.py`)

- **Bar grid:** beat_this beats are smoothed with a local linear fit over ±4 beats (only where the local tempo is
  steady), which removes the tracker's ~20 ms frame quantisation. Downbeats are snapped to the nearest beat. The
  most common bar length is extrapolated to cover the whole file. Beats before the first downbeat form bar 0.
- **Key:** Krumhansl–Kessler profile correlation, computed on the note pitch-class histogram and on the chroma sum.
- **Chord per bar:** madmom segments are weighted by overlap with the bar. A second chord is shown when it covers
  more than 30% of the bar. The template fit uses transcribed notes weighted by duration × velocity × confidence,
  with a bonus for the bass note and a small penalty for complex chords; a fit score of 0.55 or less shows `?`.
- **Microtiming:** off-beat onsets are compared with 16th vs. triplet positions (the triplet share is about 30% by
  chance, and above 55% switches the grid to 6 steps). The per-stem deviation from the nearest grid step is given in
  ms. Swing = median position of off-beat 8ths (and 16ths) inside the beat, where ratio 1.0 = straight and
  2.0 = triplet swing. The section also gives tempo drift and local BPM p5–p95, plus drum accents by beat position.
- **Melody:** a skyline (the highest note per 16th slot) from the vocals/other/guitar/piano stems (confidence
  ≥ 0.3). Stepwise and leap shares; motifs = 4-note interval patterns that recur at least 3 times.
- **Quality:** ffprobe (codec, bitrate), ffmpeg `ebur128=peak=true` (LUFS, LRA, true peak), sample peak, crest,
  clipped-sample share, bandwidth (highest frequency within 50 dB of the 200 Hz–4 kHz median), side/mid ratio, and
  the level of the quietest 5% of frames.

## Cross-checks (`crosscheck/`, `lib/crosscheck.py`)

These are evidence to test judgments against. They are not the predictions.

| file | contents |
|---|---|
| `clap_embeddings.npz` | `ids`, `emb`: one L2-normalised CLAP audio embedding per track (the mean of up to 30 evenly spaced 10 s windows, skipping near-silent ones). |
| `clap_text.npz` | Normalised text embeddings for the tag vocabularies (style/instrument/mood/production). |
| `similarity.npy` | 35×35 cosine similarity matrix, in the order of `ids`. |
| `neighbors.md`, `neighbors.csv` | For every track, its top-5 **labelled** neighbours by CLAP cosine (`id:sim`), plus the collection-wide median/p10/p90 of off-diagonal similarity for scale. The files contain no labels. |
| `models.md`, `models.json` | **Label-derived.** Leave-one-out models on the 18 labelled tracks, with the anchored score as target. `ridge_all7`, `ridge_music6 (no LUFS)` and `lufs_only` (StandardScaler + RidgeCV, alpha chosen in each fold) and `clap_knn3` (similarity-weighted mean of the 3 nearest labelled tracks). Reported: LOO Spearman, exact-tier and within-one-tier accuracy, and MAE. The JSON adds per-track LOO predictions, coefficients, predictions and tiers for the unlabelled tracks, single-feature Spearman correlations, and the feature table. The 7 features are pulse clarity, harmonic richness, dynamic contrast, section variety, melody presence, tempo and integrated LUFS (LUFS is a confound probe). |

## Score scale (`lib/scale.py`)

Tiers map to fixed bands on a 0–100 scale, with 8-point gaps between tiers:

| tier | band |
|---|---|
| S | 82–98 |
| A | 52–74 |
| B | 12–44 |

Inside a tier, ranks are evenly spaced from the top of the band to the bottom; a tier with one track sits mid-band.
`tier_of(score)` maps a score back to a tier using the gap midpoints: S ≥ 78, A ≥ 48, otherwise B.

## Downstream artefacts (Steps 3–6) and how they fit

```
labels.csv ─► lib/scale.py ─► labeled_scores.csv (anchored 0–100 scale)
     │                                   │
listening_notes.md ×18 + track_table ─► taste_profile.md (v1) ─► validation/round1 ─► taste_profile.md (v2) ─► validation/round2
                                                                                        │
tools/PLACEMENT_BRIEF.md (side by side vs all 18) ─► 17 subagents ─► placements/<id>.md (+ tiebreaks.md)
                                                                                        │ reviewed, ties broken
                                                         placements/placements.jsonl ─► tools/assemble.py
                                                                                        ├─► predictions.csv
                                                                                        ├─► combined_order.md
                                                                                        └─► tiers/{S,A,B}/  ("N - <id>" symlinks)
labeled_scores.csv + predictions.csv ─► tools/plot_scores.py ─► scores.png ─► report.md
```

| file | contents |
|---|---|
| `taste_profile.md` | What the user values, in listener terms, with evidence tracks and strength marks, plus the loudness/quality confound check. Version 2; v1 and v2 are copied in `validation/`. |
| `labeled_scores.csv` | Anchored scores for the labelled tracks (`lib/scale.py`). |
| `validation/` | Leave-one-out placement by judgement: `round{1,2}.csv`, metrics from `placement_kit.py score-validation`, and a README with the revision and the leakage disclosure. |
| `tools/PLACEMENT_BRIEF.md` | The brief each prediction subagent followed (one per unlabelled track). |
| `placements/<id>.md` | Per-track reasoning (pass 2, final): a holistic side-by-side verdict against **all 18** labelled tracks, the flip point, why here, uncertainty, and a main-session review line. `tiebreaks.md` orders tracks that share a slot by pairwise comparison. `placements.jsonl` holds the reviewed final values; `pass2_raw.jsonl` the subagents' raw replies. `pass1/` keeps the earlier anchor-based pass. |
| `predictions.csv` | id, predicted_tier, estimated_rank_within_tier (among unlabelled tracks in that tier), position, score, 80% range, confidence, top-3 CLAP neighbours, ridge-model tier, two-sentence rationale. |
| `combined_order.md`, `tiers.txt`, `tiers/` | Labelled and predicted tracks in one order. `tiers/<T>/N - <id>[ (predicted)]` are relative symlinks to the track's MP3 when the audio folders exist (`../labeled`, `../unlabeled` or `blind/…`), otherwise to its packet. Rebuild with `python3 eval/tools/assemble.py eval/placements/placements.jsonl`. |
| `scores.png` | Every track's score with 80% error bars on the shaded tier bands (`tools/plot_scores.py`). |
| `report.md` | Plain-language results for the user. |

The steps above need only `numpy scipy matplotlib` (no venv or audio).

## Known limitations

- **Stem names are guesses.** Demucs 6-stem routes a sax, synth lead or violin into `guitar` or `other`, and
  `vocals` in these instrumentals is usually bleed from a lead instrument. Use CLAP instrument tags and
  register/timbre to decide what an instrument really is.
- **Bleed in quiet passages.** In sparse intros and outros, reverb or noise in the drum stem can fill the drum
  grid, and pitched stems can pick up ghost notes. The level gates reduce this but don't remove it.
- **madmom chords are maj/min/N only.** With thirdless (power-chord) voicings, major vs. minor is unreliable. The
  `from notes` column is richer but inherits transcription errors.
- **Transcription confidence.** In packet v4 most stems have 1–15% low-confidence notes. Clearly higher shares
  (>25%, e.g. the guitars in t5fe4a915) point to distortion, dense mixes or noisy timbres: trust roots and form more
  than exact pitches. Velocity mostly reflects level, not playing dynamics. (Packets before v4 had a frame-mapping bug
  that made confidence decay with time; all packets were rebuilt.)
- **Tempo and meter.** The tempo can be off by 2× or 3/2 (e.g. t3c988896 tracks at 150 but feels like 75 with a
  half-time backbeat). The tracker can also switch level mid-track (tde35730e: 140 → 70 BPM at bar 20; t728b4b03:
  a ×2/3 switch at bar 51), which invalidates that track's tempo-CV, drift and microtiming figures. A "3 beats/bar"
  reading may be a misread 6/8 or 12/8. Single-bar jumps (tc8f1d0c8) are tracker slips; a smooth multi-bar glide
  (ted929feb's closing ritardando) is real. A high beat-interval CV is the warning sign.
- **Microtiming depends on the grid.** All deviations and swing figures are measured against the tracked (smoothed)
  grid. If the grid is doubtful, so are the groove numbers.
- **Sections are statistical.** A change of texture can split a passage that sounds continuous, and boundaries can
  sit one bar off the true phrase (t61233098, td231b399). Letters mark similarity, not song form. A section's mean
  dB understates a fade. Energy labels are dB below the track's loudest bars (high > −4, mid > −10, low); the first
  build used within-track tertiles, which could call a section 0.3 dB quieter than its neighbours "low".
- **Drum rows.** With heavy sub-bass or a four-on-the-floor kick, the kick and snare band detectors often fire on the
  same hit, so the backbeat can't always be read. The drum-vs-grid mean offset ranges −18 to +5 ms across tracks
  (median ≈ −1 ms); a single track's offset can't be split into feel vs. grid placement.
- **Harmony labels.** madmom can name a slash chord by its bass triad (Bm/A read as D) and may call a whole
  arpeggiated passage one chord while the bass moves. Key estimates often confuse relative major/minor, and a
  repeated pedal note can skew the notes-based key (t61233098: C#m vs. the true F#m).
- **Stem level vs. notes.** A stem can count as "active" by level (bleed) while holding no notes.
- **Quality metrics describe the file, not the music.** LUFS, true peak, bandwidth and clipping describe mastering
  and source encoding.
- **CLAP tags are coarse.** The model often confuses neighbouring genres. The collection-relative "stands out"
  list is more useful than raw scores.

## Tool choices

Versions as installed in `eval/.venv` (Python 3.12.14, CPU only).

| tool | version | license | role / why |
|---|---|---|---|
| Demucs (maintained fork `github.com/adefossez/demucs`) | 4.1.0 | MIT | Source separation with `htdemucs_6s` (drums, bass, other, vocals, guitar, piano), weights from HF `adefossez/HTDemucs-6s`. The six stems give separate guitar and piano lines. The fork is maintained (release 2026-07). |
| Basic Pitch (Spotify) | 0.4.0 | Apache-2.0 | Polyphonic note transcription per stem. Runs its bundled ONNX model through onnxruntime 1.30.0, because its `tensorflow<2.15.1` pin doesn't support Python 3.12 / numpy 2. Installed with `--no-deps`. |
| beat_this (CPJKU) | 1.1.0 | MIT | Beats and downbeats (checkpoint `final0`), post-processed with madmom's DBN. Robust across genres. |
| madmom | 0.17.dev0 (git `27f032e`) | code BSD; bundled models CC BY-NC-SA 4.0 (fine for personal non-commercial use) | DeepChroma chord recognition (maj/min/N) and the DBN beat post-processor. The PyPI 0.16.1 release (2018) is broken on modern numpy. |
| librosa | 0.11.0 (pinned `<1`) | ISC | Features (RMS, centroid, MFCC, CQT, mel), onsets, drum-band onset picking. librosa 1.0.0 (2026-08) is newer than Basic Pitch's API expectations. |
| ffmpeg / ffprobe (system) | 8.1.2 | LGPL/GPL (build dependent) | Decode and encode (no torchaudio I/O), probing, EBU R128 loudness via `ebur128`. |
| transformers + CLAP | 5.17.0; model `laion/larger_clap_music_and_speech` | Apache-2.0 / Apache-2.0 | Audio embeddings for neighbours, and zero-shot tags. `laion/larger_clap_music` was tried first but gives collapsed embeddings under transformers 5.17: audio–audio cosine ≈ 0.98 between unrelated clips, `logit_scale` 0.027, text similarities ≈ 0. `laion/clap-htsat-unfused` behaved normally in the same setup, which isolated the fault to that checkpoint, so the pipeline switched to `larger_clap_music_and_speech`. |
| torch / torchaudio | 2.11.0+cpu | BSD-3-Clause | Runtime for Demucs, beat_this and CLAP. torchaudio is only needed by beat_this's import chain. |
| scikit-learn | 1.9.1 | BSD-3-Clause | RidgeCV + StandardScaler for the LOO cross-check models. |
| scipy / numpy | 1.18.1 / 2.5.3 | BSD-3-Clause | Spearman correlation, numerics. |
| matplotlib | 3.11.2 | Matplotlib (PSF-style) | Packet images and `scores.png`. |
| pretty_midi | 0.2.11.post0 | MIT | MIDI export. |
| uv | (in `.bootstrap/`) | MIT / Apache-2.0 | Installs Python 3.12 and the venv inside `eval/`. |
| custom (`lib/packet.py`) | packet v3 | — | Bar grid, per-bar table, novelty sections, chord per bar, key, microtiming, melody/motifs, drum transcription, quality metrics (see above). |
