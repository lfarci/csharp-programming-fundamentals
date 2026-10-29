🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › C01

# C01 · Even or odd

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | ⭐ | 3 · Conditions | — | [B02](B02-rectangle-calculator.md) | Custom |

## 🎯 Goal

Give back `true` if `n` is even, `false` if it is odd.

## ▶️ Start and check

```bash
./ex start C01     # creates practice/C01_EvenOrOdd.cs (never overwrites your work)
./ex check C01     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#5-do-one-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `bool IsEven(int n)`: input = n, an int (whole number); result = a bool (true or false), given back with return.

## 🧪 Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `IsEven(7)` | `false` |
| `IsEven(0)` | `true` |
| `IsEven(-4)` | `true` |
| `IsEven(-3)` | `false` |

## ⚠️ Edge cases to test

- 0 is even.
- Negative numbers: `-3 % 2` is `-1`, not `1`!

## 📏 Rules

- Use `%` and `if`/`else`.
- No LINQ and no ready-made helpers: you write every step yourself.

## 🗺️ Before coding

Fill the [reading worksheet](../docs/reading-an-exercise.md#4-the-worksheet-copy-it): what goes in? what comes out? a tiny example by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

A number is even when the remainder of the division by 2 is 0.

</details>

<details><summary>Hint 2</summary>

`if (n % 2 == 0) { ... } else { ... }`

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Say if a number is a multiple of 3, of 5, of both, or of none.

## 🔑 Solution

Only after a real try: [open the solution for C01](../solutions/C01_EvenOrOdd.cs). Your solution can be different and still correct!

---

⬅️ Previous: [B03 · Seconds to hours, minutes, seconds](B03-seconds-to-hms.md) · 📚 [All exercises](README.md) · Next: [C02 · Largest of three](C02-largest-of-three.md) ➡️
