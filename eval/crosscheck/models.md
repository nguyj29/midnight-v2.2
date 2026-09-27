# Leave-one-out cross-check models

Target = anchored score (see labeled_scores.csv). Ridge with standardised features; alpha chosen by internal CV inside each training fold. Tier accuracy maps predicted score to a tier via band midpoints.

| model | Spearman (LOO) | exact tier | within one tier | MAE (points) |
|---|---|---|---|---|
| ridge_all7 | -0.89 (p=0.00) | 39% | 83% | 25.8 |
| ridge_music6 (no LUFS) | -0.86 (p=0.00) | 33% | 100% | 23.4 |
| lufs_only | -0.94 (p=0.00) | 39% | 100% | 22.0 |
| clap_knn3 | -0.29 (p=0.25) | 17% | 83% | 27.4 |

## Ridge coefficients (all labelled data, per 1 SD of feature)

- ridge_all7 (alpha 615.8): {'pulse_clarity': -0.02, 'harmonic_richness': -0.31, 'dynamic_contrast_db': 0.24, 'section_variety': 0.04, 'melody_presence': -0.09, 'tempo_bpm': -0.11, 'integrated_lufs': 0.17}
- ridge_music6 (no LUFS) (alpha 233.6): {'pulse_clarity': -0.03, 'harmonic_richness': -0.77, 'dynamic_contrast_db': 0.57, 'section_variety': 0.1, 'melody_presence': -0.22, 'tempo_bpm': -0.28}

## Single-feature Spearman correlation with anchored score (n=18)

- pulse_clarity: rho -0.08 (p=0.744) — beat-tracker activation at beats (groove definiteness)
- harmonic_richness: rho -0.50 (p=0.034) — share of bars whose fitted chord is a 7th/9th/6th/sus/dim (not plain triad/power)
- dynamic_contrast_db: rho +0.41 (p=0.088) — per-bar loudness p90 - p10 (arrangement dynamics)
- section_variety: rho -0.09 (p=0.719) — distinct section letters
- melody_presence: rho +0.00 (p=0.990) — share of bars with a skyline melody
- tempo_bpm: rho -0.09 (p=0.717) — median tempo
- integrated_lufs: rho +0.17 (p=0.496) — mastering loudness (confound probe)
