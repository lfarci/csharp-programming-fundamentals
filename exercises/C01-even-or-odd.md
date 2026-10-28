# C01 · Even or odd

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | ⭐ | 3 · Conditions | — | [B02](B02-rectangle-calculator.md) | Custom |

## 🎯 Goal

Read a whole number and say if it is even or odd.

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `7`

```text
7 is odd
```

**Example 2** — input: `0`

```text
0 is even
```

**Example 3** — input: `-4`

```text
-4 is even
```

## ⚠️ Edge cases to test

- 0 is even.
- Negative numbers: `-3 % 2` is `-1`, not `1`!

## 📏 Rules

- Use `%` and `if`/`else`.
- No LINQ, no ready-made helpers that do the loop for you. The loop **is** the exercise.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats / what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

A number is even when the remainder of the division by 2 is 0.

</details>

<details><summary>Hint 2</summary>

`if (n % 2 == 0) { ... } else { ... }`

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Say if a number is a multiple of 3, of 5, of both, or of none.

## 🔑 Solution

Only after a real try: [C01-even-or-odd](../solutions/C01-even-or-odd.cs). Your solution can be different and still correct!

⬅️ [Back to the inventory](README.md)
