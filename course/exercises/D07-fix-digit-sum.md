---
prev:
  text: "D11 · Largest digit"
  link: /exercises/D11-largest-digit
next:
  text: "D05 · Reverse a number"
  link: /exercises/D05-reverse-a-number
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Digits](../themes/loops-digits.md) › D07

# D07 · Fix: digit sum

<ExerciseHeader />

<div class="gh-only">

**Loops › Digits** · exercise 10 of 13 in this group (67 of 86 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Independent | medium | fix the bugs | [Digit extraction](../cookbook/06-digit-extraction.md) | [D04](D04-digit-sum.md) |

</div>

## Goal

`DigitSum(n)` should give back the sum of the digits of n (n ≥ 0). The code is written, but it has 2 bugs. Fix them.

## Start and check

```bash
./ex start D07     # creates practice/D07_FixDigitSum.cs (never overwrites your work)
./ex check D07     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** the file already holds code that compiles but gives wrong answers. Run `./ex check`, read which example fails, trace that example on paper, then fix the bug. Change as little as you can.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `DigitSum(123)` | `6` |
| `DigitSum(10)` | `1` |
| `DigitSum(7)` | `7` |
| `DigitSum(0)` | `0` |
| `DigitSum(9045)` | `18` |

## Edge cases to test

- `DigitSum(10)`: the loop must still run for the 1.
- `DigitSum(0)` is 0.

## Rules

- The file already has code. It compiles, but it has bugs. Change as **little** as you can.
- There are **2** bugs.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Trace `DigitSum(123)` with a table: `n`, `n % 10`, `sum`.

</details>

<details><summary>Hint 2</summary>

Which operator gives the **last digit**, and which one **removes** it?

</details>

<details><summary>Hint 3</summary>

Trace `DigitSum(10)`: does the loop run at all?

</details>

## Mastery check

Solve this variation **alone**, on another day:

Write a trace table for `DigitSum(907)` with the fixed code.

## Solution

Only after a real try: [open the solution for D07](../../internal/solutions/D07_FixDigitSum.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [D11 · Largest digit](D11-largest-digit.md) · [Loops](../themes/loops.md) · Next: [D05 · Reverse a number](D05-reverse-a-number.md)

</div>
