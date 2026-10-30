---
prev:
  text: "Basics"
  link: /themes/basics
next:
  text: "B02 · Rectangle calculator"
  link: /exercises/B02-rectangle-calculator
---

[Home](../../README.md) › [Exercises](README.md) › [Basics](../themes/basics.md) › [First programs](../themes/basics-first-programs.md) › B01

# B01 · Hello you

<ExerciseHeader />

<div class="gh-only">

**Basics › First programs** · exercise 1 of 3 in this group (1 of 7 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | — | — |

</div>

## Goal

Ask the user for their name and greet them.

## Start and check

```bash
./ex start B01     # creates practice/B01_HelloYou.cs (never overwrites your work)
./ex check B01     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** write the whole program inside `Run()`: read with `Console.ReadLine()`, print with `Console.WriteLine()`.

## Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `Ada`

```text
Hello, Ada!
```

**Example 2** — input: `Sam`

```text
Hello, Sam!
```

## Edge cases to test

- An empty name: what does your program print? (`Hello, !` is OK for now.)

`./ex check` tests these too: input *(empty)* prints `Hello, !`.

## Rules

- Use `Console.Write`, `Console.ReadLine` and `Console.WriteLine`.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [reading worksheet](../docs/reading-an-exercise.md#the-template): what goes in? what comes out? a tiny example by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

`Console.ReadLine()` gives you the text the user typed. Store it in a `string` variable.

</details>

<details><summary>Hint 2</summary>

Glue text together with `+`, or use interpolation: `$"Hello, {name}!"`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Ask for a first name **and** a city, and print `Ada lives in Brussels.`

## Solution

Only after a real try: [open the solution for B01](../../internal/solutions/B01_HelloYou.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [Basics](../themes/basics.md) · [Basics](../themes/basics.md) · Next: [B02 · Rectangle calculator](B02-rectangle-calculator.md)

</div>
