# CLAP zero-shot tags — tde35730e

Model `laion/larger_clap_music_and_speech`, track embedding = mean of 10s windows. 'Top' = highest raw text-audio similarity; 'stands out' = highest z-score relative to the other tracks in this collection. Weak, style-level evidence only: CLAP often confuses neighbouring genres.

- **style** top: chamber music (0.54), jazz (0.53), gospel (0.53), anime soundtrack (0.50), new age (0.50), shoegaze (0.49)
  - stands out: gospel (z=+2.7), world music (z=+2.4), chamber music (z=+2.2), jazz (z=+2.2), neoclassical (z=+2.1)
- **instrument** top: bells (0.65), piano (0.56), electric piano (0.55), orchestra (0.54), harp (0.54), organ (0.53)
  - stands out: choir (z=+2.6), bells (z=+2.2), violin (z=+2.1), orchestra (z=+1.8), brass section (z=+1.7)
- **mood** top: triumphant (0.55), mysterious (0.55), happy (0.54), anxious (0.51), nostalgic (0.50), epic (0.49)
  - stands out: mysterious (z=+2.2), epic (z=+2.1), triumphant (z=+1.8), happy (z=+1.8), anxious (z=+1.6)
- **production** top: minimal sparse arrangement (0.41), dense layered arrangement (0.40), spacious reverb (0.38), dry close-miked sound (0.37), heavily compressed (0.34), live band recording (0.34)
  - stands out: live band recording (z=+1.9), spacious reverb (z=+1.6), dry close-miked sound (z=+1.5), distorted and noisy (z=+1.1), heavily compressed (z=+1.0)
