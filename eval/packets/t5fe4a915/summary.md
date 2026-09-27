# Packet summary — t5fe4a915

- Duration 2:35.2; 58 bars of 4 beats; tempo ≈ 89.4 BPM (beat-interval CV 1.94%); pulse clarity 0.963 (beat_this final0 + madmom DBN).
- Key estimate (from notes): D major r=0.71, B minor r=0.57; (from chroma): F# minor r=0.82, D major r=0.79
- Loudness: -12.0 LUFS integrated, LRA 12.1 LU, true peak 0.5 dBTP, crest 16.3 dB; per-bar RMS p10/p90 [-29.5, -14.1] dBFS.
- Source file: mp3 263 kbps 48000 Hz; bandwidth ≈ 20015 Hz; clipped samples 5.91e-05; side/mid -4.1 dB; quietest-5% frame level -33.3 dB.
- Brightness median 838 Hz; onset rate 2.98/s.

## Stems

| stem | active bars | notes | range | median | mean conf | low-conf | vel med/sd | polyphony | med dur (beats) |
|---|---|---|---|---|---|---|---|---|---|
| bass | 78% | 255 | F1-G2 | D2 | 0.48 | 7% | 126/8.6 | 1.0 | 0.4 |
| other | 71% | 135 | F#2-A6 | F#4 | 0.39 | 28% | 116/19.5 | 1.06 | 0.23 |
| vocals | 0% | 0 (silent) | | | | | | | |
| guitar | 79% | 292 | D2-C5 | Bb3 | 0.41 | 31% | 120/13.3 | 1.18 | 0.36 |
| piano | 62% | 64 | D2-C#7 | C#3 | 0.42 | 17% | 126/14.1 | 1.03 | 0.2 |
| drums | 86% | hits {'kick': 1278, 'snare': 399, 'hat': 291} | | | | | | | |

Stem level (90th pct RMS dBFS): drums -16.7, bass -24.4, other -20.9, vocals -76.8, guitar -21.6, piano -26.2

## Sections

| section | bars | time | energy | dB | stems | chords |
|---|---|---|---|---|---|---|
| A1 | 1–8 | 0:00.0–0:21.5 | low | -30.1 | OP | N(8) |
| B1 | 9–16 | 0:21.5–0:42.9 | high | -15.8 | DBGP | Bm Bm > F# Bm Bm > F# F# > Bm Bm > F# D D > F# |
| C1 | 17–20 | 0:42.9–0:53.7 | high | -14.7 | DBOGP | D(4) |
| D1 | 21–29 | 0:53.7–1:17.8 | high | -15.1 | DBOG | N(2) N > D D(2) F#m Bm F#m F# |
| B2 | 30–40 | 1:17.8–1:47.3 | high | -15.4 | DBGP | Bm > G G > D D Bm Bm > A Bm Bm > F# F# Bm > F# Bm > D D > F# |
| C2 | 41–56 | 1:47.3–2:29.9 | high | -14.7 | DBOG | D(4) N(2) N > D D(3) Bm Bm > F#m F# > Bm G D(2) |
| A2 | 57–58 | 2:29.9–2:35.2 | low | -33.2 |  | D N |

## Harmony

- Chord changes per bar 0.91; distinct chords 7; same chord 4 bars later 0.15, 8 bars later 0.16.
- Most common (madmom): [('D', 24), ('Bm', 17), ('N', 15), ('F#', 11), ('F#m', 3), ('G', 3), ('A', 1)]
- Common 4-bar progressions: [['N | N | N | N', 3], ['D | D | D | D', 2], ['D | D | N | N', 2], ['N | N | N > D | D', 2]]
- Chord qualities fitted from notes: [('5', 17), ('maj', 11), ('aug', 8), ('maj7', 7), ('m', 3), ('sus4', 3), ('maj9', 2), ('dim', 2), ('sus2', 1), ('6', 1)] (unknown 0.0)

## Melody (skyline of non-bass stems)

- 362 skyline notes, range D2-C#7 (p10–p90 B2-A4), stepwise 28%, leaps ≥4th 61%, mean |interval| 7.97 st.
- Skyline comes from: {'guitar': 213, 'other': 107, 'piano': 42}; melody present in 57/58 bars.
- Recurring 4-note interval motifs: [-8, 4, 4] ×4 (bars [19, 21, 43, 45])

## Microtiming & groove

Deviations are measured against a locally smoothed beat grid divided into 4 steps per beat (16th notes).
- drums: n=1720, mean offset -1.3 ms, mean |dev| 29.9 ms, sd 41.2 ms, 42% within 10 ms of the grid, 56% within 15% of a grid step
- bass: n=255, mean offset -1.9 ms, mean |dev| 37.6 ms, sd 44.8 ms, 17% within 10 ms of the grid, 37% within 15% of a grid step
- other: n=135, mean offset -2.6 ms, mean |dev| 38.7 ms, sd 45.4 ms, 12% within 10 ms of the grid, 39% within 15% of a grid step
- guitar: n=292, mean offset 2.6 ms, mean |dev| 29.4 ms, sd 38.9 ms, 32% within 10 ms of the grid, 56% within 15% of a grid step
- piano: n=64, mean offset -10.0 ms, mean |dev| 32.5 ms, sd 38.8 ms, 20% within 10 ms of the grid, 45% within 15% of a grid step
- Subdivision: 23% of informative off-beat onsets sit nearer a triplet grid than a 16th grid (~30% if onsets were placed at random; well under that = straight 16ths, >60% = triplet/compound feel)
- 8th swing: off-beat at 0.492 of the beat (ratio 0.97; 1.0 straight, 2.0 triplet)
- 16th swing: ratio 1.39
- Tempo: IBI CV 1.94%, drift 0.46 BPM/min, local BPM p5–p95 [89.1, 89.7]
- Drum hit strength sd 0.248; hits by beat [count, mean strength]: {'kick': {'1': [115, 0.63], '2': [99, 0.67], '3': [123, 0.62], '4': [104, 0.64]}, 'snare': {'1': [49, 0.81], '2': [46, 0.87], '3': [47, 0.8], '4': [46, 0.87]}, 'hat': {'1': [50, 0.81], '2': [46, 0.85], '3': [47, 0.82], '4': [46, 0.85]}}

## Files

- `sections.md`, `chords.md`, `bars.md`/`bars.csv`, `score.md` (per-bar multi-stem view), `notes/*.txt`, `midi/*.mid`, `beats.csv`, `features.json`, `stems/*.mp3`, `mel.png`, `chroma.png`, `energy.png`, `clap_tags.md`
