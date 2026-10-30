---
prev:
  text: "L02 · Boundaries: < or <="
  link: /exercises/L02-boundaries
next:
  text: "L11 · Count from a to b"
  link: /exercises/L11-count-from-a-to-b
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Count](../themes/loops-count.md) › L03

# L03 · Count up and down

<ExerciseHeader />

<div class="gh-only">

**Loops › Count** · exercise 3 of 13 in this group (3 of 86 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | [Counter loop](../cookbook/01-counter-loop.md) | [L01](L01-trace-a-loop.md) |

</div>

## Goal

Read a positive number N. Print the numbers from 1 to N on one line, then from N down to 1 on a second line.

## Start and check

```bash
./ex start L03     # creates practice/L03_CountUpAndDown.cs (never overwrites your work)
./ex check L03     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** write the whole program inside `Run()`: read with `Console.ReadLine()`, print with `Console.WriteLine()`.

## Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `4`

```text
1 2 3 4
4 3 2 1
```

**Example 2** — input: `1`

```text
1
1
```

## Edge cases to test

- N = 1.

## Rules

- Two loops. Use `Console.Write` to stay on the same line.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Loop 1: start 1, test `i <= n`, step `i++`.

</details>

<details><summary>Hint 2</summary>

Loop 2: start `n`, test `i >= 1`, step `i--`.

</details>

<details><summary>Hint 3</summary>

`Console.Write(i + " ");` then `Console.WriteLine();` after the loop.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Print the even numbers from N down to 2 on one line.

## Solution

Only after a real try: [open the solution for L03](../../internal/solutions/L03_CountUpAndDown.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [L02 · Boundaries: < or <=](L02-boundaries.md) · [Loops](../themes/loops.md) · Next: [L11 · Count from a to b](L11-count-from-a-to-b.md)

</div>
