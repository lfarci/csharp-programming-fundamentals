---
prev:
  text: "E02 · Parse or zero"
  link: /exercises/E02-parse-or-zero
next:
  text: "Roadmap"
  link: /ROADMAP
---

[Home](../README.md) › [Exercises](README.md) › [Methods and errors](../themes/methods.md) › [Errors](../themes/methods.md#errors) › E01

# E01 · Safe number reader

<ExerciseHeader />

<div class="gh-only">

**Methods and errors › Errors** · exercise 2 of 2 in this group (4 of 4 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Independent | medium | write code | [Input validation](../cookbook/09-input-validation.md) | [L07](L07-ask-until-valid.md) |

</div>

## Goal

Ask for a whole number. Use `int.Parse` inside `try`/`catch`: if it fails, print `That is not a number.` and ask again. At the end print `Thanks: X`.

## Start and check

```bash
./ex start E01     # creates practice/E01_SafeNumberReader.cs (never overwrites your work)
./ex check E01     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** write the whole program inside `Run()`: read with `Console.ReadLine()`, print with `Console.WriteLine()`.

## Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `abc`, `12x`, `42`

```text
That is not a number.
That is not a number.
Thanks: 42
```

## Edge cases to test

- Empty input also fails.

## Rules

- Use `try`/`catch (FormatException)` (not `TryParse`, which you used in L07).
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Loop until it works: `while (true) { try { ... break; } catch (FormatException) { ... } }`.

</details>

<details><summary>Hint 2</summary>

`break` goes **after** the `int.Parse` line inside `try`: it only runs if parsing worked.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Also catch `OverflowException` (try `99999999999`) with its own message.

## Solution

Only after a real try: [open the solution for E01](../solutions/E01_SafeNumberReader.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [E02 · Parse or zero](E02-parse-or-zero.md) · [Methods and errors](../themes/methods.md) · Next: [Roadmap](../ROADMAP.md)

</div>
