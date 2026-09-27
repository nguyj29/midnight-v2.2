# CLAP zero-shot tags — t728b4b03

Model `laion/larger_clap_music_and_speech`, track embedding = mean of 10s windows. 'Top' = highest raw text-audio similarity; 'stands out' = highest z-score relative to the other tracks in this collection. Weak, style-level evidence only: CLAP often confuses neighbouring genres.

- **style** top: trap beat (0.48), lo-fi hip hop beat (0.42), synthwave (0.40), electronic dance music (0.36), boom bap hip hop (0.34), dubstep (0.32)
  - stands out: trap beat (z=+1.7), lo-fi hip hop beat (z=+0.9), boom bap hip hop (z=+0.6), dubstep (z=+0.5), electronic dance music (z=-0.0)
- **instrument** top: vocal chops (0.38), 808 bass (0.35), synth bass (0.34), lead synthesizer (0.34), sampled breakbeat (0.32), drum machine (0.29)
  - stands out: sampled breakbeat (z=+0.5), distorted electric guitar (z=-0.0), 808 bass (z=-0.2), lead synthesizer (z=-0.5), synth bass (z=-0.6)
- **mood** top: dark (0.27), aggressive (0.22), nostalgic (0.21), hypnotic (0.21), uplifting (0.18), sad (0.17)
  - stands out: aggressive (z=-0.5), dark (z=-0.8), epic (z=-1.0), bittersweet (z=-1.2), anxious (z=-1.2)
- **production** top: vintage analog sound (0.28), dense layered arrangement (0.27), lo-fi recording (0.25), distorted and noisy (0.21), minimal sparse arrangement (0.16), heavily compressed (0.12)
  - stands out: distorted and noisy (z=+0.6), dense layered arrangement (z=-0.6), lo-fi recording (z=-0.7), spacious reverb (z=-1.0), vintage analog sound (z=-1.2)
