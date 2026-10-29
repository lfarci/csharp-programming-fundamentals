🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › A02

# A02 · Count multiples of 3

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | ⭐ | 4b · Running result | [Conditional accumulator](../cookbook/03-conditional-accumulator.md) | [A01](A01-sum-1-to-n.md), [C01](C01-even-or-odd.md) | Custom |

## 🎯 Goal

Read N. Count how many numbers from 1 to N (included) are divisible by 3.

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `10`

```text
Count: 3
```

**Example 2** — input: `2`

```text
Count: 0
```

**Example 3** — input: `9`

```text
Count: 3
```

## ⚠️ Edge cases to test

- N smaller than 3 → 0.
- N itself divisible by 3 → counted.

## 📏 Rules

- Loop + `if` + counter. No division trick (`n / 3`) except to check.
- No LINQ and no ready-made helpers: you write every step yourself.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

Divisible by 3: `i % 3 == 0`.

</details>

<details><summary>Hint 2</summary>

Box: `count = 0`, `count++` only when the `if` is true.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Count the numbers from 1 to N that are divisible by 3 **but not** by 2.

## 🔑 Solution

Only after a real try: [open the solution for A02](../solutions/A02-count-multiples-of-3.cs). Your solution can be different and still correct!

---

⬅️ Previous: [A01 · Sum from 1 to N](A01-sum-1-to-n.md) · 📚 [All exercises](README.md) · Next: [A03 · Sum of the even numbers](A03-sum-even-values.md) ➡️
