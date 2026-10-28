# R02 · Largest value in an array

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Independent | ⭐⭐ | 6 · Arrays | [Array traversal](../cookbook/11-array-traversal.md), [Min/max](../cookbook/04-min-max.md) | [R01](R01-sum-an-array.md), [C02](C02-largest-of-three.md) | Custom |

## 🎯 Goal

Read numbers into an array (at least 1). Print the largest value and its position (index). Input format: first how many numbers, then one number per line. Fill the array with a loop (see [array traversal](../cookbook/11-array-traversal.md)).

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `3`, `-5`, `-2`, `-9`

```text
Largest: -2 at index 1
```

**Example 2** — input: `5`, `3`, `7`, `2`, `7`, `1`

```text
Largest: 7 at index 1
```

## ⚠️ Edge cases to test

- All negative.
- The max appears twice → give the **first** position.

## 📏 Rules

- No `.Max()`. Start with `values[0]`, not 0.
- No LINQ, no ready-made helpers that do the loop for you. The loop **is** the exercise.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats / what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

Two boxes: `max = values[0]` and `maxIndex = 0`.

</details>

<details><summary>Hint 2</summary>

Loop from index 1. Use `>` (not `>=`) to keep the first position.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Print the second largest value.

## 🔑 Solution

Only after a real try: [R02-largest-in-an-array](../solutions/R02-largest-in-an-array.cs). Your solution can be different and still correct!

⬅️ [Back to the inventory](README.md)
