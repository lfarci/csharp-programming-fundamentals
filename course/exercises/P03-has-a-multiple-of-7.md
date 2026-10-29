---
prev:
  text: "S03 · Even Fibonacci sum"
  link: /exercises/S03-even-fibonacci-sum
next:
  text: "P04 · Has an even digit"
  link: /exercises/P04-has-an-even-digit
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Search and combine](../themes/loops.md#search-and-combine) › P03

# P03 · Has a multiple of 7

<ExerciseHeader />

<div class="gh-only">

**Loops › Search and combine** · exercise 1 of 9 in this group (73 of 81 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | [Flag/search](../cookbook/05-flag-search.md) | [A16](A16-count-multiples-of-5.md) |

</div>

## Goal

Give back `true` if at least one number from `a` to `b` is divisible by 7.

## Start and check

```bash
./ex start P03     # creates practice/P03_HasAMultipleOf7.cs (never overwrites your work)
./ex check P03     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `bool HasMultipleOf7(int a, int b)`: input = a, an int (whole number), b, an int (whole number); result = a bool (true or false), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `HasMultipleOf7(1, 6)` | `false` |
| `HasMultipleOf7(1, 7)` | `true` |
| `HasMultipleOf7(10, 20)` | `true` |
| `HasMultipleOf7(15, 20)` | `false` |

## Edge cases to test

- `a` bigger than `b`: no number, so `false`.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

A flag box: `bool found = false;` before the loop. It means: not found yet.

</details>

<details><summary>Hint 2</summary>

Inside the loop: `if (i % 7 == 0) found = true;`. After the loop: `return found;`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Give back `true` if at least one number from `a` to `b` is divisible by `k`.

## Solution

Only after a real try: [open the solution for P03](../../internal/solutions/P03_HasAMultipleOf7.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [S03 · Even Fibonacci sum](S03-even-fibonacci-sum.md) · [Loops](../themes/loops.md) · Next: [P04 · Has an even digit](P04-has-an-even-digit.md)

</div>
