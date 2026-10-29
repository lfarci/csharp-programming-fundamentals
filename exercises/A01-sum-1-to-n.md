🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › A01

# A01 · Sum from 1 to N

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | ⭐ | 4b · Running result | [Counter loop](../cookbook/01-counter-loop.md), [Accumulator](../cookbook/02-accumulator.md) | [L03](L03-count-up-and-down.md) | Custom |

## 🎯 Goal

Read N and print the sum 1 + 2 + … + N.

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `5`

```text
Sum: 15
```

**Example 2** — input: `1`

```text
Sum: 1
```

**Example 3** — input: `10`

```text
Sum: 55
```

**Example 4** — input: `0`

```text
Sum: 0
```

## ⚠️ Edge cases to test

- N = 0 → the loop runs 0 times → sum stays 0.

## 📏 Rules

- Use a loop. No formula `n * (n + 1) / 2` (you can use it to **check** your answer).
- No LINQ and no ready-made helpers: you write every step yourself.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

Fill the trace table for N = 4 first: `i`, `sum before`, `sum after`.

</details>

<details><summary>Hint 2</summary>

The box `sum` is created **before** the loop and starts at 0.

</details>

<details><summary>Hint 3</summary>

Inside the loop: `sum += i;`. Print **after** the loop.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Sum from A to B (read both). Then: sum of the squares 1² + 2² + … + N².

## 🔑 Solution

Only after a real try: [open the solution for A01](../solutions/A01-sum-1-to-n.cs). Your solution can be different and still correct!

---

⬅️ Previous: [L08 · Guess the number](L08-guess-the-number.md) · 📚 [All exercises](README.md) · Next: [A02 · Count multiples of 3](A02-count-multiples-of-3.md) ➡️
