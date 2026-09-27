## Validation metrics

| metric | value |
|---|---|
| n | 18 |
| tier_accuracy | 1.0 |
| within_one_tier | 1.0 |
| spearman_rho | 0.9959 |
| spearman_p | 4.185e-18 |
| kendall_tau | 0.9739 |
| kendall_p | 5.311e-14 |
| range80_coverage | 1.0 |
| mean_range_width | 19.667 |
| mae_points | 2.6 |

## Per track

| id | true pos | true score | pred tier | pred score | 80% range | position | pos score | tier | range | abs err |
|---|---|---|---|---|---|---|---|---|---|---|
| t68bc6fa5 | S1 | 98.0 | S | 91.0 | 82.0-98.0 | between S3 and S4 | 91.3 | hit | hit | 7.0 |
| t8aca41eb | S2 | 95.3 | S | 90.0 | 82.0-98.0 | between S3 and S4 | 91.3 | hit | hit | 5.3 |
| t5fe4a915 | S3 | 92.7 | S | 88.0 | 80.0-97.0 | between S4 and S5 | 88.7 | hit | hit | 4.7 |
| t0d513ac8 | S4 | 90.0 | S | 86.0 | 78.0-95.0 | between S5 and S6 | 86.0 | hit | hit | 4.0 |
| t77478144 | S5 | 87.3 | S | 83.0 | 72.0-92.0 | between S6 and S7 | 83.3 | hit | hit | 4.3 |
| t9d4d0c39 | S6 | 84.7 | S | 85.0 | 77.0-93.0 | between S5 and S7 | 84.7 | hit | hit | 0.3 |
| tc8f1d0c8 | S7 | 82.0 | S | 80.0 | 70.0-90.0 | between S6 and A1 in S | 83.3 | hit | hit | 2.0 |
| tac555977 | A1 | 74.0 | A | 72.0 | 62.0-82.0 | above A2 | 78.0 | hit | hit | 2.0 |
| t9fb064e8 | A2 | 70.3 | A | 70.0 | 60.0-80.0 | between A1 and A3 | 70.3 | hit | hit | 0.3 |
| t94fd0413 | A3 | 66.7 | A | 67.0 | 57.0-77.0 | between A2 and A4 | 66.7 | hit | hit | 0.3 |
| t3b9d70c1 | A4 | 63.0 | A | 60.0 | 50.0-70.0 | between A5 and A6 | 57.5 | hit | hit | 3.0 |
| tde35730e | A5 | 59.3 | A | 55.0 | 42.0-68.0 | between A6 and A7 | 53.9 | hit | hit | 4.3 |
| td231b399 | A6 | 55.7 | A | 56.0 | 46.0-66.0 | between A5 and A7 | 55.6 | hit | hit | 0.3 |
| t21aaeadf | A7 | 52.0 | A | 51.0 | 40.0-62.0 | between A6 and B1 in A | 53.9 | hit | hit | 1.0 |
| t61233098 | B1 | 44.0 | B | 40.0 | 30.0-52.0 | between A7 and B2 in B | 38.6 | hit | hit | 4.0 |
| ted20dc6f | B2 | 33.3 | B | 34.0 | 24.0-48.0 | between B1 and B3 | 33.4 | hit | hit | 0.7 |
| tb20bad3c | B3 | 22.7 | B | 26.0 | 16.0-38.0 | between B2 and B4 | 22.6 | hit | hit | 3.3 |
| t8d54bfc3 | B4 | 12.0 | B | 12.0 | 6.0-22.0 | below B3 | 20.6 | hit | hit | 0.0 |

## Tier confusion (rows = true, cols = predicted)

| true \ pred | S | A | B |
|---|---|---|---|
| S | 7 | 0 | 0 |
| A | 0 | 7 | 0 |
| B | 0 | 0 | 4 |
