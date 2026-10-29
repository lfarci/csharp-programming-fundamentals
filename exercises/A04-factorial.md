🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › A04

# A04 · Factorial

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Independent | ⭐⭐ | 4b · Running result | [Accumulator](../cookbook/02-accumulator.md) | [A01](A01-sum-1-to-n.md) | Custom · teacher topic: Factorial |

## 🎯 Goal

Read N (0 ≤ N ≤ 20) and print N! = 1 × 2 × … × N. By definition 0! = 1.

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `5`

```text
5! = 120
```

**Example 2** — input: `0`

```text
0! = 1
```

**Example 3** — input: `12`

```text
12! = 479001600
```

**Example 4** — input: `20`

```text
20! = 2432902008176640000
```

## ⚠️ Edge cases to test

- N = 0 → 1 (the loop runs 0 times, the box keeps its start value).
- 13! does not fit in an `int` → use `long`.

## 📏 Rules

- A loop, no recursion, no library.
- No LINQ and no ready-made helpers: you write every step yourself.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

Trace 4! on paper: 1 → 1 → 2 → 6 → 24.

</details>

<details><summary>Hint 2</summary>

Product box. What must it start at? (Not 0!)

</details>

<details><summary>Hint 3</summary>

`long product = 1; for (int i = 1; i <= n; i++) product *= i;`

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Print every factorial from 0! to N! (one per line), with **one** loop.

## 🔑 Solution

Only after a real try: [open the solution for A04](../solutions/A04-factorial.cs). Your solution can be different and still correct!

---

⬅️ Previous: [A03 · Sum of the even numbers](A03-sum-even-values.md) · 📚 [All exercises](README.md) · Next: [A05 · Two accumulators: sum and squares](A05-sum-square-difference.md) ➡️
