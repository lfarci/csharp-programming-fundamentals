🏠 [Home](../README.md) › 🔑 [Solutions](README.md) › S01

# Answer key · S01 Trace two changing variables (paper)

| Turn | `next` | `a` after | `b` after | Output |
| ---: | ---: | ---: | ---: | --- |
| 1 | 3 | 2 | 3 | `a=2 b=3` |
| 2 | 5 | 3 | 5 | `a=3 b=5` |
| 3 | 8 | 5 | 8 | `a=5 b=8` |

With the lines swapped (`b = next; a = b;`): turn 1 → b = 3, then a = 3 (the **new** b!). Output `a=3 b=3`, then `a=6 b=6`, `a=12 b=12`. The old value of `b` was lost.

Mastery check: `a` and `b` go through 1 1, 1 2, 2 3, 3 5, 5 8, 8 13 → it is the **Fibonacci** sequence.

⬅️ [Back to the exercise](../exercises/S01-trace-updates.md)
