[Home](../README.md) › [Exercises](README.md) › [Loops: repeat and count](../themes/loops-repeat.md) › L16

# L16 · Odd numbers

| Level | Difficulty | Theme | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | easy | [Loops: repeat and count](../themes/loops-repeat.md) | [Counter loop](../cookbook/01-counter-loop.md) | [L11](L11-count-from-a-to-b.md) | Custom |

## Goal

Print the odd numbers 1, 3, 5, … up to n, one per line.

## Start and check

```bash
./ex start L16     # creates practice/L16_OddNumbers.cs (never overwrites your work)
./ex check L16     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what it **prints** is its result (it has no `return`).

- `void PrintOdds(int n)`: input = n, an int (whole number); result = the lines it writes with Console.Write / Console.WriteLine (no return).

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `PrintOdds(7)` | prints:<br>`1`<br>`3`<br>`5`<br>`7` |
| `PrintOdds(8)` | prints:<br>`1`<br>`3`<br>`5`<br>`7` |
| `PrintOdds(1)` | prints:<br>`1` |

## Edge cases to test

- n even: the last number is n − 1.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Start at 1, step `i += 2`.

</details>

<details><summary>Hint 2</summary>

Compare with L06 (even numbers): only the start changes.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Print the odd numbers from n down to 1.

## Solution

Only after a real try: [open the solution for L16](../solutions/L16_OddNumbers.cs). Your solution can be different and still correct!

---

Previous: [L15 · Count by any step](L15-count-by-step.md) · [All exercises](README.md) · Next: [L17 · Count down by 2](L17-count-down-by-2.md)
