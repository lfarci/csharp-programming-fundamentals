🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › G03

# G03 · Multiplication grid

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Independent | ⭐⭐ | 4c · Draw in 2D | [Nested grid](../cookbook/08-nested-grid.md) | [G01](G01-rectangle.md), [L04](L04-multiplication-table.md) | Custom |

## 🎯 Goal

Read N. Print an N×N grid where the cell at row `r` and column `c` contains `r × c`. Each number takes 4 characters (right-aligned).

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `4`

```text
   1   2   3   4
   2   4   6   8
   3   6   9  12
   4   8  12  16
```

## ⚠️ Edge cases to test

- N = 1 → one cell.

## 📏 Rules

- Nested loops.
- No LINQ and no ready-made helpers: you write every step yourself.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

Same skeleton as G01, but print a number instead of a star.

</details>

<details><summary>Hint 2</summary>

Right-align on 4 characters: `Console.Write($"{row * col,4}");`

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Only print the cells where `c <= r` (a triangle of numbers).

## 🔑 Solution

Only after a real try: [open the solution for G03](../solutions/G03-multiplication-grid.cs). Your solution can be different and still correct!

---

⬅️ Previous: [G02 · Draw a right triangle](G02-right-triangle.md) · 📚 [All exercises](README.md) · Next: [G04 · Hollow rectangle](G04-hollow-rectangle.md) ➡️
