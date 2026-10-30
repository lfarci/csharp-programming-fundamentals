---
prev:
  text: "A08 · Multiples of 3 or 5"
  link: /exercises/A08-multiples-of-3-or-5
next:
  text: "A06 · Average until zero"
  link: /exercises/A06-average-until-zero
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Until the user stops](../themes/loops-until-the-user-stops.md) › L05

# L05 · Until zero

<ExerciseHeader />

<div class="gh-only">

**Loops › Until the user stops** · exercise 1 of 5 in this group (37 of 86 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Independent | medium | write code | [Sentinel loop](../cookbook/10-sentinel-loop.md), [Accumulator](../cookbook/02-accumulator.md) | [L03](L03-count-up-and-down.md) |

</div>

## Goal

Read whole numbers one by one. Stop when the user types 0. Print how many **non-zero** numbers were entered.

## Start and check

```bash
./ex start L05     # creates practice/L05_UntilZero.cs (never overwrites your work)
./ex check L05     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** write the whole program inside `Run()`: read with `Console.ReadLine()`, print with `Console.WriteLine()`.

## Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `5`, `-2`, `8`, `0`

```text
You entered 3 numbers.
```

**Example 2** — input: `0`

```text
You entered 0 numbers.
```

## Edge cases to test

- The first number is already 0.
- Negative numbers count too.

## Rules

- You do not know how many numbers will come: no `for`.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

This is the [sentinel loop](../cookbook/10-sentinel-loop.md). 0 is the sentinel.

</details>

<details><summary>Hint 2</summary>

`while (true) { read; if (value == 0) break; count++; }`

</details>

<details><summary>Hint 3</summary>

Do not count the 0 itself.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Also print how many of the numbers were negative.

## Solution

Only after a real try: [open the solution for L05](../../internal/solutions/L05_UntilZero.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [A08 · Multiples of 3 or 5](A08-multiples-of-3-or-5.md) · [Loops](../themes/loops.md) · Next: [A06 · Average until zero](A06-average-until-zero.md)

</div>
