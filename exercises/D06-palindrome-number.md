🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › D06

# D06 · Palindrome number

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Challenge | ⭐⭐⭐ | 4d · Digits | [Digit extraction](../cookbook/06-digit-extraction.md) | [D05](D05-reverse-a-number.md) | Custom |

## 🎯 Goal

Give back `true` if n reads the same in both directions (n ≥ 0).

## ▶️ Start and check

```bash
./ex start D06     # creates practice/D06_PalindromeNumber.cs (never overwrites your work)
./ex check D06     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#5-do-one-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `bool IsPalindrome(int n)`: input = n, an int (whole number); result = a bool (true or false), given back with return.

## 🧪 Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `IsPalindrome(1221)` | `true` |
| `IsPalindrome(123)` | `false` |
| `IsPalindrome(7)` | `true` |
| `IsPalindrome(0)` | `true` |
| `IsPalindrome(10)` | `false` |

## ⚠️ Edge cases to test

- One digit → palindrome.
- Keep the original `n` to compare at the end!

## 📏 Rules

- No string. Reuse D05.
- No LINQ and no ready-made helpers: you write every step yourself.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

Palindrome ⇔ the reversed number equals the original.

</details>

<details><summary>Hint 2</summary>

Work on a copy `remaining`, so `n` is still there at the end.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Find all palindrome numbers between 100 and 200.

## 🔑 Solution

Only after a real try: [open the solution for D06](../solutions/D06_PalindromeNumber.cs). Your solution can be different and still correct!

---

⬅️ Previous: [D05 · Reverse a number](D05-reverse-a-number.md) · 📚 [All exercises](README.md) · Next: [S01 · Trace two changing variables (paper)](S01-trace-updates.md) ➡️
