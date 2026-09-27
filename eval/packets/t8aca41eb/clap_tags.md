# CLAP zero-shot tags — t8aca41eb

Model `laion/larger_clap_music_and_speech`, track embedding = mean of 10s windows. 'Top' = highest raw text-audio similarity; 'stands out' = highest z-score relative to the other tracks in this collection. Weak, style-level evidence only: CLAP often confuses neighbouring genres.

- **style** top: house music (0.53), electronic dance music (0.49), trap beat (0.45), techno (0.45), dubstep (0.40), synthwave (0.39)
  - stands out: house music (z=+2.2), electronic dance music (z=+1.5), dubstep (z=+1.4), trap beat (z=+1.3), techno (z=+1.2)
- **instrument** top: drum machine (0.51), sampled breakbeat (0.49), vocal chops (0.48), lead synthesizer (0.46), 808 bass (0.44), synth bass (0.41)
  - stands out: sampled breakbeat (z=+2.6), drum machine (z=+1.5), lead synthesizer (z=+0.9), 808 bass (z=+0.9), vocal chops (z=+0.6)
- **mood** top: energetic (0.44), uplifting (0.40), hypnotic (0.33), nostalgic (0.25), dark (0.24), calm (0.23)
  - stands out: energetic (z=+1.3), uplifting (z=-0.0), aggressive (z=-0.6), calm (z=-0.6), playful (z=-0.7)
- **production** top: polished modern production (0.39), vintage analog sound (0.35), lo-fi recording (0.28), dense layered arrangement (0.24), heavily compressed (0.20), minimal sparse arrangement (0.19)
  - stands out: polished modern production (z=+0.9), vintage analog sound (z=-0.2), lo-fi recording (z=-0.3), heavily compressed (z=-0.6), dense layered arrangement (z=-0.8)
