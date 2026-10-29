🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › A01

# A01 · Sum from 1 to N

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | ⭐ | 4b · Running result | [Counter loop](../cookbook/01-counter-loop.md), [Accumulator](../cookbook/02-accumulator.md) | [L03](L03-count-up-and-down.md) | Custom |

## 🎯 Goal

Give back the sum 1 + 2 + … + n.

## ▶️ Start and check

```bash
./ex start A01     # creates practice/A01_Sum1ToN.cs (never overwrites your work)
./ex check A01     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#5-do-one-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int SumTo(int n)`: input = n, an int (whole number); result = an int (whole number), given back with return.

## 🧪 Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `SumTo(5)` | `15` |
| `SumTo(1)` | `1` |
| `SumTo(10)` | `55` |
| `SumTo(0)` | `0` |

## ⚠️ Edge cases to test

- N = 0 → the loop runs 0 times → sum stays 0.

## 📏 Rules

- Use a loop. No formula `n * (n + 1) / 2` (you can use it to **check** your answer).
- No LINQ and no ready-made helpers: you write every step yourself.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

Fill the trace table for N = 4 first: `i`, `sum before`, `sum after`.

</details>

<details><summary>Hint 2</summary>

The box `sum` is created **before** the loop and starts at 0.

</details>

<details><summary>Hint 3</summary>

Inside the loop: `sum += i;`. `return sum;` **after** the loop.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Sum from A to B (read both). Then: sum of the squares 1² + 2² + … + N².

## 🔑 Solution

Only after a real try: [open the solution for A01](../solutions/A01_Sum1ToN.cs). Your solution can be different and still correct!

---

⬅️ Previous: [L08 · Guess the number](L08-guess-the-number.md) · 📚 [All exercises](README.md) · Next: [A02 · Count multiples of 3](A02-count-multiples-of-3.md) ➡️
