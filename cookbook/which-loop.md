[Home](../README.md) › [Cookbook](README.md) › Which loop?

# Which loop should I use?

A loop is a tool. First say **what repeats** and **what makes it stop**. Then pick the loop.

![Which loop should I use? Visit every item of an array, a list or a string: foreach if you only need the values, for with i if you need the position. Otherwise, if you know the number of turns before the loop starts: for. If not, and the body must run at least once: do while; else while.](../diagrams/which-loop.svg)

| Loop | Use it when… | Typical exercise |
| --- | --- | --- |
| `for` | you know the number of turns (from 1 to N, `width` stars) | sum 1 to N, factorial, a multiplication table |
| `while` | you stop when something changes, maybe after **zero** turns | digits (`while (n > 0)`), Fibonacci up to a limit |
| `do … while` | you must do it **once** before you can check | ask for input until it is valid, menus |
| `foreach` | you visit every item and do not need its position | sum of an array, count letters in a string |

These are good defaults, not laws: every `for` can be written as a `while`.

---

[Cookbook](README.md) · Next: [Combining recipes](combining-recipes.md)
