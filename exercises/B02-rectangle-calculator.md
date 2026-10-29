[Home](../README.md) › [Exercises](README.md) › [Variables and expressions](../themes/variables.md) › B02

# B02 · Rectangle calculator

| Level | Difficulty | Theme | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | easy | [Variables and expressions](../themes/variables.md) | — | [B01](B01-hello-you.md) | Custom |

## Goal

`Area` gives back width × height. `Perimeter` gives back 2 × (width + height).

## Start and check

```bash
./ex start B02     # creates practice/B02_RectangleCalculator.cs (never overwrites your work)
./ex check B02     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** fill in these methods in the file. The *parameters* are its input; what you `return` is its result.

- `int Area(int width, int height)`: input = width, an int (whole number), height, an int (whole number); result = an int (whole number), given back with return.
- `int Perimeter(int width, int height)`: input = width, an int (whole number), height, an int (whole number); result = an int (whole number), given back with return.

## Examples

Your method must give these results. `./ex check` tests all of them.

| Call | Result |
| --- | --- |
| `Area(4, 3)` | `12` |
| `Perimeter(4, 3)` | `14` |
| `Area(5, 5)` | `25` |
| `Perimeter(5, 5)` | `20` |
| `Area(0, 7)` | `0` |

## Edge cases to test

- A width of 0 gives an area of 0.

## Rules

- Use `*`, `+` and `return`. No `if` needed.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [reading worksheet](../docs/reading-an-exercise.md#the-template): what goes in? what comes out? a tiny example by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Area = width × height. Perimeter = 2 × (width + height).

</details>

<details><summary>Hint 2</summary>

Each method is one line: `return width * height;`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Do the same for a circle with a `double` radius (area = π × r², use `Math.PI`).

## Solution

Only after a real try: [open the solution for B02](../solutions/B02_RectangleCalculator.cs). Your solution can be different and still correct!

---

Previous: [B01 · Hello you](B01-hello-you.md) · [All exercises](README.md) · Next: [B03 · Seconds to hours, minutes, seconds](B03-seconds-to-hms.md)
