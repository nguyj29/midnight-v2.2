# CLAP zero-shot tags — t8d54bfc3

Model `laion/larger_clap_music_and_speech`, track embedding = mean of 10s windows. 'Top' = highest raw text-audio similarity; 'stands out' = highest z-score relative to the other tracks in this collection. Weak, style-level evidence only: CLAP often confuses neighbouring genres.

- **style** top: downtempo chillout (0.57), new age (0.53), piano and strings (0.46), vaporwave (0.42), minimalist music (0.42), synthwave (0.42)
  - stands out: new age (z=+1.7), downtempo chillout (z=+1.6), solo classical piano (z=+1.4), neoclassical (z=+1.2), minimalist music (z=+1.2)
- **instrument** top: electric piano (0.55), piano (0.55), arpeggiator (0.50), harp (0.50), synthesizer pads (0.49), bells (0.45)
  - stands out: synthesizer pads (z=+1.3), clean electric guitar (z=+1.2), harp (z=+1.2), piano (z=+1.1), arpeggiator (z=+1.1)
- **mood** top: uplifting (0.61), nostalgic (0.54), calm (0.52), hypnotic (0.48), dreamy (0.48), sad (0.48)
  - stands out: uplifting (z=+2.2), calm (z=+1.7), bittersweet (z=+1.6), peaceful (z=+1.4), melancholic (z=+1.4)
- **production** top: minimal sparse arrangement (0.51), polished modern production (0.41), dense layered arrangement (0.40), vintage analog sound (0.38), spacious reverb (0.35), home demo quality (0.34)
  - stands out: minimal sparse arrangement (z=+1.5), spacious reverb (z=+1.4), polished modern production (z=+1.2), home demo quality (z=+1.2), dense layered arrangement (z=+0.7)
