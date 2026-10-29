[Home](../README.md) › [Roadmap](../ROADMAP.md) › [Exercises](README.md) › K01

# K01 · Shopping list

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Independent | medium | 9 · Collections | [Sentinel loop](../cookbook/10-sentinel-loop.md), [Array traversal](../cookbook/11-array-traversal.md) | [R01](R01-sum-an-array.md), [L05](L05-until-zero.md) | Custom |

## Goal

Read items until the user types `done`. Store them in a `List<string>`. Print them numbered, then the total.

## Start and check

```bash
./ex start K01     # creates practice/K01_ShoppingList.cs (never overwrites your work)
./ex check K01     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#5-do-one-exercise).

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

Only after a real try: [open the solution for K01](../solutions/K01_ShoppingList.cs). Your solution can be different and still correct!

---

Previous: [E01 · Safe number reader](E01-safe-number-reader.md) · [All exercises](README.md) · Next: [N01 · Armstrong with methods](N01-armstrong-with-methods.md)
