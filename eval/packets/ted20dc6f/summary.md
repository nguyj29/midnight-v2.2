# Packet summary — ted20dc6f

- Duration 2:03.0; 45 bars of 4 beats; tempo ≈ 85.4 BPM (beat-interval CV 1.23%); pulse clarity 0.975 (beat_this final0 + madmom DBN).
- Key estimate (from notes): C major r=0.81, G major r=0.65; (from chroma): C major r=0.88, F major r=0.73
- Loudness: -12.8 LUFS integrated, LRA 3.1 LU, true peak -0.9 dBTP, crest 15.4 dB; per-bar RMS p10/p90 [-18.4, -15.1] dBFS.
- Source file: mp3 294 kbps 48000 Hz; bandwidth ≈ 20004 Hz; clipped samples 0.00e+00; side/mid -6.2 dB; quietest-5% frame level -26.0 dB.
- Brightness median 2068 Hz; onset rate 2.58/s.

## Stems

| stem | active bars | notes | range | median | mean conf | low-conf | vel med/sd | polyphony | med dur (beats) |
|---|---|---|---|---|---|---|---|---|---|
| bass | 98% | 404 | E1-C4 | G2 | 0.62 | 1% | 127/13.7 | 1.13 | 0.25 |
| other | 96% | 1264 | F2-G7 | C5 | 0.52 | 8% | 111/15.8 | 3.5 | 0.31 |
| vocals | 13% | 55 | G3-G6 | G4 | 0.45 | 9% | 125/19.6 | 1.24 | 0.25 |
| guitar | 7% | 113 | G2-F5 | C4 | 0.51 | 9% | 124/12.1 | 1.82 | 0.26 |
| piano | 20% | 137 | E2-Bb6 | E4 | 0.56 | 4% | 127/9.1 | 2.22 | 0.31 |
| drums | 89% | hits {'kick': 926, 'snare': 922, 'hat': 709} | | | | | | | |

Stem level (90th pct RMS dBFS): drums -17.7, bass -19.0, other -18.3, vocals -32.7, guitar -44.3, piano -29.0

## Sections

| section | bars | time | energy | dB | stems | chords |
|---|---|---|---|---|---|---|
| A1 | 0–11 | 0:00.0–0:31.7 | mid | -18.7 | DBO | loop[N Am C > G Am] x3.0 |
| B1 | 12–20 | 0:31.7–0:57.0 | high | -16.2 | DBOP | Bb Am Bb Am Bb Am Bb Dm Bb > E |
| A2 | 21–24 | 0:57.0–1:08.2 | high | -16.6 | DBO | Am C > F Am Bb |
| C1 | 25–32 | 1:08.2–1:30.7 | high | -15.2 | DBO | Cm C# Cm C# Cm C# Bb Fm > G |
| D1 | 33–40 | 1:30.7–1:53.1 | high | -15.5 | DBO | Cm(2) Ab Bb > G Cm Eb Ab Fm > G |
| A3 | 41–44 | 1:53.1–2:03.0 | low | -36.0 | DBO | G > Am Am > C F > Am N |

## Harmony

- Chord changes per bar 1.2; distinct chords 13; same chord 4 bars later 0.46, 8 bars later 0.38.
- Most common (madmom): [('Am', 14), ('Bb', 10), ('G', 7), ('Cm', 6), ('C', 5), ('C#', 3), ('N', 2), ('F', 2)]
- Common 4-bar progressions: [['C > G | Am | Bb | Am', 3], ['Bb | Am | C > G | Am', 2], ['Bb | Am | Bb | Am', 2], ['N | Am | C > G | Am', 1]]
- Chord qualities fitted from notes: [('m9', 7), ('m', 7), ('5', 5), ('m7b5', 4), ('aug', 4), ('7', 4), ('sus2', 3), ('maj7', 3), ('m7', 2), ('dim', 2)] (unknown 0.02)

## Melody (skyline of non-bass stems)

- 633 skyline notes, range Ab2-Eb7 (p10–p90 F4-D6), stepwise 24%, leaps ≥4th 59%, mean |interval| 7.24 st.
- Skyline comes from: {'other': 555, 'piano': 41, 'guitar': 21, 'vocals': 16}; melody present in 43/45 bars.
- Recurring 4-note interval motifs: [7, 0, 0] ×7 (bars [5, 7, 11, 19, 22, 23, 31]); [0, -11, 4] ×5 (bars [1, 9, 19, 21, 42]); [0, -4, 4] ×5 (bars [3, 9, 11]); [-7, 7, 0] ×5 (bars [7, 11, 18, 19, 31]); [7, 0, -11] ×4 (bars [1, 9, 19, 42]); [-4, 4, 0] ×4 (bars [3, 9, 10, 20])

## Microtiming & groove

Deviations are measured against a locally smoothed beat grid divided into 4 steps per beat (16th notes).
- drums: n=1647, mean offset 5.4 ms, mean |dev| 30.2 ms, sd 39.9 ms, 36% within 10 ms of the grid, 53% within 15% of a grid step
- bass: n=403, mean offset 3.6 ms, mean |dev| 33.7 ms, sd 43.0 ms, 23% within 10 ms of the grid, 51% within 15% of a grid step
- other: n=1264, mean offset -0.5 ms, mean |dev| 40.4 ms, sd 48.2 ms, 16% within 10 ms of the grid, 37% within 15% of a grid step
- vocals: n=55, mean offset -6.1 ms, mean |dev| 53.8 ms, sd 58.5 ms, 4% within 10 ms of the grid, 16% within 15% of a grid step
- guitar: n=113, mean offset 5.9 ms, mean |dev| 44.1 ms, sd 51.7 ms, 14% within 10 ms of the grid, 30% within 15% of a grid step
- piano: n=137, mean offset 3.0 ms, mean |dev| 23.0 ms, sd 31.6 ms, 33% within 10 ms of the grid, 72% within 15% of a grid step
- Subdivision: 23% of informative off-beat onsets sit nearer a triplet grid than a 16th grid (~30% if onsets were placed at random; well under that = straight 16ths, >60% = triplet/compound feel)
- 8th swing: off-beat at 0.511 of the beat (ratio 1.05; 1.0 straight, 2.0 triplet)
- 16th swing: ratio 1.3
- Tempo: IBI CV 1.23%, drift -0.26 BPM/min, local BPM p5–p95 [85.2, 86.1]
- Drum hit strength sd 0.234; hits by beat [count, mean strength]: {'kick': {'1': [65, 0.58], '2': [89, 0.46], '3': [87, 0.45], '4': [90, 0.46]}, 'snare': {'1': [54, 0.64], '2': [47, 0.61], '3': [68, 0.28], '4': [57, 0.58]}, 'hat': {'1': [50, 0.67], '2': [56, 0.41], '3': [44, 0.31], '4': [59, 0.44]}}

## Files

- `sections.md`, `chords.md`, `bars.md`/`bars.csv`, `score.md` (per-bar multi-stem view), `notes/*.txt`, `midi/*.mid`, `beats.csv`, `features.json`, `stems/*.mp3`, `mel.png`, `chroma.png`, `energy.png`, `clap_tags.md`
