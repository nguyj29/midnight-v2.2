# CLAP zero-shot tags — t709e8ec1

Model `laion/larger_clap_music_and_speech`, track embedding = mean of 10s windows. 'Top' = highest raw text-audio similarity; 'stands out' = highest z-score relative to the other tracks in this collection. Weak, style-level evidence only: CLAP often confuses neighbouring genres.

- **style** top: piano and strings (0.55), new age (0.49), minimalist music (0.42), neoclassical (0.41), downtempo chillout (0.41), jazz (0.40)
  - stands out: bossa nova (z=+2.1), acoustic folk (z=+2.0), solo classical piano (z=+1.9), latin music (z=+1.9), piano and strings (z=+1.7)
- **instrument** top: harp (0.57), electric piano (0.52), piano (0.51), cello (0.42), marimba (0.42), bells (0.40)
  - stands out: marimba (z=+1.7), harp (z=+1.6), cello (z=+1.5), acoustic guitar (z=+1.3), upright bass (z=+0.9)
- **mood** top: dreamy (0.52), romantic (0.50), melancholic (0.49), nostalgic (0.49), uplifting (0.48), calm (0.48)
  - stands out: romantic (z=+1.7), dreamy (z=+1.7), melancholic (z=+1.5), playful (z=+1.5), bittersweet (z=+1.5)
- **production** top: minimal sparse arrangement (0.43), dense layered arrangement (0.34), polished modern production (0.31), dry close-miked sound (0.28), spacious reverb (0.27), home demo quality (0.26)
  - stands out: minimal sparse arrangement (z=+0.9), spacious reverb (z=+0.8), dry close-miked sound (z=+0.5), home demo quality (z=+0.3), dense layered arrangement (z=+0.2)
