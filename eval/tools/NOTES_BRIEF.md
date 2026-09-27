# Brief: writing listening_notes.md for a track packet

You are reading a blind, instrumental music track through its analysis packet (you cannot hear audio). Write
`eval/packets/<id>/listening_notes.md` in the style of the finished examples:
`eval/packets/t0d513ac8/listening_notes.md`, `t21aaeadf`, `t3b9d70c1`, `t5fe4a915` (read at least two first).

## Hard rules (blind test)
- Do NOT read `labels.csv`, anything in `private/` or `tracks/`, `eval/crosscheck/`, or anything outside the project folder.
- Do NOT try to identify the song or artist (no web lookups, no fingerprinting). If the music itself makes you think
  you recognise it, add a line "**Recognition.** I think this may be ... (not used in any judgment)" and nothing more.
- Do not judge the track by comparison with other tracks' notes; describe this track on its own terms.
- Only write the one file `listening_notes.md` per assigned track. Do not modify anything else.

## What to read (in this order)
1. `packets/<id>/summary.md` (overview: tempo, key, loudness, stems, sections, harmony, melody, microtiming)
2. `packets/<id>/clap_tags.md` (zero-shot style tags; weak evidence, but very useful for instrument identity)
3. Images with the Read tool: `mel.png`, `energy.png` (and `chroma.png` if harmony matters)
4. `python3 eval/tools/skim.py <id> 2` — the first 2 bars of every section from `score.md`
5. Targeted look-ups in `score.md`, `bars.md`, `chords.md` for specific moments you want to check.
   Do NOT dump `notes/*.txt` or all of `score.md` for long tracks.

## Known packet quirks (don't misread these as music)
- Demucs 6-stem labels are guesses: a sax, synth lead or violin often lands in `guitar` or `other`; the `vocals`
  stem in these instrumentals is usually lead-instrument bleed. Use CLAP instrument tags + register/timbre clues.
- In quiet intros/outros the drum-grid rows can fill with hits from noise/reverb; the drums aren't really playing.
- madmom chords are major/minor/N only; thirdless (power-chord) voicings make major vs minor unreliable. The
  "from notes" chord column captures 7ths/9ths/sus but inherits transcription errors.
- Note confidence (packet v4+) is the geometric mean of Basic Pitch's frame and onset posteriors. A high
  low-confidence share (>25%) usually means distortion, dense mixes or breathy/noisy timbres: trust roots and form
  more than exact melody pitches. (Packets before v4 had a bug that made confidence decay with time — ignore any
  confidence numbers quoted in older notes.)
- Tempo can be off by 2x or 3/2; beats-per-bar 3 may be a misread 6/8/12/8. Stop-start or rubato sections break
  local BPM. Microtiming stats measure against the tracked grid; if the grid is doubtful, say so.
- Loudness/quality numbers (LUFS, true peak, clipping, bandwidth) describe mastering/source quality, not the music.
- A section's mean dB understates a fade (look at the per-bar levels in bars.md).
- A stem can show "active" by level from bleed while having 0 notes.
- madmom may call a whole arpeggiated passage one chord even when the bass moves: trust the bass + note-fitted chords.
- The melody "leaps" stat counts arpeggio octave jumps; the real tune may be in one stem (often piano/vocals/guitar).
- Section "energy" labels (packets rebuilt after this note) are dB below the track's loudest bars; older packets used
  within-track tertiles, so a section 0.3 dB quieter than its neighbours could read "low".
- In older packets, drum hits a few ms before a downbeat were labelled beat 5.00 of the previous 4/4 bar.
- Instrument identity: weigh CLAP's *stands out* instrument tags (z-scores) together with the spectrogram (clean,
  well-separated harmonic lines vs smeared noise), stereo width, crest factor and low-confidence %. Don't dismiss a
  strong standout tag without a concrete reason; say which reading the evidence favours and how sure you are.

## Required sections (use these bold headings)
**What it is.** style, instrumentation, tempo/meter/key, overall character (2–4 sentences)
**How it develops.** time-stamped walk through the sections: what enters/leaves, harmony, energy, melody
**What's striking.** musical strengths, with specific bars/times and numbers
**What's weak or questionable.** musical weaknesses, with specifics
**What I can't tell from the packet.** honest limits
**Packet reliability.** which parts of the packet are trustworthy for this track
**Style tags (CLAP, weak evidence).** what stands out and whether it agrees with your reading
**In plain words.** 3–5 sentences for a listener with no music-theory background, written like recalling the
experience of hearing it (how it feels, what it evokes, how it moves you or doesn't), not a timeline. No timestamps,
no jargon (no chord names, 'modal', 'dominant', BPM, etc.). Say what might grab or bore someone.

Write in plain, specific musical language (chord names, bar numbers, timestamps). About 350–550 words.
Report back: for each track, a 2-sentence summary and any packet problems you noticed.
