# CLAP zero-shot tags — te0e7d7c7

Model `laion/larger_clap_music_and_speech`, track embedding = mean of 10s windows. 'Top' = highest raw text-audio similarity; 'stands out' = highest z-score relative to the other tracks in this collection. Weak, style-level evidence only: CLAP often confuses neighbouring genres.

- **style** top: synthwave (0.56), anime soundtrack (0.54), techno (0.50), math rock (0.49), video game soundtrack (0.49), UK garage (0.48)
  - stands out: breakcore (z=+2.1), anime soundtrack (z=+2.0), math rock (z=+1.8), techno (z=+1.8), drum and bass (z=+1.6)
- **instrument** top: lead synthesizer (0.55), synth bass (0.53), arpeggiator (0.52), drum machine (0.50), organ (0.46), vocal chops (0.45)
  - stands out: lead synthesizer (z=+2.0), synth bass (z=+1.7), drum machine (z=+1.3), arpeggiator (z=+1.2), distorted electric guitar (z=+1.0)
- **mood** top: energetic (0.56), triumphant (0.46), uplifting (0.46), aggressive (0.38), nostalgic (0.34), happy (0.33)
  - stands out: energetic (z=+2.4), triumphant (z=+1.1), aggressive (z=+1.1), uplifting (z=+0.5), epic (z=+0.5)
- **production** top: polished modern production (0.39), vintage analog sound (0.39), dense layered arrangement (0.31), home demo quality (0.31), heavily compressed (0.31), distorted and noisy (0.19)
  - stands out: polished modern production (z=+0.9), home demo quality (z=+0.9), heavily compressed (z=+0.7), vintage analog sound (z=+0.4), distorted and noisy (z=+0.4)
