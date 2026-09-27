# Packet summary — td5b1c789

- Duration 1:29.5; 42 bars of 4 beats; tempo ≈ 112.0 BPM (beat-interval CV 0.27%); pulse clarity 0.994 (beat_this final0 + madmom DBN).
- Key estimate (from notes): A minor r=0.77, E minor r=0.73; (from chroma): C major r=0.79, A minor r=0.78
- Loudness: -10.5 LUFS integrated, LRA 3.0 LU, true peak -0.0 dBTP, crest 13.4 dB; per-bar RMS p10/p90 [-14.7, -12.5] dBFS.
- Source file: mp3 260 kbps 48000 Hz; bandwidth ≈ 20058 Hz; clipped samples 0.00e+00; side/mid -7.8 dB; quietest-5% frame level -21.9 dB.
- Brightness median 1650 Hz; onset rate 3.84/s.

## Stems

| stem | active bars | notes | range | median | mean conf | low-conf | vel med/sd | polyphony | med dur (beats) |
|---|---|---|---|---|---|---|---|---|---|
| bass | 79% | 437 | D1-E4 | G2 | 0.58 | 4% | 123/16.9 | 1.61 | 0.39 |
| other | 98% | 599 | A2-B6 | A4 | 0.53 | 5% | 118/17.1 | 2.0 | 0.37 |
| vocals | 14% | 38 | C4-Ab6 | E5 | 0.54 | 0% | 127/15.3 | 1.26 | 0.32 |
| guitar | 40% | 287 | C3-G6 | C4 | 0.56 | 5% | 122/18.6 | 2.28 | 0.46 |
| piano | 67% | 534 | D2-B6 | D4 | 0.58 | 1% | 122/14.1 | 2.21 | 0.35 |
| drums | 100% | hits {'kick': 699, 'snare': 549, 'hat': 718} | | | | | | | |

Stem level (90th pct RMS dBFS): drums -14.5, bass -18.0, other -16.6, vocals -40.2, guitar -24.4, piano -19.2

## Sections

| section | bars | time | energy | dB | stems | chords |
|---|---|---|---|---|---|---|
| A1 | 1–4 | 0:00.1–0:08.6 | high | -14.0 | DOP | F(2) G A |
| B1 | 5–12 | 0:08.6–0:25.7 | high | -12.4 | DBO | loop[Dm Dm > C Em] x2.0 |
| C1 | 13–23 | 0:25.7–0:49.3 | high | -13.1 | DBOP | F(2) C(2) F(2) C(2) Dm F Fm |
| D1 | 24–28 | 0:49.3–1:00.0 | high | -13.5 | DBOGP | Em A F Fm N |
| E1 | 29–36 | 1:00.0–1:17.2 | high | -13.3 | DBOG | Am Am > G G(2) F F > G G(2) |
| A2 | 37–40 | 1:17.2–1:25.7 | high | -15.0 | DOP | F(2) G A |
| F1 | 41–42 | 1:25.7–1:29.5 | low | -30.1 | DBO | Dm(2) |

## Harmony

- Chord changes per bar 0.81; distinct chords 9; same chord 4 bars later 0.39, 8 bars later 0.09.
- Most common (madmom): [('F', 12), ('G', 8), ('Dm', 7), ('C', 6), ('Em', 5), ('A', 3), ('Fm', 2), ('Am', 2)]
- Common 4-bar progressions: [['F | F | G | A', 2], ['Dm | Dm > C | Em | Em', 2], ['F | F | C | C', 2], ['G | A | Dm | Dm > C', 1]]
- Chord qualities fitted from notes: [('6', 7), ('m7', 6), ('m', 6), ('maj7', 5), ('m9', 4), ('add9', 3), ('sus4', 3), ('sus2', 2), ('5', 2), ('m7b5', 1)] (unknown 0.0)

## Melody (skyline of non-bass stems)

- 590 skyline notes, range A2-B6 (p10–p90 C4-B5), stepwise 37%, leaps ≥4th 44%, mean |interval| 6.17 st.
- Skyline comes from: {'other': 342, 'piano': 147, 'guitar': 84, 'vocals': 17}; melody present in 43/42 bars.
- Recurring 4-note interval motifs: [3, -3, 3] ×5 (bars [1, 3, 22, 37]); [0, 2, 0] ×5 (bars [2, 8, 10, 25, 38]); [-3, 3, -3] ×4 (bars [1, 37]); [-2, 0, 2] ×4 (bars [2, 8, 10, 38]); [0, -1, 0] ×4 (bars [8, 12, 23, 39]); [0, 0, -2] ×4 (bars [8, 10, 12, 23])

## Microtiming & groove

Deviations are measured against a locally smoothed beat grid divided into 4 steps per beat (16th notes).
- drums: n=1071, mean offset 1.8 ms, mean |dev| 20.0 ms, sd 30.0 ms, 56% within 10 ms of the grid, 66% within 15% of a grid step
- bass: n=437, mean offset -1.3 ms, mean |dev| 15.3 ms, sd 21.2 ms, 51% within 10 ms of the grid, 73% within 15% of a grid step
- other: n=598, mean offset 1.8 ms, mean |dev| 22.9 ms, sd 29.8 ms, 34% within 10 ms of the grid, 55% within 15% of a grid step
- vocals: n=38, mean offset 3.2 ms, mean |dev| 37.2 ms, sd 43.1 ms, 21% within 10 ms of the grid, 37% within 15% of a grid step
- guitar: n=287, mean offset 7.0 ms, mean |dev| 19.4 ms, sd 24.5 ms, 40% within 10 ms of the grid, 63% within 15% of a grid step
- piano: n=534, mean offset 8.1 ms, mean |dev| 15.1 ms, sd 18.5 ms, 45% within 10 ms of the grid, 76% within 15% of a grid step
- Subdivision: 16% of informative off-beat onsets sit nearer a triplet grid than a 16th grid (~30% if onsets were placed at random; well under that = straight 16ths, >60% = triplet/compound feel)
- 8th swing: off-beat at 0.508 of the beat (ratio 1.03; 1.0 straight, 2.0 triplet)
- 16th swing: ratio 1.03
- Tempo: IBI CV 0.27%, drift -0.0 BPM/min, local BPM p5–p95 [111.6, 112.5]
- Drum hit strength sd 0.24; hits by beat [count, mean strength]: {'kick': {'1': [38, 0.67], '2': [32, 0.86], '3': [31, 0.76], '4': [37, 0.64]}, 'snare': {'1': [61, 0.42], '2': [44, 0.81], '3': [42, 0.72], '4': [47, 0.73]}, 'hat': {'1': [61, 0.33], '2': [60, 0.47], '3': [53, 0.35], '4': [60, 0.46]}}

## Files

- `sections.md`, `chords.md`, `bars.md`/`bars.csv`, `score.md` (per-bar multi-stem view), `notes/*.txt`, `midi/*.mid`, `beats.csv`, `features.json`, `stems/*.mp3`, `mel.png`, `chroma.png`, `energy.png`, `clap_tags.md`
