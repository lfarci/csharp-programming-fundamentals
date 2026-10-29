🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › G03

# G03 · Multiplication grid

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Independent | ⭐⭐ | 4c · Draw in 2D | [Nested grid](../cookbook/08-nested-grid.md) | [G01](G01-rectangle.md), [L04](L04-multiplication-table.md) | Custom |

## 🎯 Goal

Print an n×n grid where the cell at row `r` and column `c` contains `r × c`. Each number takes 4 characters (right-aligned).

## ▶️ Start and check

```bash
./ex start G03     # creates practice/G03_MultiplicationGrid.cs (never overwrites your work)
./ex check G03     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#5-do-one-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `void DrawGrid(int n)`: input = n, an int (whole number); result = nothing is returned: the method prints with Console.Write / Console.WriteLine.

## 🧪 Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `DrawGrid(4)` | prints:<br>`   1   2   3   4`<br>`   2   4   6   8`<br>`   3   6   9  12`<br>`   4   8  12  16` |
| `DrawGrid(1)` | prints:<br>`   1` |

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

Only after a real try: [open the solution for G03](../solutions/G03_MultiplicationGrid.cs). Your solution can be different and still correct!

---

⬅️ Previous: [G12 · Upside-down triangle](G12-upside-down-triangle.md) · 📚 [All exercises](README.md) · Next: [G04 · Hollow rectangle](G04-hollow-rectangle.md) ➡️
