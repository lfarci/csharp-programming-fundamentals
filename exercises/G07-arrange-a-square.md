[Home](../README.md) › [Roadmap](../ROADMAP.md) › [Exercises](README.md) › G07

# G07 · Arrange the lines: a square

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | easy | 4c · Draw in 2D | [Nested grid](../cookbook/08-nested-grid.md) | [L09](L09-draw-a-row.md) | Custom |

## Goal

Print a square of `#`, `size` wide and `size` high. All the lines are given, mixed up: put them in order.

## Start and check

```bash
./ex start G07     # creates practice/G07_ArrangeASquare.cs (never overwrites your work)
./ex check G07     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#5-do-one-exercise).

**Your job:** the file already holds **all** the lines you need, mixed up and turned into comments (`//`). Put them in order and remove the `//`. No new code to invent: this trains *reading* the pattern.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `DrawSquare(3)` | prints:<br>`###`<br>`###`<br>`###` |
| `DrawSquare(1)` | prints:<br>`#` |

## Edge cases to test

- `DrawSquare(1)` prints one `#`.

## Rules

- Use every line once. You only remove the `//` and change the order.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Start from [L09 Draw one row](L09-draw-a-row.md): the inner loop is that row.

</details>

<details><summary>Hint 2</summary>

The outer loop repeats the whole row `size` times.

</details>

<details><summary>Hint 3</summary>

The `Console.WriteLine();` belongs to the outer loop, after the inner loop's `}`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Without looking, write `DrawRectangle(width, height)` from G01 on paper.

## Solution

Only after a real try: [open the solution for G07](../solutions/G07_ArrangeASquare.cs). Your solution can be different and still correct!

---

Previous: [L10 · Numbers on one line](L10-numbers-on-one-line.md) · [All exercises](README.md) · Next: [G01 · Draw a rectangle](G01-rectangle.md)
