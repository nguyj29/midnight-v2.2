# CLAP zero-shot tags — tac555977

Model `laion/larger_clap_music_and_speech`, track embedding = mean of 10s windows. 'Top' = highest raw text-audio similarity; 'stands out' = highest z-score relative to the other tracks in this collection. Weak, style-level evidence only: CLAP often confuses neighbouring genres.

- **style** top: synthwave (0.56), UK garage (0.50), anime soundtrack (0.48), video game soundtrack (0.48), shoegaze (0.47), progressive rock (0.46)
  - stands out: progressive rock (z=+1.6), funk (z=+1.5), synthwave (z=+1.4), anime soundtrack (z=+1.4), heavy metal (z=+1.3)
- **instrument** top: arpeggiator (0.60), organ (0.53), synth bass (0.51), vocal chops (0.49), piano (0.49), electric piano (0.49)
  - stands out: arpeggiator (z=+2.1), synth bass (z=+1.5), brass section (z=+1.4), string section (z=+1.3), organ (z=+1.3)
- **mood** top: uplifting (0.55), energetic (0.50), triumphant (0.47), nostalgic (0.46), happy (0.41), hypnotic (0.40)
  - stands out: energetic (z=+1.9), uplifting (z=+1.5), triumphant (z=+1.2), aggressive (z=+1.0), epic (z=+0.9)
- **production** top: vintage analog sound (0.46), polished modern production (0.39), dense layered arrangement (0.38), heavily compressed (0.30), home demo quality (0.29), minimal sparse arrangement (0.26)
  - stands out: vintage analog sound (z=+1.3), polished modern production (z=+0.9), home demo quality (z=+0.7), heavily compressed (z=+0.6), dense layered arrangement (z=+0.6)
