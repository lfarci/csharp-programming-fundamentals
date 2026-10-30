---
prev:
  text: "L13 · Count by 3"
  link: /exercises/L13-count-by-3
next:
  text: "L16 · Odd numbers"
  link: /exercises/L16-odd-numbers
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Count](../themes/loops-count.md) › L14

# L14 · Count by 5

<ExerciseHeader />

<div class="gh-only">

**Loops › Count** · exercise 7 of 13 in this group (7 of 81 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | [Counter loop](../cookbook/01-counter-loop.md) | [L13](L13-count-by-3.md) |

</div>

## Goal

Print 5, 10, 15, … up to n, one per line.

## Start and check

```bash
./ex start L14     # creates practice/L14_CountBy5.cs (never overwrites your work)
./ex check L14     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what it **prints** is its result (it has no `return`).

- `void CountBy5(int n)`: input = n, an int (whole number); result = the lines it writes with Console.Write / Console.WriteLine (no return).

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `CountBy5(22)` | prints:<br>`5`<br>`10`<br>`15`<br>`20` |
| `CountBy5(5)` | prints:<br>`5` |

## Edge cases to test

- n = 4: nothing.

`./ex check` tests these too: `CountBy5(4)` prints nothing.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Same loop as L13: only the start and the step change.

</details>

<details><summary>Hint 2</summary>

Start at 5, step `i += 5`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Count by 10 up to n.

## Solution

Only after a real try: [open the solution for L14](../../internal/solutions/L14_CountBy5.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [L13 · Count by 3](L13-count-by-3.md) · [Loops](../themes/loops.md) · Next: [L16 · Odd numbers](L16-odd-numbers.md)

</div>
