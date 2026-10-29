[Home](../../README.md) › [Roadmap](../ROADMAP.md) › Theme 3 of 4

# Arrays, text and lists

Keep many values in one variable, work on text letter by letter, save to a file, use a `List`.

<LearnCard theme="arrays" />

<div class="gh-only">

**Before you start:**

1. **Watch:** [Understanding Arrays](../learn/videos/understanding-arrays.md) (17 min)
2. **Read:** [Organize data with arrays and lists in C#](https://learn.microsoft.com/en-us/training/modules/csharp-arrays-lists/) (Microsoft Learn, Part 2)
3. **Then practise:** [R01 · Sum of an array](../exercises/R01-sum-an-array.md)

<details><summary>More on Microsoft Learn</summary>

- **Modules:** [Perform operations on arrays using helper methods in C#](https://learn.microsoft.com/en-us/training/modules/csharp-arrays-operations/) (Part 4) · [Modify the content of strings using built-in string data type methods in C#](https://learn.microsoft.com/en-us/training/modules/csharp-modify-content/) (Part 4) · [Format alphanumeric data for presentation in C#](https://learn.microsoft.com/en-us/training/modules/csharp-format-strings/) (Part 4) · [Read and write files in C#](https://learn.microsoft.com/en-us/training/modules/csharp-read-write-files/) (Part 2)
- **Videos:** [Working with Strings](../learn/videos/working-with-strings.md) · [Working with Collections](../learn/videos/working-with-collections.md)
- **Reference:** [Arrays](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/arrays) · [Collections tutorial](https://learn.microsoft.com/en-us/dotnet/csharp/tour-of-csharp/tutorials/list-collection)

</details>

</div>

## After this theme you can

- create an array and read `values[i]` without going out of range
- reuse a loop recipe on an array or a string
- write lines to a file and read them back
- choose between an array and a `List`

## The groups

Do the groups in order, and the exercises of a group from top to bottom. Tick each one when `./ex check` says DONE.

<ThemeGroups theme="arrays" />

<div class="gh-only">

1. [Arrays](#arrays): Visit every element with `values[i]`. (6 exercises)
2. [Text](#text): A string is an array of letters. (3 exercises)
3. [Files and lists](#files-and-lists): Save values in a file; use a list that grows. (2 exercises)

</div>

## Arrays

Visit every element with `values[i]`. Lesson: [Recipe 11 · Array traversal](../cookbook/11-array-traversal.md).

<ThemeExercises theme="arrays" group="arrays" />

<div class="gh-only">

| ID | Exercise | Kind | Level | Effort |
| --- | --- | --- | --- | --- |
| R01 | [Sum of an array](../exercises/R01-sum-an-array.md) | write code | Guided | easy |
| R03 | [Count matches](../exercises/R03-count-matches.md) | write code | Independent | easy |
| R02 | [Position of the largest](../exercises/R02-largest-in-an-array.md) | write code | Independent | medium |
| R06 | [Fix: largest value](../exercises/R06-fix-largest-value.md) | fix the bugs | Independent | medium |
| R04 | [Find the position](../exercises/R04-find-the-position.md) | write code | Independent | medium |
| R05 | [Reverse an array](../exercises/R05-reverse-an-array.md) | write code | Challenge | medium |

</div>

## Text

A string is an array of letters. Lesson: [Recipe 12 · Build a string](../cookbook/12-string-building.md).

<ThemeExercises theme="arrays" group="text" />

<div class="gh-only">

| ID | Exercise | Kind | Level | Effort |
| --- | --- | --- | --- | --- |
| T01 | [Count a letter](../exercises/T01-count-a-letter.md) | write code | Guided | easy |
| T02 | [Remove spaces](../exercises/T02-remove-spaces.md) | write code | Independent | easy |
| T03 | [Keep the digits](../exercises/T03-count-and-keep-digits.md) | write code | Challenge | medium |

</div>

## Files and lists

Save values in a file; use a list that grows. Lesson: [Recipe 11 · Array traversal](../cookbook/11-array-traversal.md).

<ThemeExercises theme="arrays" group="files-and-lists" />

<div class="gh-only">

| ID | Exercise | Kind | Level | Effort |
| --- | --- | --- | --- | --- |
| F01 | [Save numbers to a file](../exercises/F01-numbers-file.md) | write code | Independent | medium |
| K01 | [Shopping list](../exercises/K01-shopping-list.md) | write code | Independent | medium |

</div>

## Ready for the next theme when

You can explain the difference between `i` (the position) and `values[i]` (the value).

---

Previous: [Loops](loops.md) · [Roadmap](../ROADMAP.md) · Next: [Methods and errors](methods.md)
