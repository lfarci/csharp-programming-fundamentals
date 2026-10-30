---
prev:
  text: "R03 · Count matches"
  link: /exercises/R03-count-matches
next:
  text: "R02 · Position of the largest"
  link: /exercises/R02-largest-in-an-array
---

[Home](../../README.md) › [Exercises](README.md) › [Arrays, text and lists](../themes/arrays.md) › [Arrays](../themes/arrays-arrays.md) › R07

# R07 · Count the even values

<ExerciseHeader />

<div class="gh-only">

**Arrays, text and lists › Arrays** · exercise 3 of 8 in this group (3 of 13 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Independent | medium | write code | [Array traversal](../cookbook/11-array-traversal.md), [Conditional accumulator](../cookbook/03-conditional-accumulator.md) | [R01](R01-sum-an-array.md), [A15](A15-count-even-numbers.md) |

</div>

## Goal

Give back how many values in the array are even.

## Start and check

```bash
./ex start R07     # creates practice/R07_CountTheEvenValues.cs (never overwrites your work)
./ex check R07     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int CountEven(int[] values)`: input = values, an int[] (array of whole numbers); result = an int (whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `CountEven(new int[] { 1, 2, 3, 4 })` | `2` |
| `CountEven(new int[] { 2, 4, 6 })` | `3` |
| `CountEven(new int[] { 1, 3 })` | `0` |
| `CountEven(new int[0])` | `0` |
| `CountEven(new int[] { -2, 0, 5 })` | `2` |

## Edge cases to test

- An empty array: 0.
- Negative even values and 0 are even too.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

A15 (count the even numbers) with `values[i]` instead of `i`.

</details>

<details><summary>Hint 2</summary>

The loop goes from 0 to `values.Length - 1`: `i < values.Length`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Give back the sum of the odd values as well.

## Solution

Only after a real try: [open the solution for R07](../../internal/solutions/R07_CountTheEvenValues.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [R03 · Count matches](R03-count-matches.md) · [Arrays, text and lists](../themes/arrays.md) · Next: [R02 · Position of the largest](R02-largest-in-an-array.md)

</div>
