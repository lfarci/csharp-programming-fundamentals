---
prev:
  text: "A14 · Sum the odd numbers"
  link: /exercises/A14-sum-odd-numbers
next:
  text: "A20 · Power of 2"
  link: /exercises/A20-powers-of-2
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Add up](../themes/loops-add-up.md) › A18

# A18 · Sum of cubes

<ExerciseHeader />

<div class="gh-only">

**Loops › Add up** · exercise 6 of 12 in this group (19 of 81 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | [Accumulator](../cookbook/02-accumulator.md) | [A11](A11-arrange-sum-of-squares.md) |

</div>

## Goal

Give back 1³ + 2³ + … + n³.

## Start and check

```bash
./ex start A18     # creates practice/A18_SumOfCubes.cs (never overwrites your work)
./ex check A18     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int SumOfCubes(int n)`: input = n, an int (whole number); result = an int (whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `SumOfCubes(3)` | `36` |
| `SumOfCubes(1)` | `1` |
| `SumOfCubes(4)` | `100` |
| `SumOfCubes(0)` | `0` |

## Edge cases to test

- n = 0: 0.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

A11 (squares) with `i * i * i`.

</details>

<details><summary>Hint 2</summary>

Box before, add inside, return after.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Sum 1 + 4 + 9 + … from memory, without looking at A11.

## Solution

Only after a real try: [open the solution for A18](../../internal/solutions/A18_SumOfCubes.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [A14 · Sum the odd numbers](A14-sum-odd-numbers.md) · [Loops](../themes/loops.md) · Next: [A20 · Power of 2](A20-powers-of-2.md)

</div>
