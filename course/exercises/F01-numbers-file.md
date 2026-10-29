---
prev:
  text: "T03 · Keep the digits"
  link: /exercises/T03-count-and-keep-digits
next:
  text: "K01 · Shopping list"
  link: /exercises/K01-shopping-list
---

[Home](../../README.md) › [Exercises](README.md) › [Arrays, text and lists](../themes/arrays.md) › [Files and lists](../themes/arrays-files-and-lists.md) › F01

# F01 · Save numbers to a file

<ExerciseHeader />

<div class="gh-only">

**Arrays, text and lists › Files and lists** · exercise 1 of 2 in this group (10 of 11 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Independent | medium | write code | [Sentinel loop](../cookbook/10-sentinel-loop.md), [Array traversal](../cookbook/11-array-traversal.md), [Accumulator](../cookbook/02-accumulator.md) | [L05](L05-until-zero.md), [R01](R01-sum-an-array.md) |

</div>

## Goal

Read numbers until 0 and save them (one per line) in `numbers.txt`. Then read the file back and print how many lines it has and the sum.

## Start and check

```bash
./ex start F01     # creates practice/F01_NumbersFile.cs (never overwrites your work)
./ex check F01     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** write the whole program inside `Run()`: read with `Console.ReadLine()`, print with `Console.WriteLine()`.

## Examples

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

## Edge cases to test

- No number → an empty file.

## Rules

- Save with `File.WriteAllText`, read back with `File.ReadAllLines`. Build the text yourself with `+=` (lists come later, in the Collections theme).
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Build one string: start with `string content = "";` and add each number plus `"\n"` (a new line). Write the file once, after the loop.

</details>

<details><summary>Hint 2</summary>

`string[] lines = File.ReadAllLines("numbers.txt");` gives an array → [array traversal](../cookbook/11-array-traversal.md).

</details>

<details><summary>Hint 3</summary>

Each line is text: `int.Parse(line)`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

When the program starts, if the file exists, first print the numbers saved last time.

## Solution

Only after a real try: [open the solution for F01](../../internal/solutions/F01_NumbersFile.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [T03 · Keep the digits](T03-count-and-keep-digits.md) · [Arrays, text and lists](../themes/arrays.md) · Next: [K01 · Shopping list](K01-shopping-list.md)

</div>
