# CLAP zero-shot tags — t94fd0413

Model `laion/larger_clap_music_and_speech`, track embedding = mean of 10s windows. 'Top' = highest raw text-audio similarity; 'stands out' = highest z-score relative to the other tracks in this collection. Weak, style-level evidence only: CLAP often confuses neighbouring genres.

- **style** top: trap beat (0.53), lo-fi hip hop beat (0.51), downtempo chillout (0.48), boom bap hip hop (0.48), trip-hop (0.45), house music (0.44)
  - stands out: boom bap hip hop (z=+2.2), trap beat (z=+2.1), lo-fi hip hop beat (z=+1.8), reggae (z=+1.5), dubstep (z=+1.3)
- **instrument** top: 808 bass (0.48), drum machine (0.47), vocal chops (0.46), lead synthesizer (0.43), synth bass (0.41), synthesizer pads (0.39)
  - stands out: 808 bass (z=+1.3), sampled breakbeat (z=+1.1), drum machine (z=+1.0), lead synthesizer (z=+0.6), vocal chops (z=+0.3)
- **mood** top: hypnotic (0.40), nostalgic (0.38), uplifting (0.37), dark (0.35), calm (0.32), playful (0.29)
  - stands out: calm (z=+0.1), hypnotic (z=+0.1), dark (z=+0.0), playful (z=-0.0), peaceful (z=-0.1)
- **production** top: vintage analog sound (0.40), lo-fi recording (0.36), minimal sparse arrangement (0.34), polished modern production (0.33), dense layered arrangement (0.26), dry close-miked sound (0.20)
  - stands out: lo-fi recording (z=+0.6), vintage analog sound (z=+0.4), minimal sparse arrangement (z=+0.2), polished modern production (z=+0.1), spacious reverb (z=-0.3)
