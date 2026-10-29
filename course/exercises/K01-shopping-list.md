---
prev:
  text: "F01 · Save numbers to a file"
  link: /exercises/F01-numbers-file
next:
  text: "Next theme: Methods and errors"
  link: /themes/methods
---

[Home](../../README.md) › [Exercises](README.md) › [Arrays, text and lists](../themes/arrays.md) › [Files and lists](../themes/arrays-files-and-lists.md) › K01

# K01 · Shopping list

<ExerciseHeader />

<div class="gh-only">

**Arrays, text and lists › Files and lists** · exercise 2 of 2 in this group (11 of 11 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Independent | medium | write code | [Sentinel loop](../cookbook/10-sentinel-loop.md), [Array traversal](../cookbook/11-array-traversal.md) | [R01](R01-sum-an-array.md), [L05](L05-until-zero.md) |

</div>

## Goal

Read items until the user types `done`. Store them in a `List<string>`. Print them numbered, then the total.

## Start and check

```bash
./ex start K01     # creates practice/K01_ShoppingList.cs (never overwrites your work)
./ex check K01     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** write the whole program inside `Run()`: read with `Console.ReadLine()`, print with `Console.WriteLine()`.

## Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `milk`, `eggs`, `bread`, `done`

```text
1. milk
2. eggs
3. bread
Total: 3 items
```

**Example 2** — input: `done`

```text
Total: 0 items
```

## Edge cases to test

- `done` right away.

## Rules

- `List<string>`, `Add`, `Count`.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

`List<string> items = new List<string>();`

</details>

<details><summary>Hint 2</summary>

Sentinel loop with `"done"`.

</details>

<details><summary>Hint 3</summary>

Numbering: a `for` loop with `i + 1`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Do not add an item that is already in the list (`items.Contains(item)`).

## Solution

Only after a real try: [open the solution for K01](../../internal/solutions/K01_ShoppingList.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [F01 · Save numbers to a file](F01-numbers-file.md) · [Arrays, text and lists](../themes/arrays.md) · Next: [Next theme: Methods and errors](../themes/methods.md)

</div>
