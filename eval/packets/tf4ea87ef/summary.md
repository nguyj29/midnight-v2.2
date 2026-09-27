# Packet summary — tf4ea87ef

- Duration 1:39.4; 40 bars of 4 beats; tempo ≈ 96.8 BPM (beat-interval CV 0.24%); pulse clarity 0.94 (beat_this final0 + madmom DBN).
- Key estimate (from notes): F major r=0.85, A minor r=0.68; (from chroma): F major r=0.90, A minor r=0.73
- Loudness: -15.4 LUFS integrated, LRA 6.2 LU, true peak -0.5 dBTP, crest 18.2 dB; per-bar RMS p10/p90 [-22.4, -15.4] dBFS.
- Source file: mp3 212 kbps 48000 Hz; bandwidth ≈ 11154 Hz; clipped samples 0.00e+00; side/mid -6.7 dB; quietest-5% frame level -29.1 dB.
- Brightness median 544 Hz; onset rate 2.82/s.

## Stems

| stem | active bars | notes | range | median | mean conf | low-conf | vel med/sd | polyphony | med dur (beats) |
|---|---|---|---|---|---|---|---|---|---|
| bass | 12% | 25 | Bb1-F4 | C3 | 0.62 | 4% | 127/17.4 | 1.05 | 0.35 |
| other | 97% | 892 | Bb1-A5 | A3 | 0.5 | 8% | 121/16.3 | 2.28 | 0.3 |
| vocals | 0% | 0 (silent) | | | | | | | |
| guitar | 50% | 201 | E2-C5 | C4 | 0.57 | 8% | 126/19.2 | 2.19 | 0.62 |
| piano | 5% | 0 (silent) | | | | | | | |
| drums | 0% | hits {} | | | | | | | |

Stem level (90th pct RMS dBFS): drums -81.1, bass -38.1, other -20.9, vocals -76.5, guitar -17.5, piano -74.7

## Sections

| section | bars | time | energy | dB | stems | chords |
|---|---|---|---|---|---|---|
| A1 | 1–8 | 0:00.1–0:19.9 | mid | -21.6 | O | F(6) Dm Dm > F |
| B1 | 9–25 | 0:19.9–1:02.2 | high | -17.3 | OG | F(17) |
| C1 | 26–33 | 1:02.2–1:22.0 | high | -19.1 | BO | F(3) Bb F Dm(2) Bb |
| A2 | 34–38 | 1:22.0–1:34.5 | mid | -22.1 | O | F(5) |
| D1 | 39–40 | 1:34.5–1:39.4 | low | -40.4 |  | Dm Dm > N |

## Harmony

- Chord changes per bar 0.3; distinct chords 4; same chord 4 bars later 0.67, 8 bars later 0.75.
- Most common (madmom): [('F', 33), ('Dm', 6), ('Bb', 2), ('N', 1)]
- Common 4-bar progressions: [['F | F | F | F', 12], ['F | F | Dm | Dm > F', 1], ['Dm | Dm > F | F | F', 1], ['F | F | Bb | F', 1]]
- Chord qualities fitted from notes: [('maj', 13), ('aug', 11), ('5', 5), ('maj7', 3), ('m', 3), ('sus2', 2), ('add9', 1), ('6', 1), ('sus4', 1)] (unknown 0.0)

## Melody (skyline of non-bass stems)

- 597 skyline notes, range Bb1-A5 (p10–p90 F3-Eb5), stepwise 24%, leaps ≥4th 64%, mean |interval| 8.36 st.
- Skyline comes from: {'other': 486, 'guitar': 111}; melody present in 40/40 bars.
- Recurring 4-note interval motifs: [12, 0, -4] ×4 (bars [7, 10, 39]); [0, -1, -4] ×3 (bars [1, 5, 27]); [-12, -4, 0] ×3 (bars [2, 16, 37]); [12, 4, 0] ×3 (bars [6, 20, 36]); [5, 0, -5] ×3 (bars [6, 17, 21]); [0, 12, -12] ×3 (bars [8, 28, 38])

## Microtiming & groove

Deviations are measured against a locally smoothed beat grid divided into 4 steps per beat (16th notes).
- bass: n=25, mean offset 6.3 ms, mean |dev| 27.7 ms, sd 38.0 ms, 44% within 10 ms of the grid, 60% within 15% of a grid step
- other: n=892, mean offset 3.6 ms, mean |dev| 33.4 ms, sd 40.5 ms, 19% within 10 ms of the grid, 43% within 15% of a grid step
- guitar: n=201, mean offset -1.6 ms, mean |dev| 25.7 ms, sd 33.1 ms, 26% within 10 ms of the grid, 57% within 15% of a grid step
- Subdivision: 23% of informative off-beat onsets sit nearer a triplet grid than a 16th grid (~30% if onsets were placed at random; well under that = straight 16ths, >60% = triplet/compound feel)
- 8th swing: off-beat at 0.523 of the beat (ratio 1.1; 1.0 straight, 2.0 triplet)
- 16th swing: ratio 1.26
- Tempo: IBI CV 0.24%, drift -0.02 BPM/min, local BPM p5–p95 [96.1, 96.8]

## Files

- `sections.md`, `chords.md`, `bars.md`/`bars.csv`, `score.md` (per-bar multi-stem view), `notes/*.txt`, `midi/*.mid`, `beats.csv`, `features.json`, `stems/*.mp3`, `mel.png`, `chroma.png`, `energy.png`, `clap_tags.md`
