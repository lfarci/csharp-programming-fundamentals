# G02 · Draw a right triangle

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Independent | ⭐⭐ | 4c · Draw in 2D | [Nested grid](../cookbook/08-nested-grid.md) | [G01](G01-rectangle.md) | Custom |

## 🎯 Goal

Read a height. Draw a right triangle: row 1 has 1 star, row 2 has 2 stars, …

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `4`

```text
*
**
***
****
```

**Example 2** — input: `1`

```text
*
```

## ⚠️ Edge cases to test

- Height 1.

## 📏 Rules

- Nested loops.
- No LINQ, no ready-made helpers that do the loop for you. The loop **is** the exercise.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats / what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

Make a table: row → number of stars. Row 3 has 3 stars.

</details>

<details><summary>Hint 2</summary>

Only the **test** of the inner loop changes compared to G01: `col <= row`.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Draw it upside down (4 stars, then 3, 2, 1).

## 🔑 Solution

Only after a real try: [G02-right-triangle](../solutions/G02-right-triangle.cs). Your solution can be different and still correct!

⬅️ [Back to the inventory](README.md)
