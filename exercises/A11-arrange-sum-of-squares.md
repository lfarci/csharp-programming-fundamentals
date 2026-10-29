[Home](../README.md) › [Exercises](README.md) › [Loops: keep a running result](../themes/loops-running-result.md) › A11

# A11 · Arrange the lines: sum of squares

| Level | Difficulty | Theme | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | easy | [Loops: keep a running result](../themes/loops-running-result.md) | [Accumulator](../cookbook/02-accumulator.md) | [L03](L03-count-up-and-down.md) | Custom |

## Goal

Give back 1² + 2² + … + n². `SumOfSquares(3)` is 1 + 4 + 9 = 14. All the lines are given, mixed up: put them in order.

## Start and check

```bash
./ex start A11     # creates practice/A11_ArrangeSumOfSquares.cs (never overwrites your work)
./ex check A11     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** the file already holds **all** the lines you need, mixed up and turned into comments (`//`). Put them in order and remove the `//`. No new code to invent: this trains *reading* the pattern.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `SumOfSquares(3)` | `14` |
| `SumOfSquares(1)` | `1` |
| `SumOfSquares(0)` | `0` |
| `SumOfSquares(10)` | `385` |

## Edge cases to test

- `SumOfSquares(0)` must give 0: does your order still work?

## Rules

- Use **every** line once. Do not add new lines; you only remove the `//` and change the order.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Which line must come before the loop? Which one after it?

</details>

<details><summary>Hint 2</summary>

The `{` and `}` lines show what is inside the loop.

</details>

<details><summary>Hint 3</summary>

Order: box, loop header, `{`, update, `}`, return.

</details>

## Mastery check

Solve this variation **alone**, on another day:

On paper, mix up the 6 lines of A04 factorial and give them to a friend (or to yourself tomorrow) to arrange.

## Solution

Only after a real try: [open the solution for A11](../solutions/A11_ArrangeSumOfSquares.cs). Your solution can be different and still correct!

---

Previous: [L19 · Count the turns](L19-count-the-turns.md) · [All exercises](README.md) · Next: [A01 · Sum from 1 to N](A01-sum-1-to-n.md)
