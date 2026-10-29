🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › A02

# A02 · Count multiples of 3

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | ⭐ | 4b · Running result | [Conditional accumulator](../cookbook/03-conditional-accumulator.md) | [A01](A01-sum-1-to-n.md), [C01](C01-even-or-odd.md) | Custom |

## 🎯 Goal

Count how many numbers from 1 to n (included) are divisible by 3.

## ▶️ Start and check

```bash
./ex start A02     # creates practice/A02_CountMultiplesOf3.cs (never overwrites your work)
./ex check A02     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#5-do-one-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int CountMultiplesOf3(int n)`: input = n, an int (whole number); result = an int (whole number), given back with return.

## 🧪 Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `CountMultiplesOf3(10)` | `3` |
| `CountMultiplesOf3(2)` | `0` |
| `CountMultiplesOf3(9)` | `3` |
| `CountMultiplesOf3(0)` | `0` |

## ⚠️ Edge cases to test

- N smaller than 3 → 0.
- N itself divisible by 3 → counted.

## 📏 Rules

- Loop + `if` + counter. No division trick (`n / 3`) except to check.
- No LINQ and no ready-made helpers: you write every step yourself.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

Divisible by 3: `i % 3 == 0`.

</details>

<details><summary>Hint 2</summary>

Box: `count = 0`, `count++` only when the `if` is true.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Count the numbers from 1 to N that are divisible by 3 **but not** by 2.

## 🔑 Solution

Only after a real try: [open the solution for A02](../solutions/A02_CountMultiplesOf3.cs). Your solution can be different and still correct!

---

⬅️ Previous: [A01 · Sum from 1 to N](A01-sum-1-to-n.md) · 📚 [All exercises](README.md) · Next: [A12 · Fix the bugs: count multiples of 7](A12-fix-count-multiples-of-7.md) ➡️
