# CLAP zero-shot tags — t9fb064e8

Model `laion/larger_clap_music_and_speech`, track embedding = mean of 10s windows. 'Top' = highest raw text-audio similarity; 'stands out' = highest z-score relative to the other tracks in this collection. Weak, style-level evidence only: CLAP often confuses neighbouring genres.

- **style** top: electronic dance music (0.44), techno (0.32), synthwave (0.31), house music (0.31), anime soundtrack (0.30), glitchy IDM electronica (0.29)
  - stands out: electronic dance music (z=+0.9), breakcore (z=+0.6), techno (z=-0.4), boom bap hip hop (z=-0.4), glitchy IDM electronica (z=-0.5)
- **instrument** top: drum machine (0.40), vocal chops (0.38), lead synthesizer (0.37), synth bass (0.31), sampled breakbeat (0.29), arpeggiator (0.29)
  - stands out: drum machine (z=+0.2), sampled breakbeat (z=+0.1), lead synthesizer (z=-0.2), vocal chops (z=-0.8), acoustic drum kit (z=-0.9)
- **mood** top: energetic (0.39), uplifting (0.28), triumphant (0.18), aggressive (0.17), hypnotic (0.16), happy (0.09)
  - stands out: energetic (z=+0.9), aggressive (z=-1.0), triumphant (z=-1.1), uplifting (z=-1.3), happy (z=-1.6)
- **production** top: polished modern production (0.25), vintage analog sound (0.23), heavily compressed (0.18), lo-fi recording (0.15), dense layered arrangement (0.13), home demo quality (0.10)
  - stands out: heavily compressed (z=-0.8), polished modern production (z=-1.1), home demo quality (z=-1.3), distorted and noisy (z=-1.6), lo-fi recording (z=-1.9)
