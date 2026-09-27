# Packet summary — t47e13f42

- Duration 2:12.6; 69 bars of 4 beats; tempo ≈ 125.0 BPM (beat-interval CV 0.92%); pulse clarity 0.805 (beat_this final0 + madmom DBN).
- Key estimate (from notes): A minor r=0.88, F major r=0.61; (from chroma): A minor r=0.95, C major r=0.67
- Loudness: -7.8 LUFS integrated, LRA 6.1 LU, true peak -0.0 dBTP, crest 9.9 dB; per-bar RMS p10/p90 [-14.3, -7.6] dBFS.
- Source file: mp3 270 kbps 48000 Hz; bandwidth ≈ 20208 Hz; clipped samples 8.55e-08; side/mid -14.1 dB; quietest-5% frame level -17.4 dB.
- Brightness median 792 Hz; onset rate 7.6/s.

## Stems

| stem | active bars | notes | range | median | mean conf | low-conf | vel med/sd | polyphony | med dur (beats) |
|---|---|---|---|---|---|---|---|---|---|
| bass | 97% | 791 | E2-F4 | A2 | 0.58 | 1% | 124/14.6 | 1.33 | 0.32 |
| other | 80% | 1687 | F2-E6 | E4 | 0.59 | 2% | 116/15.9 | 2.63 | 0.27 |
| vocals | 0% | 0 (silent) | | | | | | | |
| guitar | 30% | 577 | F2-C5 | A3 | 0.61 | 1% | 126/17.9 | 1.86 | 0.29 |
| piano | 0% | 0 (silent) | | | | | | | |
| drums | 48% | hits {'kick': 217, 'snare': 138, 'hat': 429} | | | | | | | |

Stem level (90th pct RMS dBFS): drums -10.0, bass -12.3, other -14.1, vocals -70.1, guitar -19.0, piano -60.0

## Sections

| section | bars | time | energy | dB | stems | chords |
|---|---|---|---|---|---|---|
| A1 | 1–4 | 0:00.0–0:07.6 | mid | -15.1 | BOG | Am(4) |
| B1 | 5–20 | 0:07.6–0:38.4 | mid | -12.2 | BOG | loop[Am Am > F Am F Am F] x2.3 |
| C1 | 21–32 | 0:38.4–1:01.5 | high | -7.9 | DBO | loop[Am F] x6.0 |
| B2 | 33–36 | 1:01.5–1:09.1 | high | -10.9 | BO | loop[Am F] x2.0 |
| C2 | 37–44 | 1:09.1–1:24.5 | high | -7.7 | DBO | loop[Am F] x4.0 |
| A2 | 45–52 | 1:24.5–1:39.9 | mid | -11.7 | B | loop[Am F] x4.0 |
| B3 | 53–56 | 1:39.9–1:47.5 | mid | -13.3 | BOG | loop[Am F] x2.0 |
| C3 | 57–64 | 1:47.5–2:02.9 | high | -7.7 | DBO | loop[Am F] x4.0 |
| A3 | 65–69 | 2:02.9–2:12.5 | low | -20.9 | BO | loop[Am F] x2.5 |

## Harmony

- Chord changes per bar 0.91; distinct chords 3; same chord 4 bars later 0.94, 8 bars later 0.92.
- Most common (madmom): [('Am', 38), ('F', 31), ('N', 1)]
- Common 4-bar progressions: [['Am | F | Am | F', 29], ['Am | Am | Am | Am', 1], ['Am | Am | Am | Am > F', 1], ['Am | Am > F | Am | Am', 1]]
- Chord qualities fitted from notes: [('5', 34), ('maj', 13), ('add9', 7), ('m9', 6), ('maj7', 6), ('m7', 1), ('6', 1)] (unknown 0.01)

## Melody (skyline of non-bass stems)

- 1017 skyline notes, range F2-E6 (p10–p90 F3-A5), stepwise 23%, leaps ≥4th 65%, mean |interval| 7.46 st.
- Skyline comes from: {'other': 792, 'guitar': 225}; melody present in 69/69 bars.
- Recurring 4-note interval motifs: [5, 2, -7] ×16 (bars [5, 7, 9, 19, 21, 23, 27, 31, 33, 39, 53, 55, '...']); [-7, 5, 2] ×14 (bars [3, 5, 7, 9, 19, 23, 33, 35, 53, 55]); [2, -7, 5] ×10 (bars [5, 7, 9, 23, 33, 53, 55]); [5, 2, -2] ×8 (bars [3, 5, 7, 9, 33, 35, 53, 55]); [3, -8, 5] ×8 (bars [5, 7, 33, 53, 55]); [5, 3, -8] ×7 (bars [5, 9, 33, 53, 55])

## Microtiming & groove

Deviations are measured against a locally smoothed beat grid divided into 4 steps per beat (16th notes).
- drums: n=474, mean offset 5.3 ms, mean |dev| 7.7 ms, sd 9.7 ms, 91% within 10 ms of the grid, 96% within 15% of a grid step
- bass: n=791, mean offset -1.4 ms, mean |dev| 10.0 ms, sd 14.1 ms, 65% within 10 ms of the grid, 86% within 15% of a grid step
- other: n=1687, mean offset -3.4 ms, mean |dev| 8.9 ms, sd 12.7 ms, 69% within 10 ms of the grid, 90% within 15% of a grid step
- guitar: n=576, mean offset 5.8 ms, mean |dev| 19.3 ms, sd 26.0 ms, 46% within 10 ms of the grid, 61% within 15% of a grid step
- Subdivision: 4% of informative off-beat onsets sit nearer a triplet grid than a 16th grid (~30% if onsets were placed at random; well under that = straight 16ths, >60% = triplet/compound feel)
- 8th swing: off-beat at 0.516 of the beat (ratio 1.07; 1.0 straight, 2.0 triplet)
- 16th swing: ratio 1.13
- Tempo: IBI CV 0.92%, drift -0.06 BPM/min, local BPM p5–p95 [123.6, 126.4]
- Drum hit strength sd 0.358; hits by beat [count, mean strength]: {'kick': {'1': [34, 0.56], '2': [33, 0.84], '3': [39, 0.67], '4': [31, 0.73]}, 'snare': {'1': [33, 0.93], '2': [32, 0.88], '3': [29, 0.92], '4': [28, 0.96]}, 'hat': {'1': [36, 0.89], '2': [38, 0.78], '3': [35, 0.81], '4': [39, 0.78]}}

## Files

- `sections.md`, `chords.md`, `bars.md`/`bars.csv`, `score.md` (per-bar multi-stem view), `notes/*.txt`, `midi/*.mid`, `beats.csv`, `features.json`, `stems/*.mp3`, `mel.png`, `chroma.png`, `energy.png`, `clap_tags.md`
