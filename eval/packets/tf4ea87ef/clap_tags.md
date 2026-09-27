# CLAP zero-shot tags — tf4ea87ef

Model `laion/larger_clap_music_and_speech`, track embedding = mean of 10s windows. 'Top' = highest raw text-audio similarity; 'stands out' = highest z-score relative to the other tracks in this collection. Weak, style-level evidence only: CLAP often confuses neighbouring genres.

- **style** top: downtempo chillout (0.57), ambient (0.51), vaporwave (0.47), new age (0.47), minimalist music (0.44), shoegaze (0.43)
  - stands out: ambient (z=+1.9), downtempo chillout (z=+1.6), solo classical piano (z=+1.5), neoclassical (z=+1.4), vaporwave (z=+1.4)
- **instrument** top: electric piano (0.54), harp (0.51), piano (0.49), bells (0.47), arpeggiator (0.47), synthesizer pads (0.45)
  - stands out: marimba (z=+1.4), harp (z=+1.3), clean electric guitar (z=+1.1), flute (z=+1.0), bells (z=+1.0)
- **mood** top: calm (0.54), dreamy (0.54), uplifting (0.53), peaceful (0.52), sad (0.51), anxious (0.50)
  - stands out: calm (z=+1.8), dreamy (z=+1.8), peaceful (z=+1.8), mysterious (z=+1.7), bittersweet (z=+1.7)
- **production** top: minimal sparse arrangement (0.54), spacious reverb (0.47), dense layered arrangement (0.41), lo-fi recording (0.38), home demo quality (0.37), polished modern production (0.36)
  - stands out: spacious reverb (z=+2.2), minimal sparse arrangement (z=+1.8), home demo quality (z=+1.5), live band recording (z=+1.3), dry close-miked sound (z=+0.9)
