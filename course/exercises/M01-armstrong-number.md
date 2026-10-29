---
prev:
  text: "P02 · All primes up to N"
  link: /exercises/P02-primes-up-to-n
next:
  text: "M02 · Armstrong in a range"
  link: /exercises/M02-armstrong-numbers-in-a-range
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Search and combine](../themes/loops-search-and-combine.md) › M01

# M01 · Armstrong number

<ExerciseHeader />

<div class="gh-only">

**Loops › Search and combine** · exercise 8 of 9 in this group (80 of 81 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Challenge | hard | write code | [Digit extraction](../cookbook/06-digit-extraction.md), [Accumulator](../cookbook/02-accumulator.md) | [D03](D03-count-digits.md), [D04](D04-digit-sum.md), [A07](A07-integer-power.md) |

</div>

Source: teacher topic: Armstrong.

## Goal

An Armstrong number equals the sum of its digits, each raised to the power **number of digits**. Give back `true` if n is one. Example: 153 → 3 digits → 1³ + 5³ + 3³ = 153, so yes.

## Start and check

```bash
./ex start M01     # creates practice/M01_ArmstrongNumber.cs (never overwrites your work)
./ex check M01     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `bool IsArmstrong(int n)`: input = n, an int (whole number); result = a bool (true or false), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `IsArmstrong(153)` | `true` |
| `IsArmstrong(154)` | `false` |
| `IsArmstrong(9474)` | `true` |
| `IsArmstrong(0)` | `true` |
| `IsArmstrong(10)` | `false` |
| `IsArmstrong(370)` | `true` |

## Edge cases to test

- Every 1-digit number is an Armstrong number (5¹ = 5).
- The power is the number of digits, **not always 3**.

## Rules

- No string, no `Math.Pow`. Reuse D03 (count), D04 (digits) and A07 (power).
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Cut the problem: (1) count the digits, (2) for each digit, (3) compute digit^count, (4) add, (5) compare. See [Combining recipes](../cookbook/combining-recipes.md).

</details>

<details><summary>Hint 2</summary>

Step (1) empties your copy. Make a **new** copy of `n` for step (2).

</details>

<details><summary>Hint 3</summary>

The power is a small product loop **inside** the digit loop: `power = 1; for (i = 0; i < digits; i++) power *= digit;`

</details>

## Mastery check

Solve this variation **alone**, on another day:

Two days later, from a blank file: say if N is a *Disarium* number. Each digit is raised to its **position** from the left (89 = 8¹ + 9² = 89, 135 = 1¹ + 3² + 5³ = 135).

## Solution

Only after a real try: [open the solution for M01](../../internal/solutions/M01_ArmstrongNumber.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [P02 · All primes up to N](P02-primes-up-to-n.md) · [Loops](../themes/loops.md) · Next: [M02 · Armstrong in a range](M02-armstrong-numbers-in-a-range.md)

</div>
