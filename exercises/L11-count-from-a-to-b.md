[Home](../README.md) › [Exercises](README.md) › [Loops: repeat and count](../themes/loops-repeat.md) › L11

# L11 · Count from a to b

| Level | Difficulty | Theme | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | easy | [Loops: repeat and count](../themes/loops-repeat.md) | [Counter loop](../cookbook/01-counter-loop.md) | [L03](L03-count-up-and-down.md) | Custom |

## Goal

Print the numbers from `a` to `b` (both included), one per line.

## Start and check

```bash
./ex start L11     # creates practice/L11_CountFromAToB.cs (never overwrites your work)
./ex check L11     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in this method in the file. The *parameters* are its input; what it **prints** is its result (it has no `return`).

- `void PrintFromTo(int a, int b)`: input = a, an int (whole number), b, an int (whole number); result = the lines it writes with Console.Write / Console.WriteLine (no return).

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `PrintFromTo(3, 6)` | prints:<br>`3`<br>`4`<br>`5`<br>`6` |
| `PrintFromTo(5, 5)` | prints:<br>`5` |
| `PrintFromTo(-2, 1)` | prints:<br>`-2`<br>`-1`<br>`0`<br>`1` |

## Edge cases to test

- `a` equal to `b`: one line.
- `a` bigger than `b`: nothing is printed.

## Rules

- Write the loop yourself.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

The counter starts at `a`, not at 1.

</details>

<details><summary>Hint 2</summary>

The test is `i <= b`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Print from `a` to `b` but skip `a` itself.

## Solution

Only after a real try: [open the solution for L11](../solutions/L11_CountFromAToB.cs). Your solution can be different and still correct!

---

Previous: [L08 · Guess the number](L08-guess-the-number.md) · [All exercises](README.md) · Next: [L12 · Count down](L12-count-down.md)
