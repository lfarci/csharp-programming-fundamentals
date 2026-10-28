# G06 · Pyramid

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Challenge | ⭐⭐⭐ | 4c · Draw in 2D | [Nested grid](../cookbook/08-nested-grid.md) | [G02](G02-right-triangle.md) | Custom |

## 🎯 Goal

Read a height. Draw a centered pyramid of `*`.

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `3`

```text
  *
 ***
*****
```

**Example 2** — input: `1`

```text
*
```

## ⚠️ Edge cases to test

- Height 1.

## 📏 Rules

- Nested loops: **two** inner loops (spaces, then stars).
- No LINQ, no ready-made helpers that do the loop for you. The loop **is** the exercise.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats / what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

Make a table for height 3: row → spaces → stars. Row 1: 2 spaces, 1 star. Row 2: 1 space, 3 stars. Row 3: 0, 5.

</details>

<details><summary>Hint 2</summary>

Spaces = `height - row`. Stars = `2 * row - 1`.

</details>

<details><summary>Hint 3</summary>

Inside the row loop: first a loop for the spaces, then a loop for the stars, then `WriteLine()`.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Draw a diamond (a pyramid, then the same pyramid upside down).

## 🔑 Solution

Only after a real try: [G06-pyramid](../solutions/G06-pyramid.cs). Your solution can be different and still correct!

⬅️ [Back to the inventory](README.md)
