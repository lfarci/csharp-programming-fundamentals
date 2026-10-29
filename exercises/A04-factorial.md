---
prev:
  text: "A19 · Product from a to b"
  link: /exercises/A19-product-from-a-to-b
next:
  text: "A07 · Integer power"
  link: /exercises/A07-integer-power
---

[Home](../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Add up](../themes/loops.md#add-up) › A04

# A04 · Factorial

<ExerciseHeader />

<div class="gh-only">

**Loops › Add up** · exercise 9 of 12 in this group (22 of 81 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Independent | medium | write code | [Accumulator](../cookbook/02-accumulator.md) | [A01](A01-sum-1-to-n.md) |

</div>

Source: teacher topic: Factorial.

## Goal

Give back n! = 1 × 2 × … × n (0 ≤ n ≤ 20). By definition 0! = 1.

## Start and check

```bash
./ex start A04     # creates practice/A04_Factorial.cs (never overwrites your work)
./ex check A04     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `long Factorial(int n)`: input = n, an int (whole number); result = a long (big whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `Factorial(5)` | `120` |
| `Factorial(0)` | `1` |
| `Factorial(1)` | `1` |
| `Factorial(12)` | `479001600` |
| `Factorial(20)` | `2432902008176640000` |

## Edge cases to test

- N = 0 → 1 (the loop runs 0 times, the box keeps its start value).
- 13! does not fit in an `int` → use `long`.

## Rules

- A loop, no recursion, no library.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Trace 4! on paper: 1 → 1 → 2 → 6 → 24.

</details>

<details><summary>Hint 2</summary>

Product box. What must it start at? (Not 0!)

</details>

<details><summary>Hint 3</summary>

`long product = 1; for (int i = 1; i <= n; i++) product *= i;`

</details>

## Mastery check

Solve this variation **alone**, on another day:

Print every factorial from 0! to N! (one per line), with **one** loop.

## Solution

Only after a real try: [open the solution for A04](../solutions/A04_Factorial.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [A19 · Product from a to b](A19-product-from-a-to-b.md) · [Loops](../themes/loops.md) · Next: [A07 · Integer power](A07-integer-power.md)

</div>
