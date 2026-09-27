# CLAP zero-shot tags — ted929feb

Model `laion/larger_clap_music_and_speech`, track embedding = mean of 10s windows. 'Top' = highest raw text-audio similarity; 'stands out' = highest z-score relative to the other tracks in this collection. Weak, style-level evidence only: CLAP often confuses neighbouring genres.

- **style** top: piano and strings (0.57), UK garage (0.42), post-rock (0.42), indie rock (0.40), downtempo chillout (0.40), shoegaze (0.40)
  - stands out: solo classical piano (z=+1.9), piano and strings (z=+1.8), bossa nova (z=+1.6), acoustic folk (z=+1.4), latin music (z=+1.1)
- **instrument** top: piano (0.55), electric piano (0.54), harp (0.52), clean electric guitar (0.47), arpeggiator (0.45), bells (0.45)
  - stands out: clean electric guitar (z=+1.5), acoustic guitar (z=+1.4), harp (z=+1.3), acoustic drum kit (z=+1.3), piano (z=+1.1)
- **mood** top: nostalgic (0.54), uplifting (0.47), sad (0.46), dreamy (0.41), happy (0.40), melancholic (0.39)
  - stands out: nostalgic (z=+1.2), sad (z=+1.0), dreamy (z=+0.9), romantic (z=+0.9), melancholic (z=+0.9)
- **production** top: minimal sparse arrangement (0.42), dense layered arrangement (0.36), polished modern production (0.29), home demo quality (0.27), dry close-miked sound (0.26), lo-fi recording (0.25)
  - stands out: minimal sparse arrangement (z=+0.8), home demo quality (z=+0.5), dense layered arrangement (z=+0.4), spacious reverb (z=+0.3), dry close-miked sound (z=+0.2)
