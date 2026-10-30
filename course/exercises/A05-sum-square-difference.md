---
prev:
  text: "A07 · Integer power"
  link: /exercises/A07-integer-power
next:
  text: "A10 · Sum of a series"
  link: /exercises/A10-sum-of-a-series
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Add up](../themes/loops-add-up.md) › A05

# A05 · Sum and sum of squares

<ExerciseHeader />

<div class="gh-only">

**Loops › Add up** · exercise 11 of 12 in this group (24 of 81 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Independent | medium | write code | [Accumulator](../cookbook/02-accumulator.md) | [A01](A01-sum-1-to-n.md) |

</div>

Source: prepares [Project Euler #6](https://projecteuler.net/problem=6).

## Goal

Read N. With **one** loop compute the sum 1+…+N and the sum of squares 1²+…+N². Print both, then (sum)² − (sum of squares).

## Start and check

```bash
./ex start A05     # creates practice/A05_SumSquareDifference.cs (never overwrites your work)
./ex check A05     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** write the whole program inside `Run()`: read with `Console.ReadLine()`, print with `Console.WriteLine()`.

## Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `3`

```text
Sum: 6
Sum of squares: 14
Difference: 22
```

**Example 2** — input: `10`

```text
Sum: 55
Sum of squares: 385
Difference: 2640
```

## Edge cases to test

- N = 1 → 1, 1, 0.

`./ex check` tests these too: input `1` prints `Sum of squares: 1`, `Difference: 0`.

## Rules

- One loop, two boxes.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Two boxes before the loop: `sum = 0`, `squares = 0`.

</details>

<details><summary>Hint 2</summary>

`squares += i * i;`

</details>

<details><summary>Hint 3</summary>

The difference is computed **after** the loop: `sum * sum - squares`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Now solve [Project Euler #6](https://projecteuler.net/problem=6) (N = 100). Use `long` if needed.

## Solution

Only after a real try: [open the solution for A05](../../internal/solutions/A05_SumSquareDifference.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [A07 · Integer power](A07-integer-power.md) · [Loops](../themes/loops.md) · Next: [A10 · Sum of a series](A10-sum-of-a-series.md)

</div>
