🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › F01

# F01 · Save numbers to a file

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Independent | ⭐⭐ | 5 · Files | [Sentinel loop](../cookbook/10-sentinel-loop.md), [Array traversal](../cookbook/11-array-traversal.md), [Accumulator](../cookbook/02-accumulator.md) | [L05](L05-until-zero.md), [R01](R01-sum-an-array.md) | Custom |

## 🎯 Goal

Read numbers until 0 and save them (one per line) in `numbers.txt`. Then read the file back and print how many lines it has and the sum.

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `4`, `7`, `1`, `0`

```text
Lines: 3
Sum: 12
```

**Example 2** — input: `0`

```text
Lines: 0
Sum: 0
```

## ⚠️ Edge cases to test

- No number → an empty file.

## 📏 Rules

- Save with `File.WriteAllText`, read back with `File.ReadAllLines`. Build the text yourself with `+=` (lists come in step 9).
- No LINQ and no ready-made helpers: you write every step yourself.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

Build one string: start with `string content = "";` and add each number plus `"\n"` (a new line). Write the file once, after the loop.

</details>

<details><summary>Hint 2</summary>

`string[] lines = File.ReadAllLines("numbers.txt");` gives an array → [array traversal](../cookbook/11-array-traversal.md).

</details>

<details><summary>Hint 3</summary>

Each line is text: `int.Parse(line)`.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

When the program starts, if the file exists, first print the numbers saved last time.

## 🔑 Solution

Only after a real try: [open the solution for F01](../solutions/F01-numbers-file.cs). Your solution can be different and still correct!

---

⬅️ Previous: [T03 · Count and keep the digits](T03-count-and-keep-digits.md) · 📚 [All exercises](README.md) · Next: [E01 · Safe number reader](E01-safe-number-reader.md) ➡️
