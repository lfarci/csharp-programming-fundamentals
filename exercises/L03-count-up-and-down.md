🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › L03

# L03 · Count up and down

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | ⭐ | 4a · Repeat & count | [Counter loop](../cookbook/01-counter-loop.md) | [L01](L01-trace-a-loop.md) | Custom |

## 🎯 Goal

Read a positive number N. Print the numbers from 1 to N on one line, then from N down to 1 on a second line.

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `4`

```text
1 2 3 4
4 3 2 1
```

**Example 2** — input: `1`

```text
1
1
```

## ⚠️ Edge cases to test

- N = 1.

## 📏 Rules

- Two loops. Use `Console.Write` to stay on the same line.
- No LINQ and no ready-made helpers: you write every step yourself.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

Loop 1: start 1, test `i <= n`, step `i++`.

</details>

<details><summary>Hint 2</summary>

Loop 2: start `n`, test `i >= 1`, step `i--`.

</details>

<details><summary>Hint 3</summary>

`Console.Write(i + " ");` then `Console.WriteLine();` after the loop.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Print the odd numbers from N down to 1.

## 🔑 Solution

Only after a real try: [open the solution for L03](../solutions/L03-count-up-and-down.cs). Your solution can be different and still correct!

---

⬅️ Previous: [L02 · Boundaries: < or <= ? (paper)](L02-boundaries.md) · 📚 [All exercises](README.md) · Next: [L04 · Multiplication table](L04-multiplication-table.md) ➡️
