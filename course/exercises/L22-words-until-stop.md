---
prev:
  text: "L05 · Until zero"
  link: /exercises/L05-until-zero
next:
  text: "A06 · Average until zero"
  link: /exercises/A06-average-until-zero
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Until the user stops](../themes/loops-until-the-user-stops.md) › L22

# L22 · Words until stop

<ExerciseHeader />

<div class="gh-only">

**Loops › Until the user stops** · exercise 4 of 8 in this group (50 of 99 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Independent | medium | write code | [Sentinel loop](../cookbook/10-sentinel-loop.md) | [L05](L05-until-zero.md) |

</div>

## Goal

Read words one by one. Stop when the user types `stop`. Print how many words came before it.

## Start and check

```bash
./ex start L22     # creates practice/L22_WordsUntilStop.cs (never overwrites your work)
./ex check L22     # tests your code with the examples below
```

On Windows, type `.\ex` instead of `./ex`. More in [Getting started](../docs/getting-started.md#start-your-first-exercise).

**Your job:** write the whole program inside `Run()`: read with `Console.ReadLine()`, print with `Console.WriteLine()`.

## Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `cat`, `dog`, `stop`

```text
You typed 2 words.
```

**Example 2** — input: `red`, `green`, `blue`, `stop`

```text
You typed 3 words.
```

**Example 3** — input: `stop`

```text
You typed 0 words.
```

## Edge cases to test

- The first word is already `stop`: 0 words.
- `stop` itself is not counted.

## Rules

- Same loop as L05; only the stop test changes.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Read the text as it is: `string word = Console.ReadLine()!;` (no `int.Parse`).

</details>

<details><summary>Hint 2</summary>

The sentinel test compares text: `if (word == "stop") break;`.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Also print the longest word (`word.Length`).

## Solution

Only after a real try: [open the solution for L22](../../internal/solutions/L22_WordsUntilStop.cs). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [L05 · Until zero](L05-until-zero.md) · [Loops](../themes/loops.md) · Next: [A06 · Average until zero](A06-average-until-zero.md)

</div>
