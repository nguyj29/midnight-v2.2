# CLAP zero-shot tags — tee211b9a

Model `laion/larger_clap_music_and_speech`, track embedding = mean of 10s windows. 'Top' = highest raw text-audio similarity; 'stands out' = highest z-score relative to the other tracks in this collection. Weak, style-level evidence only: CLAP often confuses neighbouring genres.

- **style** top: synthwave (0.44), lo-fi hip hop beat (0.42), electronic dance music (0.39), trap beat (0.37), shoegaze (0.36), indie rock (0.34)
  - stands out: lo-fi hip hop beat (z=+0.9), trap beat (z=+0.4), electronic dance music (z=+0.4), synthwave (z=+0.1), indie rock (z=+0.0)
- **instrument** top: vocal chops (0.46), 808 bass (0.40), synth bass (0.39), piano (0.36), lead synthesizer (0.36), drum machine (0.35)
  - stands out: vocal chops (z=+0.4), 808 bass (z=+0.3), distorted electric guitar (z=+0.2), sampled breakbeat (z=+0.2), synth bass (z=-0.0)
- **mood** top: dark (0.35), hypnotic (0.31), nostalgic (0.29), aggressive (0.28), sad (0.25), uplifting (0.24)
  - stands out: aggressive (z=+0.0), dark (z=-0.0), bittersweet (z=-0.5), anxious (z=-0.6), sad (z=-0.6)
- **production** top: vintage analog sound (0.31), dense layered arrangement (0.31), lo-fi recording (0.29), distorted and noisy (0.24), minimal sparse arrangement (0.23), heavily compressed (0.23)
  - stands out: distorted and noisy (z=+1.0), dense layered arrangement (z=-0.1), heavily compressed (z=-0.2), lo-fi recording (z=-0.2), minimal sparse arrangement (z=-0.7)
