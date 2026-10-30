---
prev:
  text: "L06 · Even numbers"
  link: /exercises/L06-even-numbers
next:
  text: "L18 · Square numbers"
  link: /exercises/L18-squares
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Count](../themes/loops-count.md) › L17

# L17 · Count down by 2

<ExerciseHeader />

<div class="gh-only">

**Loops › Count** · exercise 10 of 13 in this group (10 of 86 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | [Counter loop](../cookbook/01-counter-loop.md) | [L12](L12-count-down.md) |

</div>

## Goal

Print n, n−2, n−4, … while the number is at least 1, one per line.

## Start and check

```bash
./ex start L17     # creates practice/L17_CountDownBy2.cs (never overwrites your work)
./ex check L17     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what it **prints** is its result (it has no `return`).

- `void CountDownBy2(int n)`: input = n, an int (whole number); result = the lines it writes with Console.Write / Console.WriteLine (no return).

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `CountDownBy2(9)` | prints:<br>`9`<br>`7`<br>`5`<br>`3`<br>`1` |
| `CountDownBy2(6)` | prints:<br>`6`<br>`4`<br>`2` |

## Edge cases to test

- n = 1: one line.

`./ex check` tests these too: `CountDownBy2(1)` prints `1`.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

L12 with a step of `i -= 2`.

</details>

<details><summary>Hint 2</summary>

Test `i >= 1`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Count down by 3 from n.

## Solution

Only after a real try: [open the solution for L17](../../internal/solutions/L17_CountDownBy2.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [L06 · Even numbers](L06-even-numbers.md) · [Loops](../themes/loops.md) · Next: [L18 · Square numbers](L18-squares.md)

</div>
