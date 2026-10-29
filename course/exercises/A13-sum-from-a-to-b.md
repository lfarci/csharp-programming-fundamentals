---
prev:
  text: "A01 · Sum from 1 to N"
  link: /exercises/A01-sum-1-to-n
next:
  text: "A14 · Sum the odd numbers"
  link: /exercises/A14-sum-odd-numbers
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Add up](../themes/loops.md#add-up) › A13

# A13 · Sum from a to b

<ExerciseHeader />

<div class="gh-only">

**Loops › Add up** · exercise 4 of 12 in this group (17 of 81 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | [Accumulator](../cookbook/02-accumulator.md) | [A01](A01-sum-1-to-n.md) |

</div>

## Goal

Give back a + (a+1) + … + b.

## Start and check

```bash
./ex start A13     # creates practice/A13_SumFromAToB.cs (never overwrites your work)
./ex check A13     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int SumFromTo(int a, int b)`: input = a, an int (whole number), b, an int (whole number); result = an int (whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `SumFromTo(3, 5)` | `12` |
| `SumFromTo(1, 4)` | `10` |
| `SumFromTo(7, 7)` | `7` |
| `SumFromTo(5, 4)` | `0` |

## Edge cases to test

- `a` bigger than `b`: 0.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

A01 with the loop starting at `a`.

</details>

<details><summary>Hint 2</summary>

`sum = 0` before, `sum += i` inside, `return sum` after.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Sum the numbers from `b` down to `a`.

## Solution

Only after a real try: [open the solution for A13](../../internal/solutions/A13_SumFromAToB.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [A01 · Sum from 1 to N](A01-sum-1-to-n.md) · [Loops](../themes/loops.md) · Next: [A14 · Sum the odd numbers](A14-sum-odd-numbers.md)

</div>
