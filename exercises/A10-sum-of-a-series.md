🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › A10

# A10 · Sum of a series

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Challenge | ⭐⭐ | 4b · Running result | [Accumulator](../cookbook/02-accumulator.md) | [A01](A01-sum-1-to-n.md) | Custom |

## 🎯 Goal

Give back the sum 1 + 1/2 + 1/3 + … + 1/n as a `double`.

## ▶️ Start and check

```bash
./ex start A10     # creates practice/A10_SumOfASeries.cs (never overwrites your work)
./ex check A10     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#5-do-one-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `double SeriesSum(int n)`: input = n, an int (whole number); result = a double (decimal number), given back with return.

## 🧪 Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `SeriesSum(1)` | `1.0000`… |
| `SeriesSum(2)` | `1.5000`… |
| `SeriesSum(4)` | `2.0833`… |

> ℹ️ On a French/Dutch computer the output is `2,0833`. That is fine.

## ⚠️ Edge cases to test

- `1 / 2` with two `int`s is **0**! Use `1.0 / i`.

## 📏 Rules

- A loop with a `double` box.
- No LINQ and no ready-made helpers: you write every step yourself.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

The box is a `double` that starts at 0.

</details>

<details><summary>Hint 2</summary>

Each turn adds `1.0 / i`.

</details>

<details><summary>Hint 3</summary>

`1 / i` with two `int`s is 0! Write `1.0 / i` to get a `double` division.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Compute 1 − 1/2 + 1/3 − 1/4 + … (the sign changes every turn). Hint: a `sign` box that flips with `sign = -sign`.

## 🔑 Solution

Only after a real try: [open the solution for A10](../solutions/A10_SumOfASeries.cs). Your solution can be different and still correct!

---

⬅️ Previous: [A09 · Smallest and largest until zero](A09-min-and-max-until-zero.md) · 📚 [All exercises](README.md) · Next: [G01 · Draw a rectangle](G01-rectangle.md) ➡️
