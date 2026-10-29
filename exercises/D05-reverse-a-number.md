🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › D05

# D05 · Reverse a number

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Independent | ⭐⭐ | 4d · Digits | [Digit extraction](../cookbook/06-digit-extraction.md) | [D04](D04-digit-sum.md) | Custom |

## 🎯 Goal

Read N ≥ 0. Print the number with its digits in reverse order.

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `352`

```text
Reversed: 253
```

**Example 2** — input: `1200`

```text
Reversed: 21
```

**Example 3** — input: `0`

```text
Reversed: 0
```

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

Only after a real try: [open the solution for D05](../solutions/D05-reverse-a-number.cs). Your solution can be different and still correct!

---

⬅️ Previous: [D04 · Sum of the digits](D04-digit-sum.md) · 📚 [All exercises](README.md) · Next: [D06 · Palindrome number](D06-palindrome-number.md) ➡️
