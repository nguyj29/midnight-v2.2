# Packet summary — t511aa9f7

- Duration 1:17.6; 35 bars of 4 beats; tempo ≈ 107.1 BPM (beat-interval CV 0.28%); pulse clarity 0.992 (beat_this final0 + madmom DBN).
- Key estimate (from notes): C minor r=0.71, C major r=0.57; (from chroma): C# major r=0.86, F minor r=0.83
- Loudness: -18.0 LUFS integrated, LRA 4.2 LU, true peak 0.2 dBTP, crest 21.5 dB; per-bar RMS p10/p90 [-25.2, -18.7] dBFS.
- Source file: mp3 242 kbps 48000 Hz; bandwidth ≈ 20079 Hz; clipped samples 1.17e-06; side/mid -5.7 dB; quietest-5% frame level -42.1 dB.
- Brightness median 1233 Hz; onset rate 3.52/s.

## Stems

| stem | active bars | notes | range | median | mean conf | low-conf | vel med/sd | polyphony | med dur (beats) |
|---|---|---|---|---|---|---|---|---|---|
| bass | 0% | 0 (silent) | | | | | | | |
| other | 80% | 65 | F#2-E6 | C4 | 0.35 | 54% | 125/10.1 | 1.05 | 0.39 |
| vocals | 0% | 0 (silent) | | | | | | | |
| guitar | 86% | 134 | A2-Ab5 | C4 | 0.37 | 49% | 121/12.6 | 1.12 | 0.34 |
| piano | 11% | 8 | Ab3-C4 | Bb3 | 0.36 | 38% | 127/1.3 | 1.16 | 0.4 |
| drums | 63% | hits {'kick': 332, 'snare': 215, 'hat': 275} | | | | | | | |

Stem level (90th pct RMS dBFS): drums -21.6, bass -79.1, other -27.8, vocals -82.0, guitar -24.5, piano -40.1

## Sections

| section | bars | time | energy | dB | stems | chords |
|---|---|---|---|---|---|---|
| A1 | 1–8 | 0:00.0–0:18.0 | high | -22.0 | DOG | N(2) N > C# C#(4) N |
| B1 | 9–16 | 0:18.0–0:35.9 | high | -19.7 | DOG | N(2) N > C# C#(5) |
| A2 | 17–20 | 0:35.9–0:44.9 | mid | -23.4 | DOG | N(4) |
| C1 | 21–24 | 0:44.9–0:53.9 | mid | -22.4 | OG | C# N(3) |
| D1 | 25–33 | 0:53.9–1:14.1 | mid | -23.1 | DOG | N(5) Eb Eb > Bb Bb(2) |
| E1 | 34–35 | 1:14.1–1:17.6 | low | -57.4 |  | N(2) |

## Harmony

- Chord changes per bar 0.43; distinct chords 4; same chord 4 bars later 0.26, 8 bars later 0.59.
- Most common (madmom): [('N', 21), ('C#', 12), ('Bb', 3), ('Eb', 2)]
- Common 4-bar progressions: [['N | N | N | N', 3], ['N | N | N > C# | C#', 2], ['N > C# | C# | C# | C#', 2], ['C# | N | N | N', 2]]
- Chord qualities fitted from notes: [('5', 20), ('aug', 4), ('maj7', 3), ('sus2', 2), ('7', 1), ('add9', 1), ('m', 1), ('maj', 1)] (unknown 0.06)

## Melody (skyline of non-bass stems)

- 135 skyline notes, range A2-C6 (p10–p90 C3-C5), stepwise 39%, leaps ≥4th 48%, mean |interval| 6.63 st.
- Skyline comes from: {'guitar': 92, 'other': 38, 'piano': 5}; melody present in 33/35 bars.
- Recurring 4-note interval motifs: [11, 0, 0] ×3 (bars [3, 5, 7]); [0, 0, 12] ×3 (bars [3, 7, 20]); [0, 12, -12] ×3 (bars [7, 20, 22])

## Microtiming & groove

Deviations are measured against a locally smoothed beat grid divided into 4 steps per beat (16th notes).
- drums: n=470, mean offset 3.7 ms, mean |dev| 10.9 ms, sd 19.4 ms, 77% within 10 ms of the grid, 88% within 15% of a grid step
- other: n=65, mean offset -1.5 ms, mean |dev| 31.6 ms, sd 37.3 ms, 20% within 10 ms of the grid, 34% within 15% of a grid step
- guitar: n=133, mean offset 1.8 ms, mean |dev| 31.8 ms, sd 39.7 ms, 26% within 10 ms of the grid, 44% within 15% of a grid step
- Subdivision: 6% of informative off-beat onsets sit nearer a triplet grid than a 16th grid (~30% if onsets were placed at random; well under that = straight 16ths, >60% = triplet/compound feel)
- 8th swing: off-beat at 0.508 of the beat (ratio 1.03; 1.0 straight, 2.0 triplet)
- 16th swing: ratio 1.14
- Tempo: IBI CV 0.28%, drift -0.2 BPM/min, local BPM p5–p95 [106.7, 107.1]
- Drum hit strength sd 0.281; hits by beat [count, mean strength]: {'kick': {'1': [33, 0.48], '2': [23, 0.34], '3': [20, 0.37], '4': [31, 0.27]}, 'snare': {'1': [20, 0.65], '2': [16, 0.92], '3': [9, 0.55], '4': [16, 0.84]}, 'hat': {'1': [18, 0.79], '2': [20, 0.87], '3': [20, 0.77], '4': [20, 0.84]}}

## Files

- `sections.md`, `chords.md`, `bars.md`/`bars.csv`, `score.md` (per-bar multi-stem view), `notes/*.txt`, `midi/*.mid`, `beats.csv`, `features.json`, `stems/*.mp3`, `mel.png`, `chroma.png`, `energy.png`, `clap_tags.md`
