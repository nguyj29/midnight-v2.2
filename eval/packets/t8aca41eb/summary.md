# Packet summary — t8aca41eb

- Duration 2:35.5; 75 bars of 4 beats; tempo ≈ 114.9 BPM (beat-interval CV 0.23%); pulse clarity 0.921 (beat_this final0 + madmom DBN).
- Key estimate (from notes): A minor r=0.84, A major r=0.65; (from chroma): F major r=0.80, A minor r=0.77
- Loudness: -11.0 LUFS integrated, LRA 5.0 LU, true peak 2.0 dBTP, crest 16.6 dB; per-bar RMS p10/p90 [-35.4, -13.2] dBFS.
- Source file: mp3 257 kbps 48000 Hz; bandwidth ≈ 20381 Hz; clipped samples 6.04e-05; side/mid -7.7 dB; quietest-5% frame level -50.7 dB.
- Brightness median 2544 Hz; onset rate 3.54/s.

## Stems

| stem | active bars | notes | range | median | mean conf | low-conf | vel med/sd | polyphony | med dur (beats) |
|---|---|---|---|---|---|---|---|---|---|
| bass | 0% | 0 (silent) | | | | | | | |
| other | 89% | 1663 | G2-E7 | G4 | 0.5 | 3% | 114/13.0 | 2.66 | 0.29 |
| vocals | 25% | 128 | A3-D5 | C5 | 0.63 | 2% | 127/9.8 | 1.04 | 0.29 |
| guitar | 39% | 378 | D2-C5 | A3 | 0.5 | 6% | 123/16.0 | 1.61 | 0.27 |
| piano | 8% | 0 (silent) | | | | | | | |
| drums | 85% | hits {'kick': 441, 'snare': 691, 'hat': 738} | | | | | | | |

Stem level (90th pct RMS dBFS): drums -11.8, bass -78.1, other -18.4, vocals -21.0, guitar -28.3, piano -74.3

## Sections

| section | bars | time | energy | dB | stems | chords |
|---|---|---|---|---|---|---|
| A1 | 1–10 | 0:00.1–0:20.9 | mid | -21.6 | O | N(2) Bb Bb > N Am(2) Bb(2) Am N |
| B1 | 11–26 | 0:20.9–0:54.3 | high | -13.5 | DOG | loop[Bb Am] x4.0 |
| C1 | 27–34 | 0:54.3–1:11.0 | high | -14.7 | DOV | loop[Bb Am] x2.0 |
| C2 | 35–42 | 1:11.0–1:27.7 | high | -12.6 | DOVG | Bb Bb > Dm Am(2) Bb(2) Am Am > N |
| B2 | 43–58 | 1:27.7–2:01.1 | high | -13.6 | DO | loop[Bb Am] x4.0 |
| D1 | 59–65 | 2:01.1–2:15.7 | high | -15.8 | DO | N(2) Am(2) Bb(2) Am |
| E1 | 66–75 | 2:15.7–2:35.5 | low | -53.3 |  | N(10) |

## Harmony

- Chord changes per bar 0.53; distinct chords 4; same chord 4 bars later 0.76, 8 bars later 0.78.
- Most common (madmom): [('Bb', 30), ('Am', 30), ('N', 17), ('Dm', 1)]
- Common 4-bar progressions: [['Am | Am | Bb | Bb', 11], ['Bb | Bb | Am | Am', 10], ['N | N | N | N', 3], ['Bb | Bb | Am | N', 2]]
- Chord qualities fitted from notes: [('5', 23), ('m', 19), ('m7', 11), ('aug', 5), ('sus4', 3), ('maj', 2), ('maj9', 2)] (unknown 0.13)

## Melody (skyline of non-bass stems)

- 847 skyline notes, range G2-E7 (p10–p90 Bb3-A5), stepwise 29%, leaps ≥4th 57%, mean |interval| 6.85 st.
- Skyline comes from: {'other': 679, 'guitar': 93, 'vocals': 75}; melody present in 65/75 bars.
- Recurring 4-note interval motifs: [4, 0, 0] ×7 (bars [6, 12, 24, 44, 48, 50, 64]); [-7, 7, 0] ×7 (bars [11, 16, 19, 29, 35, 41, 48]); [0, 0, -4] ×6 (bars [6, 16, 24, 41, 49, 51]); [7, -7, 7] ×6 (bars [11, 29, 37, 38, 45]); [0, -12, 12] ×5 (bars [4, 18, 35, 43, 60]); [-7, 7, -7] ×5 (bars [5, 29, 37, 38, 45])

## Microtiming & groove

Deviations are measured against a locally smoothed beat grid divided into 4 steps per beat (16th notes).
- drums: n=1210, mean offset -2.9 ms, mean |dev| 10.1 ms, sd 13.8 ms, 62% within 10 ms of the grid, 87% within 15% of a grid step
- other: n=1663, mean offset 8.1 ms, mean |dev| 30.5 ms, sd 34.7 ms, 17% within 10 ms of the grid, 34% within 15% of a grid step
- vocals: n=128, mean offset 7.6 ms, mean |dev| 31.9 ms, sd 36.1 ms, 16% within 10 ms of the grid, 28% within 15% of a grid step
- guitar: n=376, mean offset 2.3 ms, mean |dev| 23.3 ms, sd 29.4 ms, 30% within 10 ms of the grid, 53% within 15% of a grid step
- Subdivision: 19% of informative off-beat onsets sit nearer a triplet grid than a 16th grid (~30% if onsets were placed at random; well under that = straight 16ths, >60% = triplet/compound feel)
- 8th swing: off-beat at 0.496 of the beat (ratio 0.98; 1.0 straight, 2.0 triplet)
- 16th swing: ratio 1.0
- Tempo: IBI CV 0.23%, drift 0.06 BPM/min, local BPM p5–p95 [114.9, 115.4]
- Drum hit strength sd 0.298; hits by beat [count, mean strength]: {'kick': {'1': [53, 0.81], '2': [52, 0.62], '3': [30, 0.65], '4': [53, 0.66]}, 'snare': {'1': [57, 0.75], '2': [56, 0.74], '3': [48, 0.75], '4': [60, 0.76]}, 'hat': {'1': [54, 0.67], '2': [57, 0.61], '3': [47, 0.6], '4': [53, 0.59]}}

## Files

- `sections.md`, `chords.md`, `bars.md`/`bars.csv`, `score.md` (per-bar multi-stem view), `notes/*.txt`, `midi/*.mid`, `beats.csv`, `features.json`, `stems/*.mp3`, `mel.png`, `chroma.png`, `energy.png`, `clap_tags.md`
