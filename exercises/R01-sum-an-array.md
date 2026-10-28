# R01 · Sum of an array

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | ⭐ | 6 · Arrays | [Array traversal](../cookbook/11-array-traversal.md), [Accumulator](../cookbook/02-accumulator.md) | [A01](A01-sum-1-to-n.md) | Custom |

## 🎯 Goal

Read numbers into an array, then print their sum. Input format: first how many numbers, then one number per line. Fill the array with a loop (see [array traversal](../cookbook/11-array-traversal.md)).

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `3`, `4`, `9`, `2`

```text
Sum: 15
```

**Example 2** — input: `1`, `-5`

```text
Sum: -5
```

**Example 3** — input: `0`

```text
Sum: 0
```

## ⚠️ Edge cases to test

- An empty array (0 numbers) → 0.

## 📏 Rules

- Two loops: one to fill the array, one to sum it. No LINQ (`.Sum()`).
- No LINQ, no ready-made helpers that do the loop for you. The loop **is** the exercise.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats / what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

Indexes go from 0 to `values.Length - 1`.

</details>

<details><summary>Hint 2</summary>

Sum it with `foreach (int value in values)`.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Print the sum of the values at **even positions** (0, 2, 4…).

## 🔑 Solution

Only after a real try: [R01-sum-an-array](../solutions/R01-sum-an-array.cs). Your solution can be different and still correct!

⬅️ [Back to the inventory](README.md)
