---
prev:
  text: "N01 · Armstrong with methods"
  link: /exercises/N01-armstrong-with-methods
next:
  text: "E01 · Safe number reader"
  link: /exercises/E01-safe-number-reader
---

[Home](../../README.md) › [Exercises](README.md) › [Methods and errors](../themes/methods.md) › [Errors](../themes/methods.md#errors) › E02

# E02 · Parse or zero

<ExerciseHeader />

<div class="gh-only">

**Methods and errors › Errors** · exercise 1 of 2 in this group (3 of 4 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | write code | — | [L07](L07-ask-until-valid.md) |

</div>

## Goal

Give back the number written in `text`, or 0 when `text` is not a whole number. It must never crash.

## Start and check

```bash
./ex start E02     # creates practice/E02_ParseOrZero.cs (never overwrites your work)
./ex check E02     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what you `return` is its result.

- `int ParseOrZero(string text)`: input = text, a string (text); result = an int (whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `ParseOrZero("42")` | `42` |
| `ParseOrZero("abc")` | `0` |
| `ParseOrZero("")` | `0` |
| `ParseOrZero("-7")` | `-7` |

## Edge cases to test

- Empty text: 0.
- A negative number like `-7` is a number.

## Rules

- Use `int.TryParse`, not `int.Parse`.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [reading worksheet](../docs/reading-an-exercise.md#the-template): what goes in? what comes out? a tiny example by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

`int.TryParse(text, out int number)` gives back `true` and fills `number` when the text is a number.

</details>

<details><summary>Hint 2</summary>

`if (int.TryParse(text, out int number)) return number;` then `return 0;` after it.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Write `ParseOrDefault(string text, int fallback)` that gives back `fallback` instead of 0.

## Solution

Only after a real try: [open the solution for E02](../../internal/solutions/E02_ParseOrZero.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [N01 · Armstrong with methods](N01-armstrong-with-methods.md) · [Methods and errors](../themes/methods.md) · Next: [E01 · Safe number reader](E01-safe-number-reader.md)

</div>
