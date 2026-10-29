[Home](../README.md) › [Roadmap](../ROADMAP.md) › [Exercises](README.md) › L06

# L06 · Even numbers

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | easy | 4a · Repeat & count | [Counter loop](../cookbook/01-counter-loop.md) | [L03](L03-count-up-and-down.md) | Custom |

## Goal

Read N. Print all even numbers from 2 to N on one line.

## Start and check

```bash
./ex start L06     # creates practice/L06_EvenNumbers.cs (never overwrites your work)
./ex check L06     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#5-do-one-exercise).

**Your job:** write the whole program inside `Run()`: read with `Console.ReadLine()`, print with `Console.WriteLine()`.

## Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `9`

```text
2 4 6 8
```

**Example 2** — input: `10`

```text
2 4 6 8 10
```

**Example 3** — input: `1`

```text
(nothing is printed)
```

## Edge cases to test

- N = 1 → nothing is printed.
- N is even → N is printed too.

## Rules

- Write it **two ways**: (1) step `i += 2`, (2) step `i++` with an `if`.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Way 1: start at 2, step 2.

</details>

<details><summary>Hint 2</summary>

Way 2: test every number with `i % 2 == 0`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Print the multiples of 7 between 1 and N.

## Solution

Only after a real try: [open the solution for L06](../solutions/L06_EvenNumbers.cs). Your solution can be different and still correct!

---

Previous: [L05 · Until zero](L05-until-zero.md) · [All exercises](README.md) · Next: [L07 · Ask until valid](L07-ask-until-valid.md)
