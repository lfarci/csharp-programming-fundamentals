---
prev:
  text: "L11 · Count from a to b"
  link: /exercises/L11-count-from-a-to-b
next:
  text: "L13 · Count by 3"
  link: /exercises/L13-count-by-3
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Count](../themes/loops-count.md) › L12

# L12 · Count down

<ExerciseHeader />

<div class="gh-only">

**Loops › Count** · exercise 5 of 13 in this group (5 of 81 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | [Counter loop](../cookbook/01-counter-loop.md) | [L11](L11-count-from-a-to-b.md) |

</div>

## Goal

Print n, n−1, …, 1, one per line.

## Start and check

```bash
./ex start L12     # creates practice/L12_CountDown.cs (never overwrites your work)
./ex check L12     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what it **prints** is its result (it has no `return`).

- `void CountDown(int n)`: input = n, an int (whole number); result = the lines it writes with Console.Write / Console.WriteLine (no return).

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `CountDown(4)` | prints:<br>`4`<br>`3`<br>`2`<br>`1` |
| `CountDown(1)` | prints:<br>`1` |

## Edge cases to test

- `CountDown(0)` prints nothing.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Start at `n`. Step with `i--`.

</details>

<details><summary>Hint 2</summary>

Keep going while `i >= 1`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Count down from n to 0 (0 included).

## Solution

Only after a real try: [open the solution for L12](../../internal/solutions/L12_CountDown.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [L11 · Count from a to b](L11-count-from-a-to-b.md) · [Loops](../themes/loops.md) · Next: [L13 · Count by 3](L13-count-by-3.md)

</div>
