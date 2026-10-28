# L04 · Multiplication table

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Independent | ⭐ | 4a · Repeat & count | [Counter loop](../cookbook/01-counter-loop.md) | [L03](L03-count-up-and-down.md) | Custom |

## 🎯 Goal

Read a number N and print its multiplication table from 1 to 10.

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `3`

```text
3 x 1 = 3
3 x 2 = 6
3 x 10 = 30
```

**Example 2** — input: `7`

```text
7 x 7 = 49
```

## ⚠️ Edge cases to test

- N = 0 → all results are 0.

## 📏 Rules

- One `for` loop.
- No LINQ, no ready-made helpers that do the loop for you. The loop **is** the exercise.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats / what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

What changes from line to line? Only the second number (1 to 10).

</details>

<details><summary>Hint 2</summary>

`Console.WriteLine($"{n} x {i} = {n * i}");`

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Read a second number M and print the table up to M instead of 10.

## 🔑 Solution

Only after a real try: [L04-multiplication-table](../solutions/L04-multiplication-table.cs). Your solution can be different and still correct!

⬅️ [Back to the inventory](README.md)
