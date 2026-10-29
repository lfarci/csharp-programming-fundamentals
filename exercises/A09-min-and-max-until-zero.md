---
prev:
  text: "A06 · Average until zero"
  link: /exercises/A06-average-until-zero
next:
  text: "L07 · Ask until valid"
  link: /exercises/L07-ask-until-valid
---

[Home](../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Until the user stops](../themes/loops.md#until-the-user-stops) › A09

# A09 · Min and max until zero

<ExerciseHeader />

<div class="gh-only">

**Loops › Until the user stops** · exercise 3 of 5 in this group (37 of 81 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Independent | medium | write code | [Sentinel loop](../cookbook/10-sentinel-loop.md), [Min/max](../cookbook/04-min-max.md) | [A06](A06-average-until-zero.md), [C02](C02-largest-of-three.md) |

</div>

## Goal

Read whole numbers until 0. Print the smallest and the largest. If no number was entered, print `No numbers.`

## Start and check

```bash
./ex start A09     # creates practice/A09_MinAndMaxUntilZero.cs (never overwrites your work)
./ex check A09     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** write the whole program inside `Run()`: read with `Console.ReadLine()`, print with `Console.WriteLine()`.

## Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `4`, `-2`, `9`, `0`

```text
Min: -2
Max: 9
```

**Example 2** — input: `-5`, `-3`, `0`

```text
Min: -5
Max: -3
```

**Example 3** — input: `0`

```text
No numbers.
```

## Edge cases to test

- Only negative numbers → max must not be 0!
- Only one number → min = max.

## Rules

- No array, no list.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

What do `min` and `max` start at? Not 0. Idea: the first value read.

</details>

<details><summary>Hint 2</summary>

Use a counter: when `count == 1`, set both `min` and `max` to the value.

</details>

<details><summary>Hint 3</summary>

Or start with `min = int.MaxValue` and `max = int.MinValue`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Also print the **position** (1st, 2nd, …) of the largest number.

## Solution

Only after a real try: [open the solution for A09](../solutions/A09_MinAndMaxUntilZero.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [A06 · Average until zero](A06-average-until-zero.md) · [Loops](../themes/loops.md) · Next: [L07 · Ask until valid](L07-ask-until-valid.md)

</div>
