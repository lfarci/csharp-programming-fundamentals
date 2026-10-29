[Home](../README.md) › [Roadmap](../ROADMAP.md) › [Exercises](README.md) › L01

# L01 · Trace a loop (paper)

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | easy | 4a · Repeat & count | [Counter loop](../cookbook/01-counter-loop.md) | [C01](C01-even-or-odd.md) | Custom |

## Goal

Without running it, predict the output of this loop and fill a trace table.

```csharp
for (int i = 2; i <= 8; i += 2)
{
    Console.WriteLine(i);
}
```

Table columns: `turn`, `i at start`, `i <= 8?`, `output`, `i after step`.

## Start and check

This one is on **paper**: no code to write. When you are done, compare with the answer key (link at the bottom).

## Edge cases to test

- What is the value of `i` when the loop stops? Is it printed?

## Rules

- Paper and pen only. Run the code **after** to check.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Start: `i = 2`. Test `2 <= 8` → yes → print 2 → step `i = 4`.

</details>

<details><summary>Hint 2</summary>

Keep going until the test is false. Write the line where the test fails too.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Predict `for (int i = 10; i > 0; i -= 3)` without running it.

## Solution

Only after a real try: [open the solution for L01](../solutions/L01-trace-a-loop.md). Your solution can be different and still correct!

---

Previous: [C04 · Grade from a score](C04-grade-from-a-score.md) · [All exercises](README.md) · Next: [L02 · Boundaries: < or <= ? (paper)](L02-boundaries.md)
