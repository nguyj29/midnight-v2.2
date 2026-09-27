# CLAP zero-shot tags — t0d513ac8

Model `laion/larger_clap_music_and_speech`, track embedding = mean of 10s windows. 'Top' = highest raw text-audio similarity; 'stands out' = highest z-score relative to the other tracks in this collection. Weak, style-level evidence only: CLAP often confuses neighbouring genres.

- **style** top: shoegaze (0.51), synthwave (0.51), UK garage (0.49), post-rock (0.49), downtempo chillout (0.47), lo-fi hip hop beat (0.47)
  - stands out: lo-fi hip hop beat (z=+1.4), drum and bass (z=+1.3), post-rock (z=+1.2), shoegaze (z=+1.2), UK garage (z=+1.2)
- **instrument** top: vocal chops (0.56), electric piano (0.55), piano (0.54), organ (0.50), arpeggiator (0.49), synth bass (0.48)
  - stands out: sampled breakbeat (z=+1.9), vocal chops (z=+1.8), distorted electric guitar (z=+1.7), bass guitar (z=+1.4), organ (z=+1.1)
- **mood** top: nostalgic (0.47), hypnotic (0.46), dark (0.44), uplifting (0.41), triumphant (0.41), anxious (0.39)
  - stands out: aggressive (z=+1.1), dark (z=+1.0), hypnotic (z=+0.9), triumphant (z=+0.7), anxious (z=+0.7)
- **production** top: lo-fi recording (0.43), minimal sparse arrangement (0.41), dense layered arrangement (0.40), vintage analog sound (0.40), polished modern production (0.39), heavily compressed (0.37)
  - stands out: lo-fi recording (z=+1.4), heavily compressed (z=+1.4), distorted and noisy (z=+1.2), live band recording (z=+0.9), polished modern production (z=+0.8)
