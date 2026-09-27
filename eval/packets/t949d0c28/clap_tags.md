# CLAP zero-shot tags — t949d0c28

Model `laion/larger_clap_music_and_speech`, track embedding = mean of 10s windows. 'Top' = highest raw text-audio similarity; 'stands out' = highest z-score relative to the other tracks in this collection. Weak, style-level evidence only: CLAP often confuses neighbouring genres.

- **style** top: house music (0.41), electronic dance music (0.40), lo-fi hip hop beat (0.31), techno (0.31), downtempo chillout (0.30), trap beat (0.29)
  - stands out: electronic dance music (z=+0.5), house music (z=+0.4), breakcore (z=+0.0), lo-fi hip hop beat (z=-0.4), trap beat (z=-0.4)
- **instrument** top: vocal chops (0.40), drum machine (0.38), 808 bass (0.35), lead synthesizer (0.32), piano (0.30), bass guitar (0.29)
  - stands out: sampled breakbeat (z=+0.1), drum machine (z=-0.0), 808 bass (z=-0.3), vocal chops (z=-0.5), acoustic guitar (z=-0.6)
- **mood** top: energetic (0.31), uplifting (0.31), hypnotic (0.26), calm (0.17), nostalgic (0.15), bittersweet (0.15)
  - stands out: energetic (z=+0.2), bittersweet (z=-1.0), calm (z=-1.0), uplifting (z=-1.1), dreamy (z=-1.2)
- **production** top: polished modern production (0.30), lo-fi recording (0.28), vintage analog sound (0.26), minimal sparse arrangement (0.16), heavily compressed (0.16), dense layered arrangement (0.15)
  - stands out: polished modern production (z=-0.4), lo-fi recording (z=-0.4), heavily compressed (z=-1.0), home demo quality (z=-1.1), spacious reverb (z=-1.2)
