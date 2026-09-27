# Packet summary — t0a1b3f2b

- Duration 2:53.1; 65 bars of 4 beats; tempo ≈ 90.0 BPM (beat-interval CV 0.18%); pulse clarity 0.974 (beat_this final0 + madmom DBN).
- Key estimate (from notes): Eb major r=0.80, C minor r=0.75; (from chroma): C minor r=0.88, Eb major r=0.80
- Loudness: -9.3 LUFS integrated, LRA 3.8 LU, true peak 0.7 dBTP, crest 11.8 dB; per-bar RMS p10/p90 [-14.6, -9.9] dBFS.
- Source file: mp3 276 kbps 48000 Hz; bandwidth ≈ 20068 Hz; clipped samples 4.12e-04; side/mid -9.8 dB; quietest-5% frame level -22.1 dB.
- Brightness median 1418 Hz; onset rate 3.39/s.

## Stems

| stem | active bars | notes | range | median | mean conf | low-conf | vel med/sd | polyphony | med dur (beats) |
|---|---|---|---|---|---|---|---|---|---|
| bass | 91% | 439 | F1-D4 | Bb1 | 0.61 | 3% | 127/15.2 | 1.19 | 0.47 |
| other | 100% | 2549 | F1-G6 | Ab3 | 0.52 | 5% | 108/15.8 | 3.9 | 0.3 |
| vocals | 52% | 468 | F2-G7 | Eb4 | 0.57 | 3% | 124/16.3 | 1.32 | 0.33 |
| guitar | 14% | 261 | F2-F7 | Eb4 | 0.54 | 10% | 118/22.7 | 1.55 | 0.26 |
| piano | 0% | 0 (silent) | | | | | | | |
| drums | 97% | hits {'kick': 307, 'snare': 361, 'hat': 873} | | | | | | | |

Stem level (90th pct RMS dBFS): drums -12.7, bass -8.5, other -17.3, vocals -23.1, guitar -32.7, piano -70.9

## Sections

| section | bars | time | energy | dB | stems | chords |
|---|---|---|---|---|---|---|
| A1 | 1–8 | 0:00.2–0:21.5 | mid | -17.9 | DBO | loop[Cm Cm > Ab Fm Bb] x2.0 |
| B1 | 9–16 | 0:21.5–0:42.8 | high | -11.0 | DBOV | Cm(2) Fm Fm > Bb Cm Ab Fm Bb |
| C1 | 17–40 | 0:42.8–1:46.8 | high | -10.6 | DBOV | Cm Ab Fm Bb Cm Ab Fm Bb Cm(2) Fm Bb Cm Cm > Ab Fm Bb Cm ... |
| D1 | 41–48 | 1:46.8–2:08.1 | high | -11.4 | DBO | Cm(2) Fm Bb Cm Cm > Ab Fm Bb |
| E1 | 49–56 | 2:08.1–2:29.5 | high | -10.2 | DBOV | loop[Cm Ab Fm Bb] x2.0 |
| F1 | 57–65 | 2:29.5–2:53.1 | high | -13.4 | DBO | loop[Cm Ab Fm Bb] x2.2 |

## Harmony

- Chord changes per bar 1.03; distinct chords 6; same chord 4 bars later 0.77, 8 bars later 0.74.
- Most common (madmom): [('Cm', 22), ('Fm', 17), ('Bb', 17), ('Ab', 13), ('Eb', 1), ('N', 1)]
- Common 4-bar progressions: [['Cm | Ab | Fm | Bb', 9], ['Fm | Bb | Cm | Ab', 8], ['Cm | Cm > Ab | Fm | Bb', 3], ['Fm | Bb | Cm | Cm', 3]]
- Chord qualities fitted from notes: [('m', 23), ('maj7', 13), ('5', 7), ('sus4', 5), ('7', 5), ('6', 4), ('add9', 2), ('m6', 1), ('maj9', 1), ('sus2', 1)] (unknown 0.0)

## Melody (skyline of non-bass stems)

- 1074 skyline notes, range F1-F7 (p10–p90 G3-Eb5), stepwise 37%, leaps ≥4th 49%, mean |interval| 6.06 st.
- Skyline comes from: {'other': 788, 'vocals': 187, 'guitar': 99}; melody present in 66/65 bars.
- Recurring 4-note interval motifs: [0, -4, 4] ×7 (bars [1, 19, 35, 47, 59, 60, 63]); [1, 0, 0] ×5 (bars [7, 11, 16, 29, 37]); [4, -4, 4] ×4 (bars [0, 21, 49, 60]); [-4, 4, 0] ×4 (bars [1, 19, 35, 60]); [0, 0, -12] ×4 (bars [3, 16, 54, 56]); [-2, 0, 0] ×4 (bars [4, 6, 18, 20])

## Microtiming & groove

Deviations are measured against a locally smoothed beat grid divided into 4 steps per beat (16th notes).
- drums: n=1312, mean offset -14.0 ms, mean |dev| 14.6 ms, sd 8.9 ms, 33% within 10 ms of the grid, 89% within 15% of a grid step
- bass: n=439, mean offset -7.9 ms, mean |dev| 35.5 ms, sd 40.5 ms, 12% within 10 ms of the grid, 34% within 15% of a grid step
- other: n=2547, mean offset 10.3 ms, mean |dev| 38.1 ms, sd 43.1 ms, 13% within 10 ms of the grid, 33% within 15% of a grid step
- vocals: n=468, mean offset 8.6 ms, mean |dev| 39.8 ms, sd 45.4 ms, 12% within 10 ms of the grid, 31% within 15% of a grid step
- guitar: n=261, mean offset 9.2 ms, mean |dev| 35.4 ms, sd 39.0 ms, 9% within 10 ms of the grid, 32% within 15% of a grid step
- Subdivision: 20% of informative off-beat onsets sit nearer a triplet grid than a 16th grid (~30% if onsets were placed at random; well under that = straight 16ths, >60% = triplet/compound feel)
- 8th swing: off-beat at 0.485 of the beat (ratio 0.94; 1.0 straight, 2.0 triplet)
- 16th swing: ratio 0.86
- Tempo: IBI CV 0.18%, drift -0.04 BPM/min, local BPM p5–p95 [89.7, 90.3]
- Drum hit strength sd 0.27; hits by beat [count, mean strength]: {'kick': {'1': [65, 0.74], '2': [66, 0.8], '3': [59, 0.75], '4': [66, 0.73]}, 'snare': {'1': [61, 0.84], '2': [60, 0.85], '3': [59, 0.86], '4': [59, 0.86]}, 'hat': {'1': [62, 0.86], '2': [64, 0.88], '3': [63, 0.83], '4': [63, 0.83]}}

## Files

- `sections.md`, `chords.md`, `bars.md`/`bars.csv`, `score.md` (per-bar multi-stem view), `notes/*.txt`, `midi/*.mid`, `beats.csv`, `features.json`, `stems/*.mp3`, `mel.png`, `chroma.png`, `energy.png`, `clap_tags.md`
