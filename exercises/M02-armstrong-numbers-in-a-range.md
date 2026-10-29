🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › M02

# M02 · All Armstrong numbers in a range

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Challenge | ⭐⭐⭐ | 4 · Combine | [Counter loop](../cookbook/01-counter-loop.md), [Digit extraction](../cookbook/06-digit-extraction.md), [Accumulator](../cookbook/02-accumulator.md) | [M01](M01-armstrong-number.md) | Custom |

## 🎯 Goal

Read a lower and an upper bound. Print every Armstrong number between them (both included).

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `100`, `999`

```text
153 370 371 407
```

**Example 2** — input: `1`, `9`

```text
1 2 3 4 5 6 7 8 9
```

**Example 3** — input: `1000`, `9999`

```text
1634 8208 9474
```

## ⚠️ Edge cases to test

- Bounds included.

## 📏 Rules

- Your M01 code inside a counter loop. Beware: the inner variables must be reset for every candidate.
- No LINQ and no ready-made helpers: you write every step yourself.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

Outer loop: `candidate` from `lower` to `upper`.

</details>

<details><summary>Hint 2</summary>

Paste M01 inside and replace `n` by `candidate`.

</details>

<details><summary>Hint 3</summary>

Declare `digits`, `sum`, `remaining` **inside** the outer loop so they restart at 0.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Count how many Armstrong numbers exist below 100000.

## 🔑 Solution

Only after a real try: [open the solution for M02](../solutions/M02-armstrong-numbers-in-a-range.cs). Your solution can be different and still correct!

---

⬅️ Previous: [M01 · Armstrong number](M01-armstrong-number.md) · 📚 [All exercises](README.md) · Next: [R01 · Sum of an array](R01-sum-an-array.md) ➡️
