[Home](../README.md) › [Exercises](README.md) › [Loops: keep a running result](../themes/loops-running-result.md) › A12

# A12 · Fix the bugs: count multiples of 7

| Level | Difficulty | Theme | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | easy | [Loops: keep a running result](../themes/loops-running-result.md) | [Conditional accumulator](../cookbook/03-conditional-accumulator.md) | [A02](A02-count-multiples-of-3.md) | Custom |

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

Only after a real try: [open the solution for A12](../solutions/A12_FixCountMultiplesOf7.cs). Your solution can be different and still correct!

---

Previous: [A02 · Count multiples of 3](A02-count-multiples-of-3.md) · [All exercises](README.md) · Next: [A03 · Sum of the even numbers](A03-sum-even-values.md)
