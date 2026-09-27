# CLAP zero-shot tags — t511aa9f7

Model `laion/larger_clap_music_and_speech`, track embedding = mean of 10s windows. 'Top' = highest raw text-audio similarity; 'stands out' = highest z-score relative to the other tracks in this collection. Weak, style-level evidence only: CLAP often confuses neighbouring genres.

- **style** top: post-rock (0.54), shoegaze (0.54), progressive rock (0.51), indie rock (0.51), video game soundtrack (0.50), piano and strings (0.49)
  - stands out: progressive rock (z=+2.2), heavy metal (z=+2.1), indie rock (z=+1.9), post-rock (z=+1.8), blues (z=+1.7)
- **instrument** top: harp (0.56), bells (0.55), acoustic drum kit (0.53), piano (0.52), electric piano (0.49), arpeggiator (0.48)
  - stands out: acoustic drum kit (z=+2.4), acoustic guitar (z=+2.2), harp (z=+1.6), bells (z=+1.5), distorted electric guitar (z=+1.5)
- **mood** top: nostalgic (0.52), sad (0.46), uplifting (0.45), aggressive (0.44), hypnotic (0.43), anxious (0.42)
  - stands out: aggressive (z=+1.7), sad (z=+1.1), nostalgic (z=+1.0), anxious (z=+1.0), tense (z=+0.9)
- **production** top: minimal sparse arrangement (0.42), heavily compressed (0.39), dense layered arrangement (0.39), dry close-miked sound (0.34), vintage analog sound (0.33), polished modern production (0.33)
  - stands out: heavily compressed (z=+1.6), dry close-miked sound (z=+1.2), home demo quality (z=+0.9), minimal sparse arrangement (z=+0.8), distorted and noisy (z=+0.7)
