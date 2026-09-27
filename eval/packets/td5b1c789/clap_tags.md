# CLAP zero-shot tags — td5b1c789

Model `laion/larger_clap_music_and_speech`, track embedding = mean of 10s windows. 'Top' = highest raw text-audio similarity; 'stands out' = highest z-score relative to the other tracks in this collection. Weak, style-level evidence only: CLAP often confuses neighbouring genres.

- **style** top: UK garage (0.51), synthwave (0.47), anime soundtrack (0.46), glitchy IDM electronica (0.45), video game soundtrack (0.44), math rock (0.44)
  - stands out: glitchy IDM electronica (z=+1.7), UK garage (z=+1.4), funk (z=+1.3), math rock (z=+1.2), breakcore (z=+1.2)
- **instrument** top: piano (0.57), electric piano (0.56), vocal chops (0.55), arpeggiator (0.48), organ (0.46), drum machine (0.46)
  - stands out: vocal chops (z=+1.7), piano (z=+1.3), bass guitar (z=+1.3), electric piano (z=+1.1), acoustic drum kit (z=+1.1)
- **mood** top: nostalgic (0.50), uplifting (0.47), happy (0.43), energetic (0.40), triumphant (0.37), playful (0.37)
  - stands out: energetic (z=+1.0), happy (z=+0.9), nostalgic (z=+0.8), uplifting (z=+0.7), playful (z=+0.7)
- **production** top: vintage analog sound (0.37), polished modern production (0.34), lo-fi recording (0.31), home demo quality (0.30), heavily compressed (0.28), minimal sparse arrangement (0.28)
  - stands out: home demo quality (z=+0.8), heavily compressed (z=+0.4), polished modern production (z=+0.2), live band recording (z=+0.2), distorted and noisy (z=+0.2)
