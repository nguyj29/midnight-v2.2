# CLAP zero-shot tags — t052c16ae

Model `laion/larger_clap_music_and_speech`, track embedding = mean of 10s windows. 'Top' = highest raw text-audio similarity; 'stands out' = highest z-score relative to the other tracks in this collection. Weak, style-level evidence only: CLAP often confuses neighbouring genres.

- **style** top: synthwave (0.49), lo-fi hip hop beat (0.42), electronic dance music (0.42), trap beat (0.39), shoegaze (0.39), techno (0.38)
  - stands out: lo-fi hip hop beat (z=+0.9), electronic dance music (z=+0.7), trap beat (z=+0.7), synthwave (z=+0.6), techno (z=+0.3)
- **instrument** top: synthesizer pads (0.43), vocal chops (0.43), organ (0.42), synth bass (0.41), lead synthesizer (0.39), 808 bass (0.38)
  - stands out: synthesizer pads (z=+0.7), synth bass (z=+0.2), organ (z=+0.2), sampled breakbeat (z=+0.2), lead synthesizer (z=+0.1)
- **mood** top: dark (0.40), hypnotic (0.38), nostalgic (0.35), uplifting (0.32), sad (0.28), aggressive (0.25)
  - stands out: dark (z=+0.6), hypnotic (z=-0.2), aggressive (z=-0.2), dreamy (z=-0.3), melancholic (z=-0.4)
- **production** top: vintage analog sound (0.41), lo-fi recording (0.36), dense layered arrangement (0.34), minimal sparse arrangement (0.28), polished modern production (0.26), distorted and noisy (0.21)
  - stands out: distorted and noisy (z=+0.6), vintage analog sound (z=+0.6), lo-fi recording (z=+0.6), dense layered arrangement (z=+0.1), minimal sparse arrangement (z=-0.3)
