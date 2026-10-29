🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › L19

# L19 · Count the turns

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | ⭐ | 4a · Repeat & count | [Counter loop](../cookbook/01-counter-loop.md), [Accumulator](../cookbook/02-accumulator.md) | [L11](L11-count-from-a-to-b.md) | Custom |

## 🎯 Goal

Give back how many times a loop from `a` to `b` (both included) runs. Count with a loop, not with a formula.

## ▶️ Start and check

```bash
./ex start L19     # creates practice/L19_CountTheTurns.cs (never overwrites your work)
./ex check L19     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#5-do-one-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int CountTurns(int a, int b)`: input = a, an int (whole number), b, an int (whole number); result = an int (whole number), given back with return.

## 🧪 Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `CountTurns(1, 5)` | `5` |
| `CountTurns(3, 3)` | `1` |
| `CountTurns(4, 10)` | `7` |
| `CountTurns(5, 4)` | `0` |

## ⚠️ Edge cases to test

- `a` bigger than `b`: 0 turns.

## 📏 Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

A counter box `turns = 0` before the loop.

</details>

<details><summary>Hint 2</summary>

`turns++` inside the loop, `return turns;` after it.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

How many turns does a loop from `a` to `b` with step 2 do?

## 🔑 Solution

Only after a real try: [open the solution for L19](../solutions/L19_CountTheTurns.cs). Your solution can be different and still correct!

---

⬅️ Previous: [L18 · Square numbers](L18-squares.md) · 📚 [All exercises](README.md) · Next: [A11 · Arrange the lines: sum of squares](A11-arrange-sum-of-squares.md) ➡️
