# G05 · Checkerboard

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Challenge | ⭐⭐ | 4c · Draw in 2D | [Nested grid](../cookbook/08-nested-grid.md) | [G04](G04-hollow-rectangle.md), [C01](C01-even-or-odd.md) | Custom |

## 🎯 Goal

Read a size. Draw a size×size checkerboard with `#` and `.`, starting with `#` in the top-left corner.

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `4`

```text
#.#.
.#.#
#.#.
.#.#
```

**Example 2** — input: `1`

```text
#
```

## ⚠️ Edge cases to test

- Odd size.

## 📏 Rules

- Nested loops. No `string` tricks.
- No LINQ, no ready-made helpers that do the loop for you. The loop **is** the exercise.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats / what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

Look at `row + col` for every `#` cell. What do they have in common?

</details>

<details><summary>Hint 2</summary>

Even sum → `#`, odd sum → `.` (with rows and columns starting at 1).

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Make each square 2×2 characters big.

## 🔑 Solution

Only after a real try: [G05-checkerboard](../solutions/G05-checkerboard.cs). Your solution can be different and still correct!

⬅️ [Back to the inventory](README.md)
