# CLAP zero-shot tags — t5fe4a915

Model `laion/larger_clap_music_and_speech`, track embedding = mean of 10s windows. 'Top' = highest raw text-audio similarity; 'stands out' = highest z-score relative to the other tracks in this collection. Weak, style-level evidence only: CLAP often confuses neighbouring genres.

- **style** top: shoegaze (0.56), post-rock (0.55), indie rock (0.53), trip-hop (0.50), UK garage (0.48), synthwave (0.48)
  - stands out: indie rock (z=+2.1), post-rock (z=+1.9), progressive rock (z=+1.8), psychedelic rock (z=+1.7), shoegaze (z=+1.7)
- **instrument** top: electric piano (0.55), piano (0.53), vocal chops (0.49), bass guitar (0.48), bells (0.47), clean electric guitar (0.47)
  - stands out: distorted electric guitar (z=+2.0), bass guitar (z=+1.7), clean electric guitar (z=+1.4), upright bass (z=+1.3), acoustic drum kit (z=+1.3)
- **mood** top: nostalgic (0.56), sad (0.48), dark (0.46), hypnotic (0.45), anxious (0.45), aggressive (0.44)
  - stands out: aggressive (z=+1.7), nostalgic (z=+1.3), dark (z=+1.3), sad (z=+1.2), anxious (z=+1.2)
- **production** top: minimal sparse arrangement (0.44), dense layered arrangement (0.38), vintage analog sound (0.35), dry close-miked sound (0.35), heavily compressed (0.34), lo-fi recording (0.33)
  - stands out: dry close-miked sound (z=+1.2), heavily compressed (z=+1.1), minimal sparse arrangement (z=+1.0), distorted and noisy (z=+0.8), dense layered arrangement (z=+0.6)
