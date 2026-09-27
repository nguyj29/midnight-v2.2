# CLAP zero-shot tags — t47e13f42

Model `laion/larger_clap_music_and_speech`, track embedding = mean of 10s windows. 'Top' = highest raw text-audio similarity; 'stands out' = highest z-score relative to the other tracks in this collection. Weak, style-level evidence only: CLAP often confuses neighbouring genres.

- **style** top: chiptune (0.53), math rock (0.46), video game soundtrack (0.44), glitchy IDM electronica (0.43), synthwave (0.42), anime soundtrack (0.40)
  - stands out: chiptune (z=+2.7), math rock (z=+1.5), glitchy IDM electronica (z=+1.4), video game soundtrack (z=+0.7), anime soundtrack (z=+0.5)
- **instrument** top: lead synthesizer (0.46), organ (0.39), arpeggiator (0.34), synthesizer pads (0.33), synth bass (0.32), 808 bass (0.30)
  - stands out: lead synthesizer (z=+0.9), marimba (z=+0.6), organ (z=-0.2), bells (z=-0.3), synthesizer pads (z=-0.5)
- **mood** top: happy (0.35), hypnotic (0.32), uplifting (0.29), nostalgic (0.29), playful (0.28), anxious (0.25)
  - stands out: happy (z=+0.3), playful (z=-0.1), mysterious (z=-0.3), anxious (z=-0.3), tense (z=-0.5)
- **production** top: vintage analog sound (0.38), home demo quality (0.29), polished modern production (0.28), dry close-miked sound (0.25), distorted and noisy (0.23), dense layered arrangement (0.20)
  - stands out: distorted and noisy (z=+0.8), home demo quality (z=+0.7), vintage analog sound (z=+0.1), dry close-miked sound (z=+0.1), live band recording (z=-0.2)
