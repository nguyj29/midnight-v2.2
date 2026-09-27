# CLAP zero-shot tags — tc8f1d0c8

Model `laion/larger_clap_music_and_speech`, track embedding = mean of 10s windows. 'Top' = highest raw text-audio similarity; 'stands out' = highest z-score relative to the other tracks in this collection. Weak, style-level evidence only: CLAP often confuses neighbouring genres.

- **style** top: downtempo chillout (0.63), trip-hop (0.54), ambient (0.52), vaporwave (0.50), UK garage (0.47), house music (0.47)
  - stands out: downtempo chillout (z=+2.2), ambient (z=+1.9), trip-hop (z=+1.9), future bass (z=+1.9), vaporwave (z=+1.8)
- **instrument** top: electric piano (0.54), flute (0.46), arpeggiator (0.46), piano (0.46), harp (0.45), vocal chops (0.45)
  - stands out: flute (z=+1.3), bass guitar (z=+1.2), marimba (z=+1.2), violin (z=+1.0), clean electric guitar (z=+1.0)
- **mood** top: calm (0.55), hypnotic (0.54), peaceful (0.52), uplifting (0.49), dreamy (0.48), sad (0.47)
  - stands out: hypnotic (z=+1.9), calm (z=+1.9), peaceful (z=+1.7), tense (z=+1.5), dreamy (z=+1.4)
- **production** top: minimal sparse arrangement (0.53), lo-fi recording (0.45), polished modern production (0.43), vintage analog sound (0.41), home demo quality (0.38), dense layered arrangement (0.37)
  - stands out: minimal sparse arrangement (z=+1.7), home demo quality (z=+1.6), lo-fi recording (z=+1.6), live band recording (z=+1.4), polished modern production (z=+1.4)
