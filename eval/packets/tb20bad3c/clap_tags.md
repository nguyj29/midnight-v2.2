# CLAP zero-shot tags — tb20bad3c

Model `laion/larger_clap_music_and_speech`, track embedding = mean of 10s windows. 'Top' = highest raw text-audio similarity; 'stands out' = highest z-score relative to the other tracks in this collection. Weak, style-level evidence only: CLAP often confuses neighbouring genres.

- **style** top: synthwave (0.52), downtempo chillout (0.49), shoegaze (0.47), video game soundtrack (0.45), UK garage (0.45), new age (0.45)
  - stands out: new age (z=+1.0), downtempo chillout (z=+1.0), synthwave (z=+0.9), video game soundtrack (z=+0.8), trip-hop (z=+0.8)
- **instrument** top: electric piano (0.54), piano (0.53), organ (0.50), synthesizer pads (0.49), vocal chops (0.49), arpeggiator (0.47)
  - stands out: synthesizer pads (z=+1.4), organ (z=+1.1), piano (z=+1.0), electric piano (z=+0.9), choir (z=+0.9)
- **mood** top: nostalgic (0.53), uplifting (0.51), hypnotic (0.48), playful (0.43), dark (0.42), happy (0.41)
  - stands out: playful (z=+1.2), nostalgic (z=+1.1), hypnotic (z=+1.1), uplifting (z=+1.1), melancholic (z=+0.9)
- **production** top: minimal sparse arrangement (0.43), vintage analog sound (0.43), dense layered arrangement (0.42), polished modern production (0.38), lo-fi recording (0.33), dry close-miked sound (0.25)
  - stands out: dense layered arrangement (z=+1.0), minimal sparse arrangement (z=+0.9), vintage analog sound (z=+0.9), polished modern production (z=+0.8), spacious reverb (z=+0.6)
