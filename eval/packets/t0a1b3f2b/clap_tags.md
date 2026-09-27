# CLAP zero-shot tags — t0a1b3f2b

Model `laion/larger_clap_music_and_speech`, track embedding = mean of 10s windows. 'Top' = highest raw text-audio similarity; 'stands out' = highest z-score relative to the other tracks in this collection. Weak, style-level evidence only: CLAP often confuses neighbouring genres.

- **style** top: synthwave (0.44), house music (0.43), lo-fi hip hop beat (0.42), downtempo chillout (0.41), electronic dance music (0.40), trap beat (0.38)
  - stands out: boom bap hip hop (z=+0.9), reggae (z=+0.9), lo-fi hip hop beat (z=+0.8), house music (z=+0.8), trap beat (z=+0.6)
- **instrument** top: 808 bass (0.50), vocal chops (0.49), drum machine (0.48), synth bass (0.44), lead synthesizer (0.42), piano (0.38)
  - stands out: 808 bass (z=+1.6), drum machine (z=+1.1), sampled breakbeat (z=+1.1), vocal chops (z=+0.7), synth bass (z=+0.6)
- **mood** top: uplifting (0.38), nostalgic (0.37), hypnotic (0.34), dark (0.32), energetic (0.32), sad (0.27)
  - stands out: energetic (z=+0.3), romantic (z=-0.2), dark (z=-0.3), nostalgic (z=-0.3), uplifting (z=-0.3)
- **production** top: vintage analog sound (0.40), lo-fi recording (0.31), polished modern production (0.30), dense layered arrangement (0.24), minimal sparse arrangement (0.23), dry close-miked sound (0.19)
  - stands out: vintage analog sound (z=+0.5), lo-fi recording (z=+0.1), polished modern production (z=-0.3), dry close-miked sound (z=-0.5), minimal sparse arrangement (z=-0.8)
