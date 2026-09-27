# CLAP zero-shot tags — t6ce48b07

Model `laion/larger_clap_music_and_speech`, track embedding = mean of 10s windows. 'Top' = highest raw text-audio similarity; 'stands out' = highest z-score relative to the other tracks in this collection. Weak, style-level evidence only: CLAP often confuses neighbouring genres.

- **style** top: synthwave (0.48), lo-fi hip hop beat (0.48), trip-hop (0.45), downtempo chillout (0.44), shoegaze (0.43), trap beat (0.43)
  - stands out: lo-fi hip hop beat (z=+1.5), boom bap hip hop (z=+1.2), trap beat (z=+1.0), trip-hop (z=+1.0), funk (z=+0.7)
- **instrument** top: vocal chops (0.49), drum machine (0.46), electric piano (0.46), organ (0.44), synth bass (0.44), 808 bass (0.44)
  - stands out: drum machine (z=+0.9), sampled breakbeat (z=+0.8), 808 bass (z=+0.8), vocal chops (z=+0.8), lead synthesizer (z=+0.7)
- **mood** top: nostalgic (0.45), hypnotic (0.42), dark (0.38), sad (0.34), uplifting (0.34), calm (0.32)
  - stands out: nostalgic (z=+0.4), dark (z=+0.4), hypnotic (z=+0.3), peaceful (z=+0.2), romantic (z=+0.2)
- **production** top: vintage analog sound (0.45), lo-fi recording (0.43), polished modern production (0.33), minimal sparse arrangement (0.31), dense layered arrangement (0.26), home demo quality (0.24)
  - stands out: lo-fi recording (z=+1.4), vintage analog sound (z=+1.2), live band recording (z=+0.2), home demo quality (z=+0.1), dry close-miked sound (z=+0.0)
