# CLAP zero-shot tags — t21aaeadf

Model `laion/larger_clap_music_and_speech`, track embedding = mean of 10s windows. 'Top' = highest raw text-audio similarity; 'stands out' = highest z-score relative to the other tracks in this collection. Weak, style-level evidence only: CLAP often confuses neighbouring genres.

- **style** top: trip-hop (0.53), jazz (0.51), jazz fusion (0.49), gospel (0.49), reggae (0.48), indie rock (0.48)
  - stands out: gospel (z=+2.3), reggae (z=+2.2), blues (z=+2.1), jazz (z=+2.0), jazz fusion (z=+2.0)
- **instrument** top: piano (0.63), electric piano (0.62), bells (0.59), vocal chops (0.56), saxophone (0.53), harp (0.52)
  - stands out: saxophone (z=+2.7), marimba (z=+2.1), acoustic guitar (z=+1.9), acoustic drum kit (z=+1.9), piano (z=+1.9)
- **mood** top: nostalgic (0.59), happy (0.52), romantic (0.50), playful (0.49), uplifting (0.47), peaceful (0.46)
  - stands out: playful (z=+1.8), romantic (z=+1.7), happy (z=+1.6), nostalgic (z=+1.6), peaceful (z=+1.3)
- **production** top: dry close-miked sound (0.47), minimal sparse arrangement (0.42), lo-fi recording (0.38), vintage analog sound (0.38), dense layered arrangement (0.32), heavily compressed (0.31)
  - stands out: dry close-miked sound (z=+2.6), live band recording (z=+1.6), minimal sparse arrangement (z=+0.8), lo-fi recording (z=+0.8), heavily compressed (z=+0.7)
