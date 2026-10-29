🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › M01

# M01 · Armstrong number

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Challenge | ⭐⭐⭐ | 4 · Combine | [Digit extraction](../cookbook/06-digit-extraction.md), [Accumulator](../cookbook/02-accumulator.md) | [D03](D03-count-digits.md), [D04](D04-digit-sum.md), [A07](A07-integer-power.md) | Custom · teacher topic: Armstrong |

## 🎯 Goal

Read N ≥ 0. An Armstrong number equals the sum of its digits, each raised to the power **number of digits**. Say if N is one.

153 → 3 digits → 1³ + 5³ + 3³ = 153 ✅. 9474 → 4 digits → 9⁴ + 4⁴ + 7⁴ + 4⁴ = 9474 ✅.

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `153`

```text
153 is an Armstrong number
```

**Example 2** — input: `154`

```text
154 is not an Armstrong number
```

**Example 3** — input: `9474`

```text
9474 is an Armstrong number
```

**Example 4** — input: `0`

```text
0 is an Armstrong number
```

**Example 5** — input: `10`

```text
10 is not an Armstrong number
```

## ⚠️ Edge cases to test

- Every 1-digit number is an Armstrong number (5¹ = 5).
- The power is the number of digits, **not always 3**.

## 📏 Rules

- No string, no `Math.Pow`. Reuse D03 (count), D04 (digits) and A07 (power).
- No LINQ and no ready-made helpers: you write every step yourself.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

Cut the problem: (1) count the digits, (2) for each digit, (3) compute digit^count, (4) add, (5) compare. See [Combining recipes](../cookbook/combining-recipes.md).

</details>

<details><summary>Hint 2</summary>

Step (1) empties your copy. Make a **new** copy of `n` for step (2).

</details>

<details><summary>Hint 3</summary>

The power is a small product loop **inside** the digit loop: `power = 1; for (i = 0; i < digits; i++) power *= digit;`

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Solve it again from a blank file two days later, without looking.

## 🔑 Solution

Only after a real try: [open the solution for M01](../solutions/M01-armstrong-number.cs). Your solution can be different and still correct!

---

⬅️ Previous: [P02 · All primes up to N](P02-primes-up-to-n.md) · 📚 [All exercises](README.md) · Next: [M02 · All Armstrong numbers in a range](M02-armstrong-numbers-in-a-range.md) ➡️
