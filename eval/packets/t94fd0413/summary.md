# Packet summary — t94fd0413

- Duration 2:15.8; 40 bars of 4 beats; tempo ≈ 69.9 BPM (beat-interval CV 0.21%); pulse clarity 0.97 (beat_this final0 + madmom DBN).
- Key estimate (from notes): F# minor r=0.73, A major r=0.62; (from chroma): A major r=0.86, F# minor r=0.77
- Loudness: -11.4 LUFS integrated, LRA 3.1 LU, true peak 0.8 dBTP, crest 14.9 dB; per-bar RMS p10/p90 [-19.1, -12.3] dBFS.
- Source file: mp3 270 kbps 48000 Hz; bandwidth ≈ 20036 Hz; clipped samples 4.34e-05; side/mid -7.0 dB; quietest-5% frame level -68.9 dB.
- Brightness median 1948 Hz; onset rate 3.76/s.

## Stems

| stem | active bars | notes | range | median | mean conf | low-conf | vel med/sd | polyphony | med dur (beats) |
|---|---|---|---|---|---|---|---|---|---|
| bass | 88% | 362 | C1-F4 | B1 | 0.58 | 8% | 120/19.9 | 1.23 | 0.26 |
| other | 90% | 1334 | E1-F7 | B4 | 0.53 | 6% | 109/18.1 | 2.86 | 0.22 |
| vocals | 40% | 120 | F#3-E6 | A4 | 0.54 | 9% | 127/17.9 | 1.3 | 0.3 |
| guitar | 17% | 353 | E2-F7 | Ab4 | 0.51 | 11% | 110/22.4 | 2.39 | 0.27 |
| piano | 0% | 0 (silent) | | | | | | | |
| drums | 90% | hits {'kick': 312, 'snare': 477, 'hat': 538} | | | | | | | |

Stem level (90th pct RMS dBFS): drums -12.5, bass -14.3, other -19.3, vocals -26.7, guitar -33.9, piano -67.9

## Sections

| section | bars | time | energy | dB | stems | chords |
|---|---|---|---|---|---|---|
| A1 | 0–16 | 0:00.0–0:56.6 | high | -15.4 | DBOV | loop[N F#m B F#m] x3.0 |
| B1 | 17–21 | 0:56.6–1:13.7 | high | -14.8 | DBO | F#m Bm > C#m F#m Bm C#m |
| C1 | 22–32 | 1:13.7–1:51.5 | high | -12.8 | DBO | loop[C F Am Dm] x2.8 |
| B2 | 33–36 | 1:51.5–2:05.2 | high | -15.0 | DBO | loop[F#m Bm] x2.0 |
| D1 | 37–39 | 2:05.2–2:15.5 | low | -65.1 |  | N(3) |

## Harmony

- Chord changes per bar 0.88; distinct chords 9; same chord 4 bars later 0.31, 8 bars later 0.19.
- Most common (madmom): [('F#m', 15), ('Bm', 6), ('N', 4), ('C#m', 4), ('C', 4), ('B', 3), ('F', 3), ('Am', 3)]
- Common 4-bar progressions: [['F#m | B | F#m | F#m', 3], ['F#m | F#m | Bm > C#m | F#m', 3], ['Bm > C#m | F#m | F#m | B', 2], ['C | F | Am | Dm', 2]]
- Chord qualities fitted from notes: [('sus4', 7), ('5', 7), ('m7', 6), ('m9', 5), ('sus2', 5), ('maj', 2), ('m', 2), ('6', 2), ('maj9', 1)] (unknown 0.07)

## Melody (skyline of non-bass stems)

- 585 skyline notes, range F#1-F7 (p10–p90 F#4-F#6), stepwise 26%, leaps ≥4th 57%, mean |interval| 7.75 st.
- Skyline comes from: {'other': 463, 'guitar': 88, 'vocals': 34}; melody present in 36/40 bars.
- Recurring 4-note interval motifs: [2, 0, 0] ×7 (bars [2, 4, 8, 32, 33, 34, 35]); [-7, 2, 0] ×3 (bars [2, 3, 14]); [0, 0, -2] ×3 (bars [2, 14, 31]); [0, 0, 3] ×3 (bars [8, 21, 26]); [0, 3, -3] ×3 (bars [21, 22, 26]); [3, -5, 2] ×3 (bars [29, 30, 31])

## Microtiming & groove

Deviations are measured against a locally smoothed beat grid divided into 4 steps per beat (16th notes).
- drums: n=1179, mean offset -0.6 ms, mean |dev| 6.0 ms, sd 11.8 ms, 89% within 10 ms of the grid, 97% within 15% of a grid step
- bass: n=362, mean offset 11.3 ms, mean |dev| 52.7 ms, sd 60.5 ms, 12% within 10 ms of the grid, 32% within 15% of a grid step
- other: n=1334, mean offset 13.3 ms, mean |dev| 46.6 ms, sd 56.4 ms, 18% within 10 ms of the grid, 46% within 15% of a grid step
- vocals: n=120, mean offset 12.0 ms, mean |dev| 52.8 ms, sd 61.3 ms, 10% within 10 ms of the grid, 35% within 15% of a grid step
- guitar: n=353, mean offset 13.9 ms, mean |dev| 42.6 ms, sd 52.3 ms, 24% within 10 ms of the grid, 48% within 15% of a grid step
- Subdivision: 16% of informative off-beat onsets sit nearer a triplet grid than a 16th grid (~30% if onsets were placed at random; well under that = straight 16ths, >60% = triplet/compound feel)
- 8th swing: off-beat at 0.497 of the beat (ratio 0.99; 1.0 straight, 2.0 triplet)
- 16th swing: ratio 0.98
- Tempo: IBI CV 0.21%, drift -0.02 BPM/min, local BPM p5–p95 [69.8, 70.1]
- Drum hit strength sd 0.245; hits by beat [count, mean strength]: {'kick': {'1': [40, 0.89], '2': [55, 0.51], '3': [1, 0.85], '4': [59, 0.55]}, 'snare': {'1': [36, 0.86], '2': [36, 0.89], '3': [0, 0], '4': [36, 0.87]}, 'hat': {'1': [36, 0.54], '2': [36, 0.82], '3': [5, 0.23], '4': [36, 0.82]}}

## Files

- `sections.md`, `chords.md`, `bars.md`/`bars.csv`, `score.md` (per-bar multi-stem view), `notes/*.txt`, `midi/*.mid`, `beats.csv`, `features.json`, `stems/*.mp3`, `mel.png`, `chroma.png`, `energy.png`, `clap_tags.md`
