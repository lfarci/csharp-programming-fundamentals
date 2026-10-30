---
prev:
  text: "S05 · N-th Fibonacci"
  link: /exercises/S05-nth-fibonacci
next:
  text: "S03 · Even Fibonacci sum"
  link: /exercises/S03-even-fibonacci-sum
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Changing values](../themes/loops-changing-values.md) › S07

# S07 · Greatest common divisor

<ExerciseHeader />

<div class="gh-only">

**Loops › Changing values** · exercise 6 of 7 in this group (76 of 86 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Independent | medium | write code | [State update](../cookbook/07-state-update.md) | [S02](S02-fibonacci.md), [D01](D01-last-digit.md) |

</div>

## Goal

Give back the greatest common divisor of a and b (a ≥ 1, b ≥ 0) with Euclid's method: while `b` is not 0, replace `(a, b)` by `(b, a % b)`. When `b` is 0, the answer is `a`.

## Start and check

```bash
./ex start S07     # creates practice/S07_GreatestCommonDivisor.cs (never overwrites your work)
./ex check S07     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int Gcd(int a, int b)`: input = a, an int (whole number), b, an int (whole number); result = an int (whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `Gcd(12, 18)` | `6` |
| `Gcd(18, 12)` | `6` |
| `Gcd(7, 5)` | `1` |
| `Gcd(10, 10)` | `10` |
| `Gcd(9, 0)` | `9` |

## Edge cases to test

- b = 0: the loop never runs, the answer is a.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Same idea as Fibonacci (S02): a temporary box keeps a value before you overwrite it.

</details>

<details><summary>Hint 2</summary>

`int rest = a % b; a = b; b = rest;` in this order.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Write `Lcm(a, b)` = a / Gcd(a, b) × b.

## Solution

Only after a real try: [open the solution for S07](../../internal/solutions/S07_GreatestCommonDivisor.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [S05 · N-th Fibonacci](S05-nth-fibonacci.md) · [Loops](../themes/loops.md) · Next: [S03 · Even Fibonacci sum](S03-even-fibonacci-sum.md)

</div>
