🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › R01

# R01 · Sum of an array

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | ⭐ | 6 · Arrays | [Array traversal](../cookbook/11-array-traversal.md), [Accumulator](../cookbook/02-accumulator.md) | [A01](A01-sum-1-to-n.md) | Custom |

## 🎯 Goal

Give back the sum of all values in the array.

## ▶️ Start and check

```bash
./ex start R01     # creates practice/R01_SumAnArray.cs (never overwrites your work)
./ex check R01     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#5-do-one-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int Sum(int[] values)`: input = values, an int[] (array of whole numbers); result = an int (whole number), given back with return.

## 🧪 Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `Sum(new int[] { 4, 9, 2 })` | `15` |
| `Sum(new int[] { -5 })` | `-5` |
| `Sum(new int[0])` | `0` |

## ⚠️ Edge cases to test

- An empty array (0 numbers) → 0.

## 📏 Rules

- One loop over the array. No LINQ (`.Sum()`).
- No LINQ and no ready-made helpers: you write every step yourself.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

Indexes go from 0 to `values.Length - 1`.

</details>

<details><summary>Hint 2</summary>

Sum it with `foreach (int value in values)`.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Print the sum of the values at **even positions** (0, 2, 4…).

## 🔑 Solution

Only after a real try: [open the solution for R01](../solutions/R01_SumAnArray.cs). Your solution can be different and still correct!

---

⬅️ Previous: [M02 · All Armstrong numbers in a range](M02-armstrong-numbers-in-a-range.md) · 📚 [All exercises](README.md) · Next: [R02 · Largest value in an array](R02-largest-in-an-array.md) ➡️
