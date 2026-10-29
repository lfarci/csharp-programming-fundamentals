[Home](../README.md) › [Solutions](README.md) › L01

# Answer key · L01 Trace a loop

| Turn | `i` at start | `i <= 8`? | Output | `i` after step |
| ---: | ---: | --- | ---: | ---: |
| 1 | 2 | yes | 2 | 4 |
| 2 | 4 | yes | 4 | 6 |
| 3 | 6 | yes | 6 | 8 |
| 4 | 8 | yes | 8 | 10 |
| — | 10 | **no** → stop | | |

Output: `2 4 6 8` (one per line). The loop stops with `i = 10`, which is **not** printed.

Mastery check: `10 7 4 1` (then `i = -2`, test `-2 > 0` is false).

[Back to the exercise](../exercises/L01-trace-a-loop.md)
