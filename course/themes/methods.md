[Home](../../README.md) › [Roadmap](../ROADMAP.md) › Theme 4 of 4

# Methods and errors

Split a program into small methods, and stop bad input from crashing it.

<LearnCard theme="methods" />

<div class="gh-only">

**Before you start:**

1. **Watch:** [Defining and Calling Methods](../learn/videos/defining-and-calling-methods.md) (31 min)
2. **Read:** [Write your first C# method](https://learn.microsoft.com/en-us/training/modules/write-first-c-sharp-method/) (Microsoft Learn, Part 5)
3. **Then practise:** [N02 · A method that calls one](../exercises/N02-is-multiple-and-count.md)

<details><summary>More on Microsoft Learn</summary>

- **Modules:** [Create C# methods with parameters](https://learn.microsoft.com/en-us/training/modules/create-c-sharp-methods-parameters/) (Part 5) · [Create C# methods that return values](https://learn.microsoft.com/en-us/training/modules/create-c-sharp-methods-return-values/) (Part 5) · [Write reusable code in C#](https://learn.microsoft.com/en-us/training/modules/csharp-reusable-code/) (Part 2) · [Review the principles of code debugging and exception handling](https://learn.microsoft.com/en-us/training/modules/review-principles-code-debugging-exception-handling-c-sharp/) (Part 6) · [Implement exception handling in C# console applications](https://learn.microsoft.com/en-us/training/modules/implement-exception-handling-c-sharp/) (Part 6) · [Create and throw exceptions in C# console applications](https://learn.microsoft.com/en-us/training/modules/create-throw-exceptions-c-sharp/) (Part 6)
- **Videos:** [Gracefully Handling Exceptions](../learn/videos/gracefully-handling-exceptions.md)
- **Reference:** [Methods](https://learn.microsoft.com/en-us/dotnet/csharp/methods) · [Exceptions](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/exceptions/)

</details>

</div>

## After this theme you can

- write a method with parameters and a `return`, and call it from another method
- use `int.TryParse` or `try` / `catch`

## The groups

Do the groups in order, and the exercises of a group from top to bottom. Tick each one when `./ex check` says DONE.

<ThemeGroups theme="methods" />

<div class="gh-only">

1. [Methods](#methods): Give a recipe a name. (2 exercises)
2. [Errors](#errors): Bad input must not crash the program. (2 exercises)

</div>

## Methods

Give a recipe a name.

<ThemeExercises theme="methods" group="methods" />

<div class="gh-only">

| ID | Exercise | Kind | Level | Effort |
| --- | --- | --- | --- | --- |
| N02 | [A method that calls one](../exercises/N02-is-multiple-and-count.md) | write code | Guided | easy |
| N01 | [Armstrong with methods](../exercises/N01-armstrong-with-methods.md) | write code | Challenge | hard |

</div>

## Errors

Bad input must not crash the program. Lesson: [Recipe 9 · Input validation](../cookbook/09-input-validation.md).

<ThemeExercises theme="methods" group="errors" />

<div class="gh-only">

| ID | Exercise | Kind | Level | Effort |
| --- | --- | --- | --- | --- |
| E02 | [Parse or zero](../exercises/E02-parse-or-zero.md) | write code | Guided | easy |
| E01 | [Safe number reader](../exercises/E01-safe-number-reader.md) | write code | Independent | medium |

</div>

## Ready for the next theme when

You can turn your Armstrong solution into 3 small methods, and typing `abc` does not crash your program.

---

Previous: [Arrays, text and lists](arrays.md) · [Roadmap](../ROADMAP.md)
