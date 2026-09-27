# Packet summary — t052c16ae

- Duration 3:31.2; 84 bars of 4 beats; tempo ≈ 95.1 BPM (beat-interval CV 0.24%); pulse clarity 0.994 (beat_this final0 + madmom DBN).
- Key estimate (from notes): G minor r=0.91, Bb major r=0.74; (from chroma): G minor r=0.93, Bb major r=0.78
- Loudness: -9.2 LUFS integrated, LRA 3.5 LU, true peak 0.6 dBTP, crest 11.7 dB; per-bar RMS p10/p90 [-19.7, -9.9] dBFS.
- Source file: mp3 290 kbps 48000 Hz; bandwidth ≈ 20047 Hz; clipped samples 6.89e-05; side/mid -9.2 dB; quietest-5% frame level -27.4 dB.
- Brightness median 1457 Hz; onset rate 4.61/s.

## Stems

| stem | active bars | notes | range | median | mean conf | low-conf | vel med/sd | polyphony | med dur (beats) |
|---|---|---|---|---|---|---|---|---|---|
| bass | 88% | 875 | C1-C4 | D2 | 0.55 | 4% | 120/11.2 | 1.43 | 0.31 |
| other | 100% | 3023 | F1-G6 | G4 | 0.53 | 4% | 115/15.9 | 4.12 | 0.35 |
| vocals | 12% | 296 | G3-E7 | D4 | 0.54 | 4% | 127/12.1 | 1.2 | 0.26 |
| guitar | 2% | 0 (silent) | | | | | | | |
| piano | 2% | 0 (silent) | | | | | | | |
| drums | 79% | hits {'kick': 700, 'snare': 525, 'hat': 994} | | | | | | | |

Stem level (90th pct RMS dBFS): drums -11.2, bass -11.6, other -15.3, vocals -30.1, guitar -74.5, piano -67.6

## Sections

| section | bars | time | energy | dB | stems | chords |
|---|---|---|---|---|---|---|
| A1 | 1–8 | 0:00.1–0:20.3 | low | -25.9 | O | Gm Bb > Eb Gm > Ab Eb Gm(2) Bb F > Eb |
| B1 | 9–23 | 0:20.3–0:58.2 | high | -10.6 | DBO | loop[Gm Bb > C Bb Eb Dm] x2.4 |
| C1 | 24–27 | 0:58.2–1:08.3 | high | -12.2 | DBO | Bb > Gm Eb Dm Cm |
| B2 | 28–39 | 1:08.3–1:38.6 | high | -10.5 | DBO | loop[Gm Bb > C Gm Eb Dm] x2.0 |
| D1 | 40–52 | 1:38.6–2:11.5 | high | -11.5 | DBO | Cm C(2) Eb(2) C(2) Eb(2) C(2) Cm Eb |
| B3 | 53–69 | 2:11.5–2:54.4 | high | -10.2 | DBO | loop[Gm Eb Bb > F Eb Dm] x2.8 |
| D2 | 70–84 | 2:54.4–3:31.2 | high | -13.3 | DBO | Dm Cm C(2) Cm > Eb Eb C(2) Eb(2) C(2) Eb(3) |

## Harmony

- Chord changes per bar 0.93; distinct chords 8; same chord 4 bars later 0.26, 8 bars later 0.16.
- Most common (madmom): [('Eb', 29), ('Gm', 21), ('C', 17), ('Bb', 14), ('Dm', 8), ('Cm', 5), ('F', 4), ('Ab', 1)]
- Common 4-bar progressions: [['Gm | Eb | Bb > F | Eb', 3], ['Bb > F | Eb | Eb | Dm', 3], ['Eb | Dm | Gm | Gm', 2], ['Gm | Gm | Bb > C | Bb > Gm', 2]]
- Chord qualities fitted from notes: [('m7', 22), ('6', 12), ('maj7', 12), ('sus2', 9), ('maj9', 9), ('maj', 7), ('m9', 3), ('sus4', 3), ('5', 2), ('m', 2)] (unknown 0.01)

## Melody (skyline of non-bass stems)

- 1301 skyline notes, range F1-E7 (p10–p90 C4-A5), stepwise 26%, leaps ≥4th 55%, mean |interval| 6.8 st.
- Skyline comes from: {'other': 1187, 'vocals': 114}; melody present in 84/84 bars.
- Recurring 4-note interval motifs: [3, 0, 0] ×9 (bars [16, 39, 47, 51, 54, 59, 66, 76, 82]); [-3, 3, 0] ×9 (bars [17, 19, 33, 39, 47, 54, 58, 66, 70]); [0, -7, 7] ×8 (bars [25, 26, 35, 38, 54, 57, 63, 69]); [-3, 0, 3] ×7 (bars [10, 29, 41, 42, 43, 45, 72]); [0, -3, 3] ×7 (bars [16, 17, 20, 30, 40, 48, 67]); [-7, 7, 0] ×7 (bars [25, 35, 38, 55, 57, 63, 73])

## Microtiming & groove

Deviations are measured against a locally smoothed beat grid divided into 4 steps per beat (16th notes).
- drums: n=1696, mean offset -0.3 ms, mean |dev| 6.7 ms, sd 8.9 ms, 79% within 10 ms of the grid, 99% within 15% of a grid step
- bass: n=875, mean offset -2.2 ms, mean |dev| 26.7 ms, sd 33.4 ms, 24% within 10 ms of the grid, 54% within 15% of a grid step
- other: n=3020, mean offset -4.9 ms, mean |dev| 41.1 ms, sd 47.0 ms, 13% within 10 ms of the grid, 29% within 15% of a grid step
- vocals: n=296, mean offset -5.0 ms, mean |dev| 39.5 ms, sd 45.4 ms, 14% within 10 ms of the grid, 29% within 15% of a grid step
- Subdivision: 19% of informative off-beat onsets sit nearer a triplet grid than a 16th grid (~30% if onsets were placed at random; well under that = straight 16ths, >60% = triplet/compound feel)
- 8th swing: off-beat at 0.505 of the beat (ratio 1.02; 1.0 straight, 2.0 triplet)
- 16th swing: ratio 1.04
- Tempo: IBI CV 0.24%, drift 0.04 BPM/min, local BPM p5–p95 [94.7, 95.4]
- Drum hit strength sd 0.289; hits by beat [count, mean strength]: {'kick': {'1': [62, 0.91], '2': [61, 0.86], '3': [3, 0.56], '4': [94, 0.32]}, 'snare': {'1': [67, 0.79], '2': [64, 0.9], '3': [10, 0.36], '4': [65, 0.86]}, 'hat': {'1': [66, 0.8], '2': [62, 0.89], '3': [64, 0.77], '4': [63, 0.84]}}

## Files

- `sections.md`, `chords.md`, `bars.md`/`bars.csv`, `score.md` (per-bar multi-stem view), `notes/*.txt`, `midi/*.mid`, `beats.csv`, `features.json`, `stems/*.mp3`, `mel.png`, `chroma.png`, `energy.png`, `clap_tags.md`
