[Home](../README.md) › [Roadmap](../ROADMAP.md) › [Exercises](README.md) › L10

# L10 · Numbers on one line

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Independent | medium | 4c · Draw in 2D | [Counter loop](../cookbook/01-counter-loop.md), [Nested grid](../cookbook/08-nested-grid.md) | [L09](L09-draw-a-row.md) | Custom |

## Goal

Print the numbers 1 to n on one line, with one space between them, then end the line. `PrintNumbers(4)` prints `1 2 3 4`.

## Start and check

```bash
./ex start L10     # creates practice/L10_NumbersOnOneLine.cs (never overwrites your work)
./ex check L10     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#5-do-one-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what it **prints** is its result (it has no `return`).

- `void PrintNumbers(int n)`: input = n, an int (whole number); result = the lines it writes with Console.Write / Console.WriteLine (no return).

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `PrintNumbers(4)` | prints:<br>`1 2 3 4` |
| `PrintNumbers(1)` | prints:<br>`1` |
| `PrintNumbers(0)` | prints:<br>`` |

## Edge cases to test

- `PrintNumbers(1)` prints just `1`: no space at the end.
- `PrintNumbers(0)` prints only the line break.

## Rules

- No space after the last number. Use one `if` inside the loop.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Print the number with `Console.Write(i)`.

</details>

<details><summary>Hint 2</summary>

A space goes **between** numbers: before every number except the first (`if (i > 1)`).

</details>

<details><summary>Hint 3</summary>

After the loop, one `Console.WriteLine()`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Print `n` down to 1 on one line, separated by `, ` (`3, 2, 1`).

## Solution

Only after a real try: [open the solution for L10](../solutions/L10_NumbersOnOneLine.cs). Your solution can be different and still correct!

---

Previous: [L09 · Draw one row](L09-draw-a-row.md) · [All exercises](README.md) · Next: [G07 · Arrange the lines: a square](G07-arrange-a-square.md)
