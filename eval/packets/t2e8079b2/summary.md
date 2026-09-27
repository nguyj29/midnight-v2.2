# Packet summary — t2e8079b2

- Duration 1:00.0; 26 bars of 4 beats; tempo ≈ 105.9 BPM (beat-interval CV 0.56%); pulse clarity 0.925 (beat_this final0 + madmom DBN).
- Key estimate (from notes): C major r=0.85, A minor r=0.77; (from chroma): C major r=0.97, A minor r=0.78
- Loudness: -23.6 LUFS integrated, LRA 8.3 LU, true peak -8.2 dBTP, crest 19.5 dB; per-bar RMS p10/p90 [-37.6, -25.5] dBFS.
- Source file: mp3 215 kbps 48000 Hz; bandwidth ≈ 20025 Hz; clipped samples 0.00e+00; side/mid -8.4 dB; quietest-5% frame level -51.9 dB.
- Brightness median 734 Hz; onset rate 2.22/s.

## Stems

| stem | active bars | notes | range | median | mean conf | low-conf | vel med/sd | polyphony | med dur (beats) |
|---|---|---|---|---|---|---|---|---|---|
| bass | 0% | 0 (silent) | | | | | | | |
| other | 100% | 361 | C3-B6 | G4 | 0.42 | 33% | 113/20.7 | 2.39 | 0.41 |
| vocals | 0% | 0 (silent) | | | | | | | |
| guitar | 0% | 0 (silent) | | | | | | | |
| piano | 0% | 0 (silent) | | | | | | | |
| drums | 0% | hits {} | | | | | | | |

Stem level (90th pct RMS dBFS): drums -95.9, bass -93.4, other -23.7, vocals -88.1, guitar -96.5, piano -91.0

## Sections

| section | bars | time | energy | dB | stems | chords |
|---|---|---|---|---|---|---|
| A1 | 1–24 | 0:00.0–0:54.3 | high | -28.7 | O | loop[F C F N C] x3.0 |
| B1 | 25–26 | 0:54.3–0:58.9 | low | -41.2 | O | F N |

## Harmony

- Chord changes per bar 0.65; distinct chords 3; same chord 4 bars later 0.64, 8 bars later 0.78.
- Most common (madmom): [('C', 15), ('F', 9), ('N', 3)]
- Common 4-bar progressions: [['F | C | C | C', 3], ['C | C | F | N', 3], ['F | N | C | C', 2], ['C | C | F | C', 1]]
- Chord qualities fitted from notes: [('m', 7), ('maj', 4), ('maj7', 4), ('maj9', 3), ('5', 3), ('sus2', 2), ('m7', 2), ('sus4', 1)] (unknown 0.0)

## Melody (skyline of non-bass stems)

- 184 skyline notes, range C3-B6 (p10–p90 A3-G5), stepwise 45%, leaps ≥4th 43%, mean |interval| 6.01 st.
- Skyline comes from: {'other': 184}; melody present in 27/26 bars.
- Recurring 4-note interval motifs: [-2, 0, -1] ×4 (bars [5, 11, 13, 23]); [0, 1, 0] ×3 (bars [2, 15, 22]); [1, 0, -1] ×3 (bars [2, 10, 22]); [0, -1, 1] ×3 (bars [6, 22, 24])

## Microtiming & groove

Deviations are measured against a locally smoothed beat grid divided into 4 steps per beat (16th notes).
- other: n=361, mean offset 3.4 ms, mean |dev| 30.3 ms, sd 37.5 ms, 28% within 10 ms of the grid, 44% within 15% of a grid step
- Subdivision: 17% of informative off-beat onsets sit nearer a triplet grid than a 16th grid (~30% if onsets were placed at random; well under that = straight 16ths, >60% = triplet/compound feel)
- 8th swing: off-beat at 0.55 of the beat (ratio 1.22; 1.0 straight, 2.0 triplet)
- 16th swing: ratio 0.99
- Tempo: IBI CV 0.56%, drift -0.33 BPM/min, local BPM p5–p95 [104.9, 107.1]

## Files

- `sections.md`, `chords.md`, `bars.md`/`bars.csv`, `score.md` (per-bar multi-stem view), `notes/*.txt`, `midi/*.mid`, `beats.csv`, `features.json`, `stems/*.mp3`, `mel.png`, `chroma.png`, `energy.png`, `clap_tags.md`
