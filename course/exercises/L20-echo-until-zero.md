---
prev:
  text: "A08 · Multiples of 3 or 5"
  link: /exercises/A08-multiples-of-3-or-5
next:
  text: "L21 · Sum until -1"
  link: /exercises/L21-sum-until-minus-one
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Until the user stops](../themes/loops-until-the-user-stops.md) › L20

# L20 · Echo until zero

<ExerciseHeader />

<div class="gh-only">

**Loops › Until the user stops** · exercise 1 of 8 in this group (47 of 99 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | [Sentinel loop](../cookbook/10-sentinel-loop.md) | [L03](L03-count-up-and-down.md) |

</div>

## Goal

Read whole numbers one by one. For each one, print `You typed X`. Stop when the user types 0, then print `Bye.`

## Start and check

```bash
./ex start L20     # creates practice/L20_EchoUntilZero.cs (never overwrites your work)
./ex check L20     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** write the whole program inside `Run()`: read with `Console.ReadLine()`, print with `Console.WriteLine()`.

## Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `5`, `8`, `0`

```text
You typed 5
You typed 8
Bye.
```

**Example 2** — input: `-3`, `0`

```text
You typed -3
Bye.
```

**Example 3** — input: `0`

```text
Bye.
```

## Edge cases to test

- The first number is already 0: only `Bye.` is printed.
- The 0 itself is not echoed: try it with `./ex run L20`.

## Rules

- You do not know how many numbers will come: use `while (true)` and `break`.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

This is the [sentinel loop](../cookbook/10-sentinel-loop.md). 0 is the sentinel.

</details>

<details><summary>Hint 2</summary>

In the loop, in this order: read, `if (value == 0) break;`, then print.

</details>

<details><summary>Hint 3</summary>

`Bye.` comes after the loop, so it is printed once.

</details>

## Mastery check

Solve this variation **alone**, on another day:

For each number, print `You typed X (even)` or `You typed X (odd)`.

## Solution

Only after a real try: [open the solution for L20](../../internal/solutions/L20_EchoUntilZero.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [A08 · Multiples of 3 or 5](A08-multiples-of-3-or-5.md) · [Loops](../themes/loops.md) · Next: [L21 · Sum until -1](L21-sum-until-minus-one.md)

</div>
