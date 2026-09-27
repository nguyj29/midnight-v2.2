# CLAP zero-shot tags — t2e8079b2

Model `laion/larger_clap_music_and_speech`, track embedding = mean of 10s windows. 'Top' = highest raw text-audio similarity; 'stands out' = highest z-score relative to the other tracks in this collection. Weak, style-level evidence only: CLAP often confuses neighbouring genres.

- **style** top: UK garage (0.46), downtempo chillout (0.46), boom bap hip hop (0.44), house music (0.42), synthwave (0.41), trip-hop (0.41)
  - stands out: boom bap hip hop (z=+1.7), chiptune (z=+1.2), minimalist music (z=+1.0), ambient (z=+1.0), future bass (z=+1.0)
- **instrument** top: electric piano (0.48), synthesizer pads (0.46), 808 bass (0.42), lead synthesizer (0.41), clean electric guitar (0.39), piano (0.38)
  - stands out: marimba (z=+1.3), synthesizer pads (z=+1.0), clean electric guitar (z=+0.7), 808 bass (z=+0.6), electric piano (z=+0.4)
- **mood** top: hypnotic (0.46), peaceful (0.42), anxious (0.41), calm (0.41), happy (0.39), dreamy (0.39)
  - stands out: peaceful (z=+1.1), anxious (z=+0.9), hypnotic (z=+0.8), calm (z=+0.8), mysterious (z=+0.8)
- **production** top: vintage analog sound (0.46), lo-fi recording (0.45), home demo quality (0.44), minimal sparse arrangement (0.41), dry close-miked sound (0.40), polished modern production (0.33)
  - stands out: home demo quality (z=+2.3), dry close-miked sound (z=+1.8), lo-fi recording (z=+1.7), vintage analog sound (z=+1.3), live band recording (z=+1.0)
