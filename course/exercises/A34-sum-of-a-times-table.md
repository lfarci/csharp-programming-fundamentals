---
prev:
  text: "A26 · Sum of tens"
  link: /exercises/A26-sum-of-tens
next:
  text: "A13 · Sum from a to b"
  link: /exercises/A13-sum-from-a-to-b
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Add up](../themes/loops-add-up.md) › A34

# A34 · Sum of a times table

<ExerciseHeader />

<div class="gh-only">

**Loops › Add up** · exercise 6 of 14 in this group (19 of 96 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | [Accumulator](../cookbook/02-accumulator.md) | [A26](A26-sum-of-tens.md), [L04](L04-multiplication-table.md) |

</div>

## Goal

Give back k × 1 + k × 2 + … + k × n: the sum of the first n lines of the k times table.

## Start and check

```bash
./ex start A34     # creates practice/A34_SumOfATimesTable.cs (never overwrites your work)
./ex check A34     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int SumOfTable(int k, int n)`: input = k, an int (whole number), n, an int (whole number); result = an int (whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `SumOfTable(3, 10)` | `165` |
| `SumOfTable(10, 3)` | `60` |
| `SumOfTable(4, 1)` | `4` |
| `SumOfTable(5, 0)` | `0` |

## Edge cases to test

- n = 0: 0.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

A26 with `k` instead of 10.

</details>

<details><summary>Hint 2</summary>

`sum += k * i;`

</details>

## Mastery check

Solve this variation **alone**, on another day:

Give back the sum of the k times table from k × a to k × b.

## Solution

Only after a real try: [open the solution for A34](../../internal/solutions/A34_SumOfATimesTable.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [A26 · Sum of tens](A26-sum-of-tens.md) · [Loops](../themes/loops.md) · Next: [A13 · Sum from a to b](A13-sum-from-a-to-b.md)

</div>
