[Home](../README.md) › [Roadmap](../ROADMAP.md) › [Exercises](README.md) › R02

# R02 · Largest value in an array

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Independent | medium | 6 · Arrays | [Array traversal](../cookbook/11-array-traversal.md), [Min/max](../cookbook/04-min-max.md) | [R01](R01-sum-an-array.md), [C02](C02-largest-of-three.md) | Custom |

## Goal

Give back the **position** (index) of the largest value in the array (the first one if it appears twice). The array has at least 1 value.

## Start and check

```bash
./ex start R02     # creates practice/R02_LargestInAnArray.cs (never overwrites your work)
./ex check R02     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#5-do-one-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int IndexOfLargest(int[] values)`: input = values, an int[] (array of whole numbers); result = an int (whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `IndexOfLargest(new int[] { -5, -2, -9 })` | `1` |
| `IndexOfLargest(new int[] { 3, 7, 2, 7, 1 })` | `1` |
| `IndexOfLargest(new int[] { 4 })` | `0` |
| `IndexOfLargest(new int[] { 1, 2, 9 })` | `2` |

## Edge cases to test

- All negative.
- The max appears twice → give the **first** position.

## Rules

- No `.Max()`. Start with `values[0]`, not 0.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Two boxes: `max = values[0]` and `maxIndex = 0`.

</details>

<details><summary>Hint 2</summary>

Loop from index 1. Use `>` (not `>=`) to keep the first position.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Print the second largest value.

## Solution

Only after a real try: [open the solution for R02](../solutions/R02_LargestInAnArray.cs). Your solution can be different and still correct!

---

Previous: [R01 · Sum of an array](R01-sum-an-array.md) · [All exercises](README.md) · Next: [R06 · Fix the bugs: largest value](R06-fix-largest-value.md)
