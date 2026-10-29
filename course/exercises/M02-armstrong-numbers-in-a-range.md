---
prev:
  text: "M01 · Armstrong number"
  link: /exercises/M01-armstrong-number
next:
  text: "Next theme: Arrays, text and lists"
  link: /themes/arrays
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Search and combine](../themes/loops-search-and-combine.md) › M02

# M02 · Armstrong in a range

<ExerciseHeader />

<div class="gh-only">

**Loops › Search and combine** · exercise 9 of 9 in this group (81 of 81 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Challenge | hard | write code | [Counter loop](../cookbook/01-counter-loop.md), [Digit extraction](../cookbook/06-digit-extraction.md), [Accumulator](../cookbook/02-accumulator.md) | [M01](M01-armstrong-number.md) |

</div>

## Goal

Read a lower and an upper bound. Print every Armstrong number between them (both included).

## Start and check

```bash
./ex start M02     # creates practice/M02_ArmstrongNumbersInARange.cs (never overwrites your work)
./ex check M02     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** write the whole program inside `Run()`: read with `Console.ReadLine()`, print with `Console.WriteLine()`.

## Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `100`, `999`

```text
153 370 371 407
```

**Example 2** — input: `1`, `9`

```text
1 2 3 4 5 6 7 8 9
```

**Example 3** — input: `1000`, `9999`

```text
1634 8208 9474
```

## Edge cases to test

- Bounds included.

## Rules

- Your M01 code inside a counter loop. Beware: the inner variables must be reset for every candidate.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Outer loop: `candidate` from `lower` to `upper`.

</details>

<details><summary>Hint 2</summary>

Paste M01 inside and replace `n` by `candidate`.

</details>

<details><summary>Hint 3</summary>

Declare `digits`, `sum`, `remaining` **inside** the outer loop so they restart at 0.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Count how many Armstrong numbers exist below 100000.

## Solution

Only after a real try: [open the solution for M02](../../internal/solutions/M02_ArmstrongNumbersInARange.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [M01 · Armstrong number](M01-armstrong-number.md) · [Loops](../themes/loops.md) · Next: [Next theme: Arrays, text and lists](../themes/arrays.md)

</div>
