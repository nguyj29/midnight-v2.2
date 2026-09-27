# CLAP zero-shot tags — td83c7b30

Model `laion/larger_clap_music_and_speech`, track embedding = mean of 10s windows. 'Top' = highest raw text-audio similarity; 'stands out' = highest z-score relative to the other tracks in this collection. Weak, style-level evidence only: CLAP often confuses neighbouring genres.

- **style** top: synthwave (0.61), video game soundtrack (0.58), anime soundtrack (0.51), techno (0.47), chiptune (0.46), glitchy IDM electronica (0.46)
  - stands out: chiptune (z=+2.2), video game soundtrack (z=+2.1), synthwave (z=+1.9), glitchy IDM electronica (z=+1.8), anime soundtrack (z=+1.7)
- **instrument** top: organ (0.53), lead synthesizer (0.51), synth bass (0.48), drum machine (0.46), arpeggiator (0.46), synthesizer pads (0.45)
  - stands out: lead synthesizer (z=+1.6), organ (z=+1.4), synth bass (z=+1.1), drum machine (z=+0.9), synthesizer pads (z=+0.9)
- **mood** top: nostalgic (0.43), uplifting (0.43), hypnotic (0.42), dark (0.41), energetic (0.40), aggressive (0.40)
  - stands out: aggressive (z=+1.3), energetic (z=+1.0), epic (z=+0.8), dark (z=+0.7), triumphant (z=+0.5)
- **production** top: vintage analog sound (0.46), polished modern production (0.41), dense layered arrangement (0.41), heavily compressed (0.30), distorted and noisy (0.28), minimal sparse arrangement (0.27)
  - stands out: distorted and noisy (z=+1.5), vintage analog sound (z=+1.4), polished modern production (z=+1.1), dense layered arrangement (z=+0.8), heavily compressed (z=+0.6)
