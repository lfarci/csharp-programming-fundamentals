---
prev:
  text: "R02 · Position of the largest"
  link: /exercises/R02-largest-in-an-array
next:
  text: "R04 · Find the position"
  link: /exercises/R04-find-the-position
---

[Home](../../README.md) › [Exercises](README.md) › [Arrays, text and lists](../themes/arrays.md) › [Arrays](../themes/arrays.md#arrays) › R06

# R06 · Fix: largest value

<ExerciseHeader />

<div class="gh-only">

**Arrays, text and lists › Arrays** · exercise 4 of 6 in this group (4 of 11 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Independent | medium | fix the bugs | [Array traversal](../cookbook/11-array-traversal.md), [Min/max](../cookbook/04-min-max.md) | [R02](R02-largest-in-an-array.md) |

</div>

## Goal

`Largest(values)` should give back the largest value of the array (at least 1 value). The code is written, but it has 2 bugs. Fix them.

## Start and check

```bash
./ex start R06     # creates practice/R06_FixLargestValue.cs (never overwrites your work)
./ex check R06     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** the file already holds code that compiles but gives wrong answers. Run `./ex check`, read which example fails, trace that example on paper, then fix the bug. Change as little as you can.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `Largest(new int[] { 3, 7, 2 })` | `7` |
| `Largest(new int[] { -5, -2, -9 })` | `-2` |
| `Largest(new int[] { 4 })` | `4` |
| `Largest(new int[] { 1, 2, 9 })` | `9` |

## Edge cases to test

- All values negative.
- One value only.

## Rules

- The file already has code. It compiles, but it has bugs. Change as **little** as you can.
- There are **2** bugs. One makes the program crash.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Read the crash message from `./ex check R06`: *index outside the bounds* means the loop goes one step too far.

</details>

<details><summary>Hint 2</summary>

The last index of an array is `values.Length - 1`.

</details>

<details><summary>Hint 3</summary>

Try `[-5, -2, -9]` on paper. Why does a start value of 0 give a wrong answer?

</details>

## Mastery check

Solve this variation **alone**, on another day:

Explain why the best start value for a max is the first value of the array.

## Solution

Only after a real try: [open the solution for R06](../../internal/solutions/R06_FixLargestValue.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [R02 · Position of the largest](R02-largest-in-an-array.md) · [Arrays, text and lists](../themes/arrays.md) · Next: [R04 · Find the position](R04-find-the-position.md)

</div>
