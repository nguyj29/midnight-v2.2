# CLAP zero-shot tags — td816798a

Model `laion/larger_clap_music_and_speech`, track embedding = mean of 10s windows. 'Top' = highest raw text-audio similarity; 'stands out' = highest z-score relative to the other tracks in this collection. Weak, style-level evidence only: CLAP often confuses neighbouring genres.

- **style** top: synthwave (0.57), electronic dance music (0.53), house music (0.47), trap beat (0.46), techno (0.46), video game soundtrack (0.45)
  - stands out: electronic dance music (z=+2.0), future bass (z=+1.9), dubstep (z=+1.8), glitchy IDM electronica (z=+1.5), synthwave (z=+1.5)
- **instrument** top: lead synthesizer (0.55), synth bass (0.53), 808 bass (0.53), synthesizer pads (0.50), drum machine (0.49), vocal chops (0.48)
  - stands out: lead synthesizer (z=+2.1), 808 bass (z=+1.9), synth bass (z=+1.7), synthesizer pads (z=+1.4), drum machine (z=+1.2)
- **mood** top: hypnotic (0.43), uplifting (0.41), dark (0.38), nostalgic (0.37), energetic (0.33), sad (0.31)
  - stands out: hypnotic (z=+0.5), energetic (z=+0.4), dark (z=+0.3), aggressive (z=+0.3), uplifting (z=+0.1)
- **production** top: vintage analog sound (0.51), polished modern production (0.40), lo-fi recording (0.38), dense layered arrangement (0.37), minimal sparse arrangement (0.32), heavily compressed (0.30)
  - stands out: vintage analog sound (z=+2.0), distorted and noisy (z=+1.3), polished modern production (z=+1.1), lo-fi recording (z=+0.9), heavily compressed (z=+0.6)
