# CLAP zero-shot tags — t68bc6fa5

Model `laion/larger_clap_music_and_speech`, track embedding = mean of 10s windows. 'Top' = highest raw text-audio similarity; 'stands out' = highest z-score relative to the other tracks in this collection. Weak, style-level evidence only: CLAP often confuses neighbouring genres.

- **style** top: synthwave (0.62), techno (0.57), electronic dance music (0.55), video game soundtrack (0.54), anime soundtrack (0.50), dubstep (0.49)
  - stands out: techno (z=+2.7), dubstep (z=+2.5), electronic dance music (z=+2.2), glitchy IDM electronica (z=+2.1), synthwave (z=+2.0)
- **instrument** top: arpeggiator (0.56), synth bass (0.53), lead synthesizer (0.52), organ (0.51), drum machine (0.48), synthesizer pads (0.48)
  - stands out: arpeggiator (z=+1.7), lead synthesizer (z=+1.7), synth bass (z=+1.7), distorted electric guitar (z=+1.7), violin (z=+1.5)
- **mood** top: energetic (0.52), uplifting (0.49), triumphant (0.44), aggressive (0.42), epic (0.41), dark (0.41)
  - stands out: energetic (z=+2.0), aggressive (z=+1.5), epic (z=+1.4), triumphant (z=+1.0), uplifting (z=+0.9)
- **production** top: dense layered arrangement (0.48), polished modern production (0.44), vintage analog sound (0.40), heavily compressed (0.39), minimal sparse arrangement (0.29), distorted and noisy (0.27)
  - stands out: polished modern production (z=+1.6), dense layered arrangement (z=+1.6), heavily compressed (z=+1.6), distorted and noisy (z=+1.3), vintage analog sound (z=+0.5)
