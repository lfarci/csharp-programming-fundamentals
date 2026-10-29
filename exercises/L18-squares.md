[Home](../README.md) › [Exercises](README.md) › [Loops: repeat and count](../themes/loops-repeat.md) › L18

# L18 · Square numbers

| Level | Difficulty | Theme | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | easy | [Loops: repeat and count](../themes/loops-repeat.md) | [Counter loop](../cookbook/01-counter-loop.md) | [L11](L11-count-from-a-to-b.md) | Custom |

## Goal

Print 1², 2², …, n² (1, 4, 9, …), one per line.

## Start and check

```bash
./ex start L18     # creates practice/L18_Squares.cs (never overwrites your work)
./ex check L18     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what it **prints** is its result (it has no `return`).

- `void PrintSquares(int n)`: input = n, an int (whole number); result = the lines it writes with Console.Write / Console.WriteLine (no return).

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `PrintSquares(4)` | prints:<br>`1`<br>`4`<br>`9`<br>`16` |
| `PrintSquares(1)` | prints:<br>`1` |

## Edge cases to test

- n = 0: nothing.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

A normal 1 to n loop.

</details>

<details><summary>Hint 2</summary>

Print `i * i` instead of `i`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Print the cubes 1, 8, 27, … up to n³.

## Solution

Only after a real try: [open the solution for L18](../solutions/L18_Squares.cs). Your solution can be different and still correct!

---

Previous: [L17 · Count down by 2](L17-count-down-by-2.md) · [All exercises](README.md) · Next: [L19 · Count the turns](L19-count-the-turns.md)
