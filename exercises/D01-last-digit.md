🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › D01

# D01 · Last digit

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | ⭐ | 4d · Digits | [Digit extraction](../cookbook/06-digit-extraction.md) | [B03](B03-seconds-to-hms.md) | Custom |

## 🎯 Goal

Give back the last digit of n (n ≥ 0).

## ▶️ Start and check

```bash
./ex start D01     # creates practice/D01_LastDigit.cs (never overwrites your work)
./ex check D01     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#5-do-one-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int LastDigit(int n)`: input = n, an int (whole number); result = an int (whole number), given back with return.

## 🧪 Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `LastDigit(352)` | `2` |
| `LastDigit(7)` | `7` |
| `LastDigit(0)` | `0` |
| `LastDigit(90)` | `0` |

## ⚠️ Edge cases to test

- One-digit number → the number itself.

## 📏 Rules

- No string. Use `%`.
- No LINQ and no ready-made helpers: you write every step yourself.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

What is the remainder of 352 divided by 10? Do it on paper first.

</details>

<details><summary>Hint 2</summary>

The remainder operator is `%`: `352 % 10` gives `2`. No loop is needed here.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Print the **second to last** digit (352 → 5).

## 🔑 Solution

Only after a real try: [open the solution for D01](../solutions/D01_LastDigit.cs). Your solution can be different and still correct!

---

⬅️ Previous: [G06 · Pyramid](G06-pyramid.md) · 📚 [All exercises](README.md) · Next: [D02 · Remove the last digit](D02-remove-last-digit.md) ➡️
