🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › B03

# B03 · Seconds to hours, minutes, seconds

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Independent | ⭐⭐ | 2 · Variables & expressions | — | [B02](B02-rectangle-calculator.md) | Custom |

## 🎯 Goal

Turn a number of seconds into text like `1 h 2 min 5 s`. This trains `/` and `%`, the key tools of the digit recipe later.

## ▶️ Start and check

```bash
./ex start B03     # creates practice/B03_SecondsToHms.cs (never overwrites your work)
./ex check B03     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#5-do-one-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `string Format(int totalSeconds)`: input = totalSeconds, an int (whole number); result = a string (text), given back with return.

## 🧪 Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `Format(3725)` | `"1 h 2 min 5 s"` |
| `Format(59)` | `"0 h 0 min 59 s"` |
| `Format(7200)` | `"2 h 0 min 0 s"` |
| `Format(0)` | `"0 h 0 min 0 s"` |

## ⚠️ Edge cases to test

- 0 seconds → `0 h 0 min 0 s`.

## 📏 Rules

- No loop, no `if`. Only `/` and `%` on `int`.
- No LINQ and no ready-made helpers: you write every step yourself.

## 🗺️ Before coding

Fill the [reading worksheet](../docs/reading-an-exercise.md#4-the-worksheet-copy-it): what goes in? what comes out? a tiny example by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

1 hour = 3600 seconds. `3725 / 3600` is 1 (integer division drops the rest).

</details>

<details><summary>Hint 2</summary>

What is left after the hours? `3725 % 3600` = 125.

</details>

<details><summary>Hint 3</summary>

Then do the same with 60 on what is left: 125 / 60 = 2 minutes, 125 % 60 = 5 seconds.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Turn a number of days into weeks and days (`17` → `2 weeks 3 days`).

## 🔑 Solution

Only after a real try: [open the solution for B03](../solutions/B03_SecondsToHms.cs). Your solution can be different and still correct!

---

⬅️ Previous: [B02 · Rectangle calculator](B02-rectangle-calculator.md) · 📚 [All exercises](README.md) · Next: [C01 · Even or odd](C01-even-or-odd.md) ➡️
