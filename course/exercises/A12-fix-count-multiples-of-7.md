---
prev:
  text: "A22 · Sum of the divisors"
  link: /exercises/A22-sum-of-divisors
next:
  text: "A03 · Sum of the even numbers"
  link: /exercises/A03-sum-even-values
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Keep only some](../themes/loops.md#keep-only-some) › A12

# A12 · Fix: multiples of 7

<ExerciseHeader />

<div class="gh-only">

**Loops › Keep only some** · exercise 6 of 9 in this group (31 of 81 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | fix the bugs | [Conditional accumulator](../cookbook/03-conditional-accumulator.md) | [A02](A02-count-multiples-of-3.md) |

</div>

## Goal

`CountMultiplesOf7(n)` should count the numbers from 1 to n (included) divisible by 7. The code is written, but it has 2 bugs. Fix them.

## Start and check

```bash
./ex start A12     # creates practice/A12_FixCountMultiplesOf7.cs (never overwrites your work)
./ex check A12     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** the file already holds code that compiles but gives wrong answers. Run `./ex check`, read which example fails, trace that example on paper, then fix the bug. Change as little as you can.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `CountMultiplesOf7(7)` | `1` |
| `CountMultiplesOf7(20)` | `2` |
| `CountMultiplesOf7(6)` | `0` |
| `CountMultiplesOf7(21)` | `3` |

## Edge cases to test

- `CountMultiplesOf7(7)`: is 7 itself counted?

## Rules

- The file already has code. It compiles, but it has bugs. Change as **little** as you can.
- There are **2** bugs.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Run `./ex check A12` first and read which example fails. Then trace `CountMultiplesOf7(7)` on paper.

</details>

<details><summary>Hint 2</summary>

Look at the start value of the box. What should a count be before you have seen anything?

</details>

<details><summary>Hint 3</summary>

Look at the loop test. Is n itself included?

</details>

## Mastery check

Solve this variation **alone**, on another day:

Explain each bug in one sentence, using the words *start value* and *boundary*.

## Solution

Only after a real try: [open the solution for A12](../../internal/solutions/A12_FixCountMultiplesOf7.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [A22 · Sum of the divisors](A22-sum-of-divisors.md) · [Loops](../themes/loops.md) · Next: [A03 · Sum of the even numbers](A03-sum-even-values.md)

</div>
