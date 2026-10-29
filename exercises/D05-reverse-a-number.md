🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › D05

# D05 · Reverse a number

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Independent | ⭐⭐ | 4d · Digits | [Digit extraction](../cookbook/06-digit-extraction.md) | [D04](D04-digit-sum.md) | Custom |

## 🎯 Goal

Give back n with its digits in reverse order (n ≥ 0): 352 → 253.

## ▶️ Start and check

```bash
./ex start D05     # creates practice/D05_ReverseANumber.cs (never overwrites your work)
./ex check D05     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#5-do-one-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int ReverseNumber(int n)`: input = n, an int (whole number); result = an int (whole number), given back with return.

## 🧪 Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `ReverseNumber(352)` | `253` |
| `ReverseNumber(1200)` | `21` |
| `ReverseNumber(0)` | `0` |
| `ReverseNumber(7)` | `7` |

## ⚠️ Edge cases to test

- Trailing zeros disappear (1200 → 21).

## 📏 Rules

- Build an `int`, not a string.
- No LINQ and no ready-made helpers: you write every step yourself.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

The digits come out in the order 2, 5, 3. That is already the reversed order!

</details>

<details><summary>Hint 2</summary>

To add a digit at the right of a number: `reversed * 10 + digit`.

</details>

<details><summary>Hint 3</summary>

Trace: 0 → 2 → 25 → 253.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Explain why 1200 → 21 and not 0021.

## 🔑 Solution

Only after a real try: [open the solution for D05](../solutions/D05_ReverseANumber.cs). Your solution can be different and still correct!

---

⬅️ Previous: [D07 · Fix the bugs: digit sum](D07-fix-digit-sum.md) · 📚 [All exercises](README.md) · Next: [D06 · Palindrome number](D06-palindrome-number.md) ➡️
