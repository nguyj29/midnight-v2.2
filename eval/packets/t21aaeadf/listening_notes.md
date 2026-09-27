# Listening notes — t21aaeadf

> Disclosure: I accidentally saw this track's label (one line of labels.csv) before writing these notes. I've tried to write from the packet alone, but treat this note as possibly coloured by it.

**What it is.** A 2:50, mid-tempo (~96 BPM, very steady, 4/4) minor-key instrumental built around a **bass riff**. The bass is the loudest stem by far (about −15 dBFS against drums at about −31), with guitar carrying a simple lead line and piano in the intro and some middle passages. Drums are present but low in the mix: steady 8th-note hats and a light snare, with almost no kick. It reads as a laid-back, riff-driven groove piece (chill/lo-fi-leaning band sound), not an electronic production.

**How it develops.**
- 0:00–0:20 (A1): a hazy, noisy intro. The spectrogram shows broadband texture with a pulsing low-level bed (possibly vinyl/room noise or a filtered loop) under a few piano chords (Cm, Eb6 colour).
- 0:20–0:40 (A2): solo piano, clearer and brighter, circling Eb5/D5/C5 over Cm. This quietly previews the main melody.
- 0:40–1:15 (B1/C1/B2): the band enters and the level jumps ~7 dB. The bass riff is root–octave–fifth with a pickup (C2 … C3 held on the "and" of 2 … F2–G2 into the next bar), cycling Cm | Gm | Bbm→Bb | Fm→F in two-bar blocks. The guitar hangs on Eb5 with D5/G5/Bb5 neighbours; a C–Eb–C–Eb figure recurs (bars 20–21, 40, 47–48).
- 1:15–2:00 (D1): the drums drop out (drum stem to about −45 dB) and bass and guitar carry a longer, more wandering harmonic passage: Fm F Cm Gm Bbm Ebm Fm Ab Gm Db Fm Bb A. A development section with more chromatic colour, then a small dip in level around 1:50.
- 2:00–2:40 (B3/E1/B4): the main riff returns, with a Bbm→Bb, Fm→F variant block and brighter guitar and piano fills.
- 2:40–2:50 (A3): fade-out to silence.

**What's striking.** The minor-to-major shifts inside the loop (Bbm→Bb, Fm→F) give it a bittersweet lift each cycle, though some of this may be the chord tracker guessing on thirdless voicings (the note-fitted chords often come out as power chords, F5/G5). The arrangement is well paced: noise intro → solo piano → full band → drumless development → return → fade. That's a proper A–B–A shape, and the wide dynamics (per-bar level spans 17 dB, LRA 10 LU) support it. The tempo is very steady (beat-interval CV 0.5%, drift −0.1 BPM/min: a click or a tight band), but dynamics vary a lot from note to note (bass velocity sd 26), which fits played rather than programmed parts.

**What's weak or questionable.** The melodic material is thin. The guitar line mostly sustains one note (Eb5) with small neighbours, and the skyline motifs are 2–3-note alternations. The main riff repeats a lot, and much of the interest rests on groove and texture. The noisy intro may be atmosphere or may read as murky. Drums are so low that the groove depends on the bass.

**What I can't tell from the packet.** The guitar's tone (clean, chorus, overdriven?) and whether the noise bed is deliberate lo-fi texture. Whether the Bbm/Fm chords are real minor chords or artefacts of power-chord voicings. Transcription confidence is decent (10–15% low-confidence notes per stem), but stem assignment is the bigger doubt: which instrument plays the lead is uncertain.

**Packet reliability.** Beat grid solid (CV 2%, pulse clarity 0.80). The drum-grid rows in the quiet intro/outro are full of hits: that's the noise bed triggering the band detectors, not real drumming. The vocals stem is silent: instrumental.

**Style tags (CLAP, weak evidence), and a correction.** CLAP stands out strongly for saxophone (z=+2.7), jazz / jazz fusion / gospel / blues, acoustic drum kit, dry close-miked and live band recording, playful–romantic–nostalgic. This changes my reading: the sustained lead I attributed to 'guitar' (hanging on Eb5 with neighbours) is plausibly a **saxophone** that Demucs put in the guitar stem (this rests on CLAP's instrument tags; the transcription itself can't tell sax from guitar). So this is better read as a small live jazz/soul-jazz band groove (bass-led, soft kit, sax lead, piano) than a chill-hop production. The mood reads warm and nostalgic rather than dark.

**In plain words.** A relaxed, warm, late-night groove, probably a small live band: a rolling bass line up front, soft drums, piano, and a lead (likely saxophone) that mostly holds long notes. It starts hazy and quiet, adds piano, then the band comes in; a drumless middle stretch wanders a bit before the main groove returns and it fades out. It has a pleasant bittersweet lift each time round. The groove carries it more than any strong melody, so it can feel samey.

**Revision (packet v4).** Numbers above were corrected after a pipeline bug fix (transcription confidence and tempo were mis-measured in the first packet version); the musical reading was re-checked against the rebuilt packet.
