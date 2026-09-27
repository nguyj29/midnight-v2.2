# CLAP zero-shot tags — t77478144

Model `laion/larger_clap_music_and_speech`, track embedding = mean of 10s windows. 'Top' = highest raw text-audio similarity; 'stands out' = highest z-score relative to the other tracks in this collection. Weak, style-level evidence only: CLAP often confuses neighbouring genres.

- **style** top: piano and strings (0.57), new age (0.49), shoegaze (0.47), neoclassical (0.46), orchestral film score (0.44), downtempo chillout (0.43)
  - stands out: epic cinematic trailer music (z=+2.0), neoclassical (z=+1.9), piano and strings (z=+1.8), orchestral film score (z=+1.7), solo classical piano (z=+1.6)
- **instrument** top: piano (0.57), electric piano (0.53), bells (0.49), harp (0.48), orchestra (0.48), synthesizer pads (0.46)
  - stands out: cello (z=+1.5), piano (z=+1.4), choir (z=+1.3), orchestra (z=+1.3), harp (z=+1.1)
- **mood** top: melancholic (0.53), bittersweet (0.52), nostalgic (0.51), uplifting (0.50), sad (0.48), hypnotic (0.48)
  - stands out: bittersweet (z=+1.9), melancholic (z=+1.8), epic (z=+1.6), tense (z=+1.6), mysterious (z=+1.3)
- **production** top: dense layered arrangement (0.52), minimal sparse arrangement (0.48), spacious reverb (0.39), polished modern production (0.34), vintage analog sound (0.32), dry close-miked sound (0.23)
  - stands out: dense layered arrangement (z=+2.0), spacious reverb (z=+1.7), minimal sparse arrangement (z=+1.3), polished modern production (z=+0.2), distorted and noisy (z=-0.0)
