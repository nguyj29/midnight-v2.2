# CLAP zero-shot tags — t3c988896

Model `laion/larger_clap_music_and_speech`, track embedding = mean of 10s windows. 'Top' = highest raw text-audio similarity; 'stands out' = highest z-score relative to the other tracks in this collection. Weak, style-level evidence only: CLAP often confuses neighbouring genres.

- **style** top: synthwave (0.44), lo-fi hip hop beat (0.42), downtempo chillout (0.41), trip-hop (0.40), boom bap hip hop (0.38), UK garage (0.38)
  - stands out: boom bap hip hop (z=+1.0), lo-fi hip hop beat (z=+0.9), trip-hop (z=+0.4), reggae (z=+0.2), downtempo chillout (z=+0.2)
- **instrument** top: 808 bass (0.44), drum machine (0.43), synth bass (0.40), vocal chops (0.39), synthesizer pads (0.39), lead synthesizer (0.37)
  - stands out: 808 bass (z=+0.8), drum machine (z=+0.5), synthesizer pads (z=+0.1), synth bass (z=+0.1), brass section (z=-0.1)
- **mood** top: dark (0.38), hypnotic (0.36), nostalgic (0.35), sad (0.30), uplifting (0.28), calm (0.26)
  - stands out: dark (z=+0.3), sad (z=-0.3), calm (z=-0.3), peaceful (z=-0.3), romantic (z=-0.3)
- **production** top: vintage analog sound (0.43), lo-fi recording (0.37), dry close-miked sound (0.25), polished modern production (0.25), minimal sparse arrangement (0.23), home demo quality (0.20)
  - stands out: vintage analog sound (z=+0.9), lo-fi recording (z=+0.7), dry close-miked sound (z=+0.1), live band recording (z=-0.3), home demo quality (z=-0.3)
