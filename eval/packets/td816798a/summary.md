# Packet summary — td816798a

- Duration 2:30.4; 63 bars of 4 beats; tempo ≈ 98.9 BPM (beat-interval CV 2.12%); pulse clarity 0.864 (beat_this final0 + madmom DBN).
- Key estimate (from notes): A major r=0.78, F# minor r=0.78; (from chroma): D major r=0.85, F# minor r=0.79
- Loudness: -11.6 LUFS integrated, LRA 10.1 LU, true peak 0.6 dBTP, crest 13.0 dB; per-bar RMS p10/p90 [-23.9, -9.7] dBFS.
- Source file: mp3 250 kbps 48000 Hz; bandwidth ≈ 20327 Hz; clipped samples 4.08e-05; side/mid -9.5 dB; quietest-5% frame level -39.5 dB.
- Brightness median 1766 Hz; onset rate 2.77/s.

## Stems

| stem | active bars | notes | range | median | mean conf | low-conf | vel med/sd | polyphony | med dur (beats) |
|---|---|---|---|---|---|---|---|---|---|
| bass | 81% | 337 | B0-E4 | B1 | 0.54 | 8% | 120/21.0 | 1.2 | 0.36 |
| other | 94% | 1969 | E1-E6 | C#4 | 0.55 | 6% | 111/16.1 | 4.23 | 0.35 |
| vocals | 19% | 166 | E2-F#5 | E4 | 0.51 | 11% | 127/15.5 | 2.47 | 0.34 |
| guitar | 13% | 499 | D2-C7 | C#4 | 0.5 | 13% | 111/21.1 | 2.7 | 0.36 |
| piano | 2% | 0 (silent) | | | | | | | |
| drums | 67% | hits {'kick': 348, 'snare': 310, 'hat': 486} | | | | | | | |

Stem level (90th pct RMS dBFS): drums -15.7, bass -10.7, other -21.6, vocals -31.6, guitar -30.7, piano -72.2

## Sections

| section | bars | time | energy | dB | stems | chords |
|---|---|---|---|---|---|---|
| A1 | 0–8 | 0:00.0–0:20.6 | low | -28.7 | BOV | N E Bm E Bm E Bm E E > Bm |
| A2 | 9–17 | 0:20.6–0:42.4 | mid | -12.8 | BO | E Bm E Bm E Bm E G C#m |
| B1 | 18–35 | 0:42.4–1:26.1 | high | -10.4 | DBO | loop[D Bm Bm > D] x4.3 |
| C1 | 36–40 | 1:26.1–1:38.2 | low | -21.1 | DBOVG | D C B F#m(2) |
| B2 | 41–56 | 1:38.2–2:17.0 | high | -11.3 | DBO | D(3) F D(2) G F#m D(2) D > G F D(2) G F#m |
| C2 | 57–60 | 2:17.0–2:26.7 | low | -32.9 | O | F#m > D D(3) |
| A3 | 61–62 | 2:26.7–2:30.4 | low | -108.5 |  | N(2) |

## Harmony

- Chord changes per bar 0.84; distinct chords 10; same chord 4 bars later 0.46, 8 bars later 0.4.
- Most common (madmom): [('D', 28), ('Bm', 14), ('E', 10), ('F#m', 5), ('G', 4), ('N', 3), ('F', 2), ('C#m', 1)]
- Common 4-bar progressions: [['Bm | E | Bm | E', 4], ['D | Bm | Bm > D | D', 3], ['Bm > D | D | D | Bm', 2], ['F | D | D | G', 2]]
- Chord qualities fitted from notes: [('maj7', 11), ('m', 10), ('m9', 10), ('5', 8), ('maj', 8), ('maj9', 6), ('m7', 4), ('dim', 1), ('6', 1), ('7', 1)] (unknown 0.03)

## Melody (skyline of non-bass stems)

- 957 skyline notes, range B1-C7 (p10–p90 E3-F#5), stepwise 17%, leaps ≥4th 62%, mean |interval| 8.11 st.
- Skyline comes from: {'other': 735, 'guitar': 163, 'vocals': 59}; melody present in 60/63 bars.
- Recurring 4-note interval motifs: [3, 4, -12] ×7 (bars [41, 47, 49, 50, 55]); [3, 4, -4] ×6 (bars [14, 39, 40, 51, 53, 58]); [-3, -5, -4] ×6 (bars [40, 42, 48, 50, 52, 59]); [-12, 8, -3] ×5 (bars [22, 41, 47, 49, 50]); [4, -4, -3] ×4 (bars [14, 40, 51, 58]); [8, -3, -5] ×4 (bars [41, 43, 46, 50])

## Microtiming & groove

Deviations are measured against a locally smoothed beat grid divided into 4 steps per beat (16th notes).
- drums: n=762, mean offset -1.6 ms, mean |dev| 10.4 ms, sd 14.3 ms, 59% within 10 ms of the grid, 92% within 15% of a grid step
- bass: n=337, mean offset -0.0 ms, mean |dev| 39.1 ms, sd 45.0 ms, 12% within 10 ms of the grid, 29% within 15% of a grid step
- other: n=1969, mean offset -10.6 ms, mean |dev| 27.0 ms, sd 31.3 ms, 18% within 10 ms of the grid, 52% within 15% of a grid step
- vocals: n=166, mean offset 11.6 ms, mean |dev| 37.8 ms, sd 41.8 ms, 11% within 10 ms of the grid, 28% within 15% of a grid step
- guitar: n=499, mean offset 0.7 ms, mean |dev| 38.0 ms, sd 44.0 ms, 12% within 10 ms of the grid, 32% within 15% of a grid step
- Subdivision: 15% of informative off-beat onsets sit nearer a triplet grid than a 16th grid (~30% if onsets were placed at random; well under that = straight 16ths, >60% = triplet/compound feel)
- 8th swing: off-beat at 0.486 of the beat (ratio 0.95; 1.0 straight, 2.0 triplet)
- 16th swing: ratio 0.99
- Tempo: IBI CV 2.12%, drift 0.08 BPM/min, local BPM p5–p95 [97.4, 101.9]
- Drum hit strength sd 0.299; hits by beat [count, mean strength]: {'kick': {'1': [32, 0.36], '2': [31, 0.7], '3': [25, 0.77], '4': [34, 0.57]}, 'snare': {'1': [30, 0.62], '2': [28, 0.73], '3': [32, 0.82], '4': [29, 0.66]}, 'hat': {'1': [34, 0.64], '2': [34, 0.72], '3': [38, 0.75], '4': [36, 0.64]}}

## Files

- `sections.md`, `chords.md`, `bars.md`/`bars.csv`, `score.md` (per-bar multi-stem view), `notes/*.txt`, `midi/*.mid`, `beats.csv`, `features.json`, `stems/*.mp3`, `mel.png`, `chroma.png`, `energy.png`, `clap_tags.md`
