---
prev:
  text: "A09 · Min and max until zero"
  link: /exercises/A09-min-and-max-until-zero
next:
  text: "L08 · Guess the number"
  link: /exercises/L08-guess-the-number
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Until the user stops](../themes/loops.md#until-the-user-stops) › L07

# L07 · Ask until valid

<ExerciseHeader />

<div class="gh-only">

**Loops › Until the user stops** · exercise 4 of 5 in this group (38 of 81 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Independent | medium | write code | [Input validation](../cookbook/09-input-validation.md) | [L05](L05-until-zero.md), [C03](C03-ticket-price.md) |

</div>

## Goal

Ask for a number between 1 and 10. If the text is not a number, or is out of range, print `Invalid, try again.` and ask again. At the end print `You chose X`. New here: `int.TryParse(text, out int number)` gives back `false` instead of crashing when the text is not a number.

## Start and check

```bash
./ex start L07     # creates practice/L07_AskUntilValid.cs (never overwrites your work)
./ex check L07     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** write the whole program inside `Run()`: read with `Console.ReadLine()`, print with `Console.WriteLine()`.

## Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `abc`, `42`, `7`

```text
Invalid, try again.
Invalid, try again.
You chose 7
```

**Example 2** — input: `1`

```text
You chose 1
```

## Edge cases to test

- `abc` must not crash the program.
- 1 and 10 are valid; 0 and 11 are not.

## Rules

- Use `do … while` and `int.TryParse`.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

See the [input validation recipe](../cookbook/09-input-validation.md).

</details>

<details><summary>Hint 2</summary>

`bool ok = int.TryParse(text, out int number);` gives `false` for `abc`.

</details>

<details><summary>Hint 3</summary>

Loop condition: `while (!valid)`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Ask for a password until it has at least 8 characters (`text.Length`).

## Solution

Only after a real try: [open the solution for L07](../../internal/solutions/L07_AskUntilValid.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [A09 · Min and max until zero](A09-min-and-max-until-zero.md) · [Loops](../themes/loops.md) · Next: [L08 · Guess the number](L08-guess-the-number.md)

</div>
