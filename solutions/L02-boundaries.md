[Home](../README.md) › [Solutions](README.md) › L02

# Answer key · L02 Boundaries: < or <=

| Loop | Runs | Values printed | Last value |
| --- | ---: | --- | ---: |
| A `i < 5` from 1 | 4 | 1 2 3 4 | 4 |
| B `i <= 5` from 1 | 5 | 1 2 3 4 5 | 5 |
| C `i < 5` from 0 | 5 | 0 1 2 3 4 | 4 |
| D `i >= 1` from 5 down | 5 | 5 4 3 2 1 | 1 |
| E `k < 5` with k = 10 | **0** | nothing | — |

Rule of thumb: `for (int i = 0; i < n; i++)` and `for (int i = 1; i <= n; i++)` both run **n** times.

[Back to the exercise](../exercises/L02-boundaries.md)
