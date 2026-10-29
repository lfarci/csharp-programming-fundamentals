🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › G11

# G11 · Counting triangle

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | ⭐ | 4c · Draw in 2D | [Nested grid](../cookbook/08-nested-grid.md) | [G10](G10-row-number-triangle.md) | Custom |

## 🎯 Goal

Print a triangle where row r is `12…r`: `1`, `12`, `123`.

## ▶️ Start and check

```bash
./ex start G11     # creates practice/G11_CountingTriangle.cs (never overwrites your work)
./ex check G11     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#5-do-one-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what it **prints** is its result (it has no `return`).

- `void DrawCountingTriangle(int height)`: input = height, an int (whole number); result = the lines it writes with Console.Write / Console.WriteLine (no return).

## 🧪 Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `DrawCountingTriangle(4)` | prints:<br>`1`<br>`12`<br>`123`<br>`1234` |
| `DrawCountingTriangle(1)` | prints:<br>`1` |

## ⚠️ Edge cases to test

- height = 1: `1`.

## 📏 Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

G10, printing `col` instead of `row`.

</details>

<details><summary>Hint 2</summary>

Inner loop: `col` from 1 to `row`.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Print the same triangle upside down.

## 🔑 Solution

Only after a real try: [open the solution for G11](../solutions/G11_CountingTriangle.cs). Your solution can be different and still correct!

---

⬅️ Previous: [G10 · Triangle of row numbers](G10-row-number-triangle.md) · 📚 [All exercises](README.md) · Next: [G12 · Upside-down triangle](G12-upside-down-triangle.md) ➡️
