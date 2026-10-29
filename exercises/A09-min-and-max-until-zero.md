🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › A09

# A09 · Smallest and largest until zero

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Independent | ⭐⭐ | 4b · Running result | [Sentinel loop](../cookbook/10-sentinel-loop.md), [Min/max](../cookbook/04-min-max.md) | [A06](A06-average-until-zero.md), [C02](C02-largest-of-three.md) | Custom |

## 🎯 Goal

Read whole numbers until 0. Print the smallest and the largest. If no number was entered, print `No numbers.`

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `4`, `-2`, `9`, `0`

```text
Min: -2
Max: 9
```

**Example 2** — input: `-5`, `-3`, `0`

```text
Min: -5
Max: -3
```

**Example 3** — input: `0`

```text
No numbers.
```

## ⚠️ Edge cases to test

- Only negative numbers → max must not be 0!
- Only one number → min = max.

## 📏 Rules

- No array, no list.
- No LINQ and no ready-made helpers: you write every step yourself.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

What do `min` and `max` start at? Not 0. Idea: the first value read.

</details>

<details><summary>Hint 2</summary>

Use a counter: when `count == 1`, set both `min` and `max` to the value.

</details>

<details><summary>Hint 3</summary>

Or start with `min = int.MaxValue` and `max = int.MinValue`.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Also print the **position** (1st, 2nd, …) of the largest number.

## 🔑 Solution

Only after a real try: [open the solution for A09](../solutions/A09-min-and-max-until-zero.cs). Your solution can be different and still correct!

---

⬅️ Previous: [A08 · Multiples of 3 or 5](A08-multiples-of-3-or-5.md) · 📚 [All exercises](README.md) · Next: [A10 · Sum of a series](A10-sum-of-a-series.md) ➡️
