---
prev:
  text: "L01 · Trace a loop"
  link: /exercises/L01-trace-a-loop
next:
  text: "L03 · Count up and down"
  link: /exercises/L03-count-up-and-down
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Count](../themes/loops-count.md) › L02

# L02 · Boundaries: < or <=

<ExerciseHeader />

<div class="gh-only">

**Loops › Count** · exercise 2 of 13 in this group (2 of 86 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | paper | [Counter loop](../cookbook/01-counter-loop.md) | [L01](L01-trace-a-loop.md) |

</div>

## Goal

How many times does each loop run? What is the last value printed? Answer on paper first.

```csharp
for (int i = 1; i < 5; i++) Console.WriteLine(i);   // loop A
for (int i = 1; i <= 5; i++) Console.WriteLine(i);  // loop B
for (int i = 0; i < 5; i++) Console.WriteLine(i);   // loop C
for (int i = 5; i >= 1; i--) Console.WriteLine(i);  // loop D
int k = 10;
while (k < 5) { Console.WriteLine(k); k++; }         // loop E
```

## Start and check

This one is on **paper**: no code to write. When you are done, compare with the answer key (link at the bottom).

## Edge cases to test

- Loop E: can a loop run zero times?

## Rules

- Paper first. Then run to check.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

For each loop: write the first value, the last value that passes the test, and count.

</details>

<details><summary>Hint 2</summary>

`i < 5` and `i <= 4` mean the same thing for whole numbers.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Write 3 different `for` loops that all run exactly 7 times.

## Solution

Only after a real try: [open the solution for L02](../answer-keys/L02-boundaries.md). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [L01 · Trace a loop](L01-trace-a-loop.md) · [Loops](../themes/loops.md) · Next: [L03 · Count up and down](L03-count-up-and-down.md)

</div>
