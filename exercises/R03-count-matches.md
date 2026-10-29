🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › R03

# R03 · Count matches in an array

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Independent | ⭐ | 6 · Arrays | [Array traversal](../cookbook/11-array-traversal.md), [Conditional accumulator](../cookbook/03-conditional-accumulator.md) | [R01](R01-sum-an-array.md), [A02](A02-count-multiples-of-3.md) | Custom |

## 🎯 Goal

Read numbers into an array, then a target value. Print how many times the target appears. Input format: first how many numbers, then one number per line. Fill the array with a loop (see [array traversal](../cookbook/11-array-traversal.md)). The last line is the target.

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `5`, `2`, `4`, `2`, `5`, `2`, `2`

```text
2 appears 3 times
```

**Example 2** — input: `2`, `1`, `1`, `9`

```text
9 appears 0 times
```

## ⚠️ Edge cases to test

- Target not present → 0.

## 📏 Rules

- No LINQ (`.Count()`).
- No LINQ and no ready-made helpers: you write every step yourself.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

First read the array like in R01. Then read the target. Which recipe counts only *some* values?

</details>

<details><summary>Hint 2</summary>

Conditional accumulator: `if (value == target) count++;`

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Count the values **greater** than the target.

## 🔑 Solution

Only after a real try: [open the solution for R03](../solutions/R03-count-matches.cs). Your solution can be different and still correct!

---

⬅️ Previous: [R02 · Largest value in an array](R02-largest-in-an-array.md) · 📚 [All exercises](README.md) · Next: [R04 · Find the position](R04-find-the-position.md) ➡️
