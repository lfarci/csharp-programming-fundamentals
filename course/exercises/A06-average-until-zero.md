---
prev:
  text: "L05 · Until zero"
  link: /exercises/L05-until-zero
next:
  text: "A09 · Min and max until zero"
  link: /exercises/A09-min-and-max-until-zero
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Until the user stops](../themes/loops.md#until-the-user-stops) › A06

# A06 · Average until zero

<ExerciseHeader />

<div class="gh-only">

**Loops › Until the user stops** · exercise 2 of 5 in this group (36 of 81 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Independent | medium | write code | [Sentinel loop](../cookbook/10-sentinel-loop.md), [Accumulator](../cookbook/02-accumulator.md) | [L05](L05-until-zero.md), [A01](A01-sum-1-to-n.md) |

</div>

## Goal

Read whole numbers until 0. Print their average. If no number was entered, print `No numbers.`

## Start and check

```bash
./ex start A06     # creates practice/A06_AverageUntilZero.cs (never overwrites your work)
./ex check A06     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** write the whole program inside `Run()`: read with `Console.ReadLine()`, print with `Console.WriteLine()`.

## Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `4`, `7`, `1`, `0`

```text
Average: 4
```

**Example 2** — input: `1`, `2`, `0`

```text
Average: 1.5
```

**Example 3** — input: `0`

```text
No numbers.
```

> On a computer set to French/Dutch, `1.5` may print as `1,5`. Both are correct.

## Edge cases to test

- First value 0 → never divide by 0!
- The average can have decimals.

## Rules

- Sentinel loop + two boxes (`sum`, `count`).
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Average = sum / count, so you need **both** boxes.

</details>

<details><summary>Hint 2</summary>

`(double)sum / count` keeps the decimals. `sum / count` with two `int`s does not.

</details>

<details><summary>Hint 3</summary>

Check `count == 0` **after** the loop.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Also print how many numbers were above the average. (Why is that hard without an array? You will see in the Arrays theme.)

## Solution

Only after a real try: [open the solution for A06](../../internal/solutions/A06_AverageUntilZero.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [L05 · Until zero](L05-until-zero.md) · [Loops](../themes/loops.md) · Next: [A09 · Min and max until zero](A09-min-and-max-until-zero.md)

</div>
