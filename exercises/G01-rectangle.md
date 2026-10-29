🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › G01

# G01 · Draw a rectangle

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | ⭐ | 4c · Draw in 2D | [Nested grid](../cookbook/08-nested-grid.md) | [L03](L03-count-up-and-down.md) | Custom |

## 🎯 Goal

Read a width and a height. Draw a rectangle of `*`.

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `4`, `3`

```text
****
****
****
```

**Example 2** — input: `1`, `2`

```text
*
*
```

## ⚠️ Edge cases to test

- Width 1 → a vertical line.

## 📏 Rules

- Two nested `for` loops. Print one `*` at a time.
- No LINQ and no ready-made helpers: you write every step yourself.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

Step 1: print **one** line of `width` stars with one loop.

</details>

<details><summary>Hint 2</summary>

Step 2: repeat that line `height` times → put it in another loop.

</details>

<details><summary>Hint 3</summary>

`Console.Write("*")` in the inner loop, `Console.WriteLine()` after it.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Read the character to use too (`#`, `o`, …).

## 🔑 Solution

Only after a real try: [open the solution for G01](../solutions/G01-rectangle.cs). Your solution can be different and still correct!

---

⬅️ Previous: [A10 · Sum of a series](A10-sum-of-a-series.md) · 📚 [All exercises](README.md) · Next: [G02 · Draw a right triangle](G02-right-triangle.md) ➡️
