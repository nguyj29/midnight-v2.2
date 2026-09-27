# Packet summary — tde35730e

- Duration 2:06.9; 60 bars of 3 beats; tempo ≈ 70.1 BPM (beat-interval CV 28.63%); pulse clarity 0.975 (beat_this final0 + madmom DBN).
- Key estimate (from notes): E minor r=0.86, G major r=0.68; (from chroma): E minor r=0.89, G major r=0.74
- Loudness: -14.1 LUFS integrated, LRA 11.2 LU, true peak 0.5 dBTP, crest 20.1 dB; per-bar RMS p10/p90 [-33.2, -16.3] dBFS.
- Source file: mp3 258 kbps 48000 Hz; bandwidth ≈ 20058 Hz; clipped samples 1.73e-05; side/mid -0.4 dB; quietest-5% frame level -41.3 dB.
- Brightness median 1321 Hz; onset rate 1.66/s.

## Stems

| stem | active bars | notes | range | median | mean conf | low-conf | vel med/sd | polyphony | med dur (beats) |
|---|---|---|---|---|---|---|---|---|---|
| bass | 0% | 0 (silent) | | | | | | | |
| other | 97% | 1022 | C1-B7 | F#4 | 0.53 | 10% | 113/20.3 | 2.44 | 0.22 |
| vocals | 0% | 24 | C4-F#6 | Ab5 | 0.45 | 8% | 127/3.8 | 1.22 | 0.19 |
| guitar | 22% | 264 | D2-G6 | E3 | 0.46 | 14% | 115/16.4 | 2.54 | 0.26 |
| piano | 32% | 320 | E1-E6 | Ab3 | 0.46 | 20% | 112/23.3 | 2.34 | 0.24 |
| drums | 42% | hits {'kick': 328, 'snare': 573, 'hat': 556} | | | | | | | |

Stem level (90th pct RMS dBFS): drums -20.5, bass -73.8, other -21.1, vocals -55.0, guitar -30.4, piano -28.6

## Sections

| section | bars | time | energy | dB | stems | chords |
|---|---|---|---|---|---|---|
| A1 | 0–10 | 0:00.0–0:13.8 | low | -30.9 | O | N(11) |
| B1 | 11–16 | 0:13.8–0:21.5 | low | -29.7 | O | C(3) B(2) B > E |
| B2 | 17–20 | 0:21.5–0:27.5 | low | -34.1 | O | E(3) N |
| C1 | 21–37 | 0:27.5–1:11.2 | mid | -20.4 | OP | loop[E > Em A Em C > B Em Em > C C > D D > C] x2.1 |
| D1 | 38–55 | 1:11.2–1:57.5 | high | -17.5 | DOG | loop[D C A Em] x4.2 |
| A2 | 56–59 | 1:57.5–2:06.9 | low | -54.3 |  | E E > N N(2) |

## Harmony

- Chord changes per bar 0.9; distinct chords 8; same chord 4 bars later 0.34, 8 bars later 0.35.
- Most common (madmom): [('N', 15), ('C', 14), ('Em', 12), ('E', 9), ('D', 9), ('B', 5), ('A', 5), ('F', 3)]
- Common 4-bar progressions: [['N | N | N | N', 4], ['D | C | A | Em', 3], ['A | Em | D | C', 3], ['A | Em | C > B | Em', 2]]
- Chord qualities fitted from notes: [('5', 16), ('add9', 10), ('maj', 5), ('sus4', 5), ('m', 4), ('m7', 3), ('maj7', 3), ('6', 3), ('m6', 2), ('maj9', 2)] (unknown 0.03)

## Melody (skyline of non-bass stems)

- 556 skyline notes, range C1-B7 (p10–p90 B3-F#6), stepwise 32%, leaps ≥4th 58%, mean |interval| 7.57 st.
- Skyline comes from: {'other': 450, 'piano': 64, 'guitar': 25, 'vocals': 17}; melody present in 58/60 bars.
- Recurring 4-note interval motifs: [2, 0, 0] ×4 (bars [17, 33, 52]); [0, 2, 0] ×4 (bars [22, 33, 52]); [0, 3, 0] ×3 (bars [21, 40, 44]); [-2, 0, 2] ×3 (bars [22, 35, 52]); [12, -7, 7] ×3 (bars [26, 33, 34]); [0, -12, 12] ×3 (bars [28, 33, 41])

## Microtiming & groove

Deviations are measured against a locally smoothed beat grid divided into 4 steps per beat (16th notes).
- drums: n=1363, mean offset 4.7 ms, mean |dev| 50.6 ms, sd 60.7 ms, 12% within 10 ms of the grid, 38% within 15% of a grid step
- other: n=1022, mean offset 0.7 ms, mean |dev| 49.9 ms, sd 59.3 ms, 13% within 10 ms of the grid, 33% within 15% of a grid step
- vocals: n=24, mean offset -16.4 ms, mean |dev| 67.8 ms, sd 71.6 ms, 0% within 10 ms of the grid, 12% within 15% of a grid step
- guitar: n=264, mean offset 8.0 ms, mean |dev| 51.7 ms, sd 59.4 ms, 9% within 10 ms of the grid, 33% within 15% of a grid step
- piano: n=320, mean offset 4.8 ms, mean |dev| 49.0 ms, sd 58.4 ms, 13% within 10 ms of the grid, 38% within 15% of a grid step
- Subdivision: 30% of informative off-beat onsets sit nearer a triplet grid than a 16th grid (~30% if onsets were placed at random; well under that = straight 16ths, >60% = triplet/compound feel)
- 8th swing: off-beat at 0.561 of the beat (ratio 1.28; 1.0 straight, 2.0 triplet)
- 16th swing: ratio 1.23
- Tempo: IBI CV 28.63%, drift -42.08 BPM/min, local BPM p5–p95 [69.8, 140.6]
- Drum hit strength sd 0.195; hits by beat [count, mean strength]: {'kick': {'1': [41, 0.56], '2': [45, 0.45], '3': [9, 0.78]}, 'snare': {'1': [58, 0.79], '2': [67, 0.7], '3': [41, 0.71]}, 'hat': {'1': [55, 0.67], '2': [55, 0.62], '3': [64, 0.58]}}

## Files

- `sections.md`, `chords.md`, `bars.md`/`bars.csv`, `score.md` (per-bar multi-stem view), `notes/*.txt`, `midi/*.mid`, `beats.csv`, `features.json`, `stems/*.mp3`, `mel.png`, `chroma.png`, `energy.png`, `clap_tags.md`
