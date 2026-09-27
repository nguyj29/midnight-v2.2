# CLAP zero-shot tags — t3b9d70c1

Model `laion/larger_clap_music_and_speech`, track embedding = mean of 10s windows. 'Top' = highest raw text-audio similarity; 'stands out' = highest z-score relative to the other tracks in this collection. Weak, style-level evidence only: CLAP often confuses neighbouring genres.

- **style** top: synthwave (0.43), downtempo chillout (0.42), trap beat (0.42), lo-fi hip hop beat (0.41), house music (0.39), shoegaze (0.39)
  - stands out: trap beat (z=+1.0), reggae (z=+0.8), lo-fi hip hop beat (z=+0.8), future bass (z=+0.6), downtempo chillout (z=+0.3)
- **instrument** top: electric piano (0.43), vocal chops (0.43), synth bass (0.42), 808 bass (0.41), synthesizer pads (0.40), organ (0.38)
  - stands out: clean electric guitar (z=+0.5), 808 bass (z=+0.4), distorted electric guitar (z=+0.3), synth bass (z=+0.3), synthesizer pads (z=+0.3)
- **mood** top: nostalgic (0.37), hypnotic (0.36), dark (0.36), uplifting (0.30), calm (0.30), dreamy (0.28)
  - stands out: dark (z=+0.1), calm (z=-0.0), dreamy (z=-0.0), peaceful (z=-0.2), nostalgic (z=-0.3)
- **production** top: lo-fi recording (0.39), vintage analog sound (0.36), minimal sparse arrangement (0.30), dense layered arrangement (0.28), polished modern production (0.27), dry close-miked sound (0.19)
  - stands out: lo-fi recording (z=+1.0), live band recording (z=+0.1), spacious reverb (z=-0.0), minimal sparse arrangement (z=-0.1), vintage analog sound (z=-0.1)
