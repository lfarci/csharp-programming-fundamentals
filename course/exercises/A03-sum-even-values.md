---
prev:
  text: "A12 · Fix: multiples of 7"
  link: /exercises/A12-fix-count-multiples-of-7
next:
  text: "A17 · Sum the multiples of k"
  link: /exercises/A17-sum-multiples-of-k
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Keep only some](../themes/loops-keep-only-some.md) › A03

# A03 · Sum of the even numbers

<ExerciseHeader />

<div class="gh-only">

**Loops › Keep only some** · exercise 7 of 9 in this group (32 of 81 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Independent | easy | write code | [Conditional accumulator](../cookbook/03-conditional-accumulator.md) | [A02](A02-count-multiples-of-3.md) |

</div>

## Goal

Give back the sum of the even numbers from 1 to n.

## Start and check

```bash
./ex start A03     # creates practice/A03_SumEvenValues.cs (never overwrites your work)
./ex check A03     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int SumOfEvens(int n)`: input = n, an int (whole number); result = an int (whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `SumOfEvens(6)` | `12` |
| `SumOfEvens(7)` | `12` |
| `SumOfEvens(1)` | `0` |
| `SumOfEvens(10)` | `30` |

## Edge cases to test

- N = 1 → 0.

## Rules

- Loop + `if` + accumulator.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Same loop as A02 (loop + `if (i % 2 == 0)`).

</details>

<details><summary>Hint 2</summary>

The box is `sum`, not `count`: inside the `if`, write `sum += i;` instead of `count++;`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Print the sum of the even numbers AND the sum of the odd numbers with **one** loop.

## Solution

Only after a real try: [open the solution for A03](../../internal/solutions/A03_SumEvenValues.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [A12 · Fix: multiples of 7](A12-fix-count-multiples-of-7.md) · [Loops](../themes/loops.md) · Next: [A17 · Sum the multiples of k](A17-sum-multiples-of-k.md)

</div>
