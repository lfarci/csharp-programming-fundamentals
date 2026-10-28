# G04 · Hollow rectangle

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Independent | ⭐⭐ | 4c · Draw in 2D | [Nested grid](../cookbook/08-nested-grid.md) | [G01](G01-rectangle.md) | Custom |

## 🎯 Goal

Read a width and a height. Draw only the border of the rectangle with `*`; the inside is spaces.

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `5`, `4`

```text
*****
*   *
*   *
*****
```

**Example 2** — input: `3`, `3`

```text
***
* *
***
```

## ⚠️ Edge cases to test

- Height 1 or 2 → no inside.

## 📏 Rules

- Nested loops + one `if` inside.
- No LINQ, no ready-made helpers that do the loop for you. The loop **is** the exercise.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats / what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

A cell is on the border if it is in the first row, the last row, the first column or the last column.

</details>

<details><summary>Hint 2</summary>

`if (row == 1 || row == height || col == 1 || col == width)`.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Draw an X inside a square (cells where `row == col` or `row + col == size + 1`).

## 🔑 Solution

Only after a real try: [G04-hollow-rectangle](../solutions/G04-hollow-rectangle.cs). Your solution can be different and still correct!

⬅️ [Back to the inventory](README.md)
