# CLAP zero-shot tags — ted20dc6f

Model `laion/larger_clap_music_and_speech`, track embedding = mean of 10s windows. 'Top' = highest raw text-audio similarity; 'stands out' = highest z-score relative to the other tracks in this collection. Weak, style-level evidence only: CLAP often confuses neighbouring genres.

- **style** top: shoegaze (0.58), psychedelic rock (0.54), post-rock (0.52), synthwave (0.50), progressive rock (0.48), indie rock (0.46)
  - stands out: psychedelic rock (z=+2.6), shoegaze (z=+1.9), progressive rock (z=+1.8), gospel (z=+1.6), heavy metal (z=+1.6)
- **instrument** top: organ (0.51), vocal chops (0.51), electric piano (0.50), arpeggiator (0.46), orchestra (0.46), synth bass (0.45)
  - stands out: distorted electric guitar (z=+1.8), saxophone (z=+1.7), brass section (z=+1.4), choir (z=+1.4), organ (z=+1.2)
- **mood** top: dark (0.50), hypnotic (0.44), nostalgic (0.43), aggressive (0.43), triumphant (0.39), uplifting (0.38)
  - stands out: dark (z=+1.7), aggressive (z=+1.6), epic (z=+0.9), hypnotic (z=+0.6), triumphant (z=+0.6)
- **production** top: dense layered arrangement (0.45), heavily compressed (0.41), vintage analog sound (0.40), lo-fi recording (0.36), minimal sparse arrangement (0.33), polished modern production (0.32)
  - stands out: heavily compressed (z=+1.9), distorted and noisy (z=+1.5), dense layered arrangement (z=+1.3), live band recording (z=+0.9), lo-fi recording (z=+0.6)
