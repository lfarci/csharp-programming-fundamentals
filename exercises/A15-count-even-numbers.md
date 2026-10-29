🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › A15

# A15 · Count the even numbers

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | ⭐ | 4b · Running result | [Conditional accumulator](../cookbook/03-conditional-accumulator.md) | [A02](A02-count-multiples-of-3.md) | Custom |

## 🎯 Goal

Give back how many numbers from 1 to n are even.

## ▶️ Start and check

```bash
./ex start A15     # creates practice/A15_CountEvenNumbers.cs (never overwrites your work)
./ex check A15     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#5-do-one-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int CountEvens(int n)`: input = n, an int (whole number); result = an int (whole number), given back with return.

## 🧪 Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `CountEvens(10)` | `5` |
| `CountEvens(7)` | `3` |
| `CountEvens(1)` | `0` |

## ⚠️ Edge cases to test

- n = 1: 0.

## 📏 Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

Like A02: only the test changes.

</details>

<details><summary>Hint 2</summary>

`if (i % 2 == 0) count++;`

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Count the odd numbers from 1 to n.

## 🔑 Solution

Only after a real try: [open the solution for A15](../solutions/A15_CountEvenNumbers.cs). Your solution can be different and still correct!

---

⬅️ Previous: [A14 · Sum the odd numbers](A14-sum-odd-numbers.md) · 📚 [All exercises](README.md) · Next: [A16 · Count multiples of 5](A16-count-multiples-of-5.md) ➡️
