# CLAP zero-shot tags — t9d4d0c39

Model `laion/larger_clap_music_and_speech`, track embedding = mean of 10s windows. 'Top' = highest raw text-audio similarity; 'stands out' = highest z-score relative to the other tracks in this collection. Weak, style-level evidence only: CLAP often confuses neighbouring genres.

- **style** top: house music (0.45), electronic dance music (0.44), synthwave (0.43), downtempo chillout (0.41), vaporwave (0.40), lo-fi hip hop beat (0.39)
  - stands out: house music (z=+1.1), electronic dance music (z=+1.0), vaporwave (z=+0.5), lo-fi hip hop beat (z=+0.5), downtempo chillout (z=+0.3)
- **instrument** top: vocal chops (0.46), electric piano (0.42), lead synthesizer (0.40), 808 bass (0.40), piano (0.39), drum machine (0.38)
  - stands out: 808 bass (z=+0.3), vocal chops (z=+0.3), lead synthesizer (z=+0.3), drum machine (z=-0.1), electric piano (z=-0.1)
- **mood** top: hypnotic (0.43), uplifting (0.39), nostalgic (0.32), dark (0.31), sad (0.30), dreamy (0.29)
  - stands out: hypnotic (z=+0.5), dreamy (z=+0.1), bittersweet (z=+0.0), uplifting (z=-0.1), calm (z=-0.1)
- **production** top: vintage analog sound (0.36), lo-fi recording (0.35), polished modern production (0.30), minimal sparse arrangement (0.29), dense layered arrangement (0.29), dry close-miked sound (0.24)
  - stands out: lo-fi recording (z=+0.5), dry close-miked sound (z=+0.1), vintage analog sound (z=-0.1), minimal sparse arrangement (z=-0.3), dense layered arrangement (z=-0.4)
