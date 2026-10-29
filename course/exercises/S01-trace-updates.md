---
prev:
  text: "D06 · Palindrome number"
  link: /exercises/D06-palindrome-number
next:
  text: "S04 · Doubling"
  link: /exercises/S04-doubling
---

[Home](../../README.md) › [Exercises](README.md) › [Loops](../themes/loops.md) › [Changing values](../themes/loops.md#changing-values) › S01

# S01 · Trace two variables

<ExerciseHeader />

<div class="gh-only">

**Loops › Changing values** · exercise 1 of 5 in this group (68 of 81 in the theme)

| Level | Effort | Kind | Recipes | Do these first |
| --- | --- | --- | --- | --- |
| Guided | easy | paper | [State update](../cookbook/07-state-update.md) | [L01](L01-trace-a-loop.md) |

</div>

## Goal

Without running it, fill a trace table (`turn`, `next`, `a`, `b`) for this code. Then run it to check.

```csharp
int a = 1;
int b = 2;
for (int i = 1; i <= 3; i++)
{
    int next = a + b;
    a = b;
    b = next;
    Console.WriteLine($"a={a} b={b}");
}
```

Then swap the two middle lines (`b = next;` before `a = b;`). What changes? Why?

## Start and check

This one is on **paper**: no code to write. When you are done, compare with the answer key (link at the bottom).

## Edge cases to test

- Order of the assignments.

## Rules

- Paper first.
- No LINQ and no ready-made helpers: you write every step yourself.

## Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## Hints (open one at a time)

<details><summary>Hint 1</summary>

Each line runs **one after the other**, not all at the same time.

</details>

<details><summary>Hint 2</summary>

Turn 1: next = 1 + 2 = 3, then a = 2, then b = 3.

</details>

## Mastery check

Solve this variation **alone**, on another day:

Predict the output when `a = 0` and `b = 1` and the loop runs 6 times. Which famous sequence is it?

## Solution

Only after a real try: [open the solution for S01](../answer-keys/S01-trace-updates.md). Your solution can be different and still correct!

---

<div class="gh-only">

Previous: [D06 · Palindrome number](D06-palindrome-number.md) · [Loops](../themes/loops.md) · Next: [S04 · Doubling](S04-doubling.md)

</div>
