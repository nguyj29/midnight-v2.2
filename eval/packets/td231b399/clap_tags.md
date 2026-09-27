# CLAP zero-shot tags — td231b399

Model `laion/larger_clap_music_and_speech`, track embedding = mean of 10s windows. 'Top' = highest raw text-audio similarity; 'stands out' = highest z-score relative to the other tracks in this collection. Weak, style-level evidence only: CLAP often confuses neighbouring genres.

- **style** top: UK garage (0.47), vaporwave (0.43), shoegaze (0.37), synthwave (0.36), funk (0.36), post-rock (0.35)
  - stands out: breakcore (z=+1.0), gospel (z=+1.0), UK garage (z=+1.0), vaporwave (z=+0.8), heavy metal (z=+0.8)
- **instrument** top: organ (0.45), electric piano (0.45), arpeggiator (0.41), flute (0.40), vocal chops (0.40), orchestra (0.40)
  - stands out: brass section (z=+1.1), string section (z=+0.9), choir (z=+0.9), saxophone (z=+0.7), violin (z=+0.7)
- **mood** top: nostalgic (0.36), hypnotic (0.35), triumphant (0.34), uplifting (0.34), peaceful (0.34), epic (0.33)
  - stands out: epic (z=+0.7), mysterious (z=+0.5), peaceful (z=+0.4), triumphant (z=+0.2), calm (z=+0.1)
- **production** top: lo-fi recording (0.45), vintage analog sound (0.39), home demo quality (0.35), live band recording (0.33), polished modern production (0.29), dry close-miked sound (0.26)
  - stands out: live band recording (z=+1.8), lo-fi recording (z=+1.6), home demo quality (z=+1.3), spacious reverb (z=+0.3), vintage analog sound (z=+0.3)
