---
prev:
  text: "A20 · Power of 2"
  link: /exercises/A20-powers-of-2
next:
  text: "A04 · Factorial"
  link: /exercises/A04-factorial
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Add up](../themes/loops-add-up.md) › A19

# A19 · Product from a to b

<ExerciseHeader />

<div class="gh-only">

**Loops › Add up** · exercise 8 of 12 in this group (21 of 86 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | [Accumulator](../cookbook/02-accumulator.md) | [A20](A20-powers-of-2.md), [A13](A13-sum-from-a-to-b.md) |

</div>

## Goal

Give back a × (a+1) × … × b. If `a` is bigger than `b`, give back 1.

## Start and check

```bash
./ex start A19     # creates practice/A19_ProductFromAToB.cs (never overwrites your work)
./ex check A19     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `long ProductFromTo(int a, int b)`: input = a, an int (whole number), b, an int (whole number); result = a long (big whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `ProductFromTo(2, 4)` | `24` |
| `ProductFromTo(3, 3)` | `3` |
| `ProductFromTo(1, 5)` | `120` |
| `ProductFromTo(5, 4)` | `1` |

## Edge cases to test

- `a` bigger than `b`: 1 (nothing was multiplied).

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Like A20: the product box starts at 1, and each turn does `product *= i;`.

</details>

<details><summary>Hint 2</summary>

The loop starts at `a` and stops after `b`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Multiply only the even numbers from a to b.

## Solution

Only after a real try: [open the solution for A19](../../internal/solutions/A19_ProductFromAToB.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [A20 · Power of 2](A20-powers-of-2.md) · [Loops](../themes/loops.md) · Next: [A04 · Factorial](A04-factorial.md)

</div>
