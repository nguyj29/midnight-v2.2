# CLAP zero-shot tags — t61233098

Model `laion/larger_clap_music_and_speech`, track embedding = mean of 10s windows. 'Top' = highest raw text-audio similarity; 'stands out' = highest z-score relative to the other tracks in this collection. Weak, style-level evidence only: CLAP often confuses neighbouring genres.

- **style** top: orchestral film score (0.54), drum and bass (0.52), epic cinematic trailer music (0.49), video game soundtrack (0.47), shoegaze (0.45), chamber music (0.45)
  - stands out: epic cinematic trailer music (z=+2.6), orchestral film score (z=+2.4), drum and bass (z=+2.2), chamber music (z=+1.6), heavy metal (z=+1.5)
- **instrument** top: orchestra (0.64), string section (0.61), brass section (0.57), cello (0.55), piano (0.51), violin (0.50)
  - stands out: brass section (z=+3.0), string section (z=+3.0), violin (z=+2.7), orchestra (z=+2.6), cello (z=+2.5)
- **mood** top: triumphant (0.62), epic (0.54), nostalgic (0.49), dark (0.48), uplifting (0.48), happy (0.46)
  - stands out: epic (z=+2.6), triumphant (z=+2.4), aggressive (z=+1.7), dark (z=+1.5), playful (z=+1.4)
- **production** top: dense layered arrangement (0.45), polished modern production (0.45), heavily compressed (0.43), minimal sparse arrangement (0.36), vintage analog sound (0.33), spacious reverb (0.32)
  - stands out: heavily compressed (z=+2.0), polished modern production (z=+1.7), dense layered arrangement (z=+1.3), spacious reverb (z=+1.1), live band recording (z=+0.9)
