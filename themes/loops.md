[Home](../README.md) › [Roadmap](../ROADMAP.md) › Theme 2 of 4

# Loops

Repeat code with `for` and `while`: count, add up, draw, take digits apart, search.

<LearnCard theme="loops" />

<div class="gh-only">

**Before you start:**

1. **Watch:** [for Iteration Statement](../learn/videos/for-iteration-statement.md) (18 min)
2. **Read:** [Iterate through a code block using for statement in C#](https://learn.microsoft.com/en-us/training/modules/csharp-for/) (Microsoft Learn, Part 3)
3. **Then practise:** [L01 · Trace a loop](../exercises/L01-trace-a-loop.md)

<details><summary>More on Microsoft Learn</summary>

- **Modules:** [Add looping logic to your code using the do-while and while statements in C#](https://learn.microsoft.com/en-us/training/modules/csharp-do-while/) (Part 3) · [Repeat actions with loops in C#](https://learn.microsoft.com/en-us/training/modules/csharp-repeat-actions-loops/) (Part 2) · [Control variable scope and logic using code blocks in C#](https://learn.microsoft.com/en-us/training/modules/csharp-code-blocks/) (Part 3) · [Guided project - Develop conditional branching and looping structures in C#](https://learn.microsoft.com/en-us/training/modules/guided-project-develop-conditional-branching-looping/) (Part 3) · [Challenge project - Develop branching and looping structures in C#](https://learn.microsoft.com/en-us/training/modules/challenge-project-develop-branching-looping-structures-c-sharp/) (Part 3) · [Implement the Visual Studio Code debugging tools for C#](https://learn.microsoft.com/en-us/training/modules/implement-visual-studio-code-debugging-tools/) (Part 6)
- **Videos:** [While Iteration Statement](../learn/videos/while-iteration-statement.md)
- **Reference:** [Iteration statements](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/iteration-statements)

</details>

</div>

## After this theme you can

- predict and trace a loop on paper, and find an off-by-one bug
- write a sum, a count and a product with a loop
- draw a rectangle and a triangle with a loop inside a loop
- take the digits of a number apart with `% 10` and `/ 10`
- update 2 or 3 variables in the right order
- answer a yes-or-no question with a `bool` flag

## The groups

Do the groups in order, and the exercises of a group from top to bottom. Tick each one when `./ex check` says DONE.

<ThemeGroups theme="loops" />

<div class="gh-only">

1. [Count](#count): One loop that prints numbers: change only the start, the test or the step. (13 exercises)
2. [Add up](#add-up): A box before the loop, an update inside, the result after. (12 exercises)
3. [Keep only some](#keep-only-some): The same box, with an `if` inside the loop. (9 exercises)
4. [Until the user stops](#until-the-user-stops): Read values until a stop value, or until the input is valid. (5 exercises)
5. [Draw rows and grids](#draw-rows-and-grids): One row, then the same row many times: a loop inside a loop. (8 exercises)
6. [Draw shapes](#draw-shapes): The inner loop depends on the row, or an `if` picks the character. (8 exercises)
7. [Digits](#digits): `% 10` gives the last digit, `/ 10` removes it. (12 exercises)
8. [Changing values](#changing-values): Keep the last values in variables, like Fibonacci. (5 exercises)
9. [Search and combine](#search-and-combine): A `bool` flag that starts false, `break` to stop early, then two recipes together. (9 exercises)

</div>

## Count

One loop that prints numbers: change only the start, the test or the step. Lesson: [Recipe 1 · Counter loop](../cookbook/01-counter-loop.md).

<ThemeExercises theme="loops" group="count" />

<div class="gh-only">

| ID | Exercise | Kind | Level | Effort |
| --- | --- | --- | --- | --- |
| L01 | [Trace a loop](../exercises/L01-trace-a-loop.md) | paper | Guided | easy |
| L02 | [Boundaries: < or <=](../exercises/L02-boundaries.md) | paper | Guided | easy |
| L03 | [Count up and down](../exercises/L03-count-up-and-down.md) | write code | Guided | easy |
| L11 | [Count from a to b](../exercises/L11-count-from-a-to-b.md) | write code | Guided | easy |
| L12 | [Count down](../exercises/L12-count-down.md) | write code | Guided | easy |
| L13 | [Count by 3](../exercises/L13-count-by-3.md) | write code | Guided | easy |
| L14 | [Count by 5](../exercises/L14-count-by-5.md) | write code | Guided | easy |
| L16 | [Odd numbers](../exercises/L16-odd-numbers.md) | write code | Guided | easy |
| L06 | [Even numbers](../exercises/L06-even-numbers.md) | write code | Guided | easy |
| L17 | [Count down by 2](../exercises/L17-count-down-by-2.md) | write code | Guided | easy |
| L18 | [Square numbers](../exercises/L18-squares.md) | write code | Guided | easy |
| L15 | [Count by any step](../exercises/L15-count-by-step.md) | write code | Independent | medium |
| L04 | [Multiplication table](../exercises/L04-multiplication-table.md) | write code | Independent | easy |

</div>

## Add up

A box before the loop, an update inside, the result after. Lesson: [Recipe 2 · Accumulator](../cookbook/02-accumulator.md).

<ThemeExercises theme="loops" group="add-up" />

<div class="gh-only">

| ID | Exercise | Kind | Level | Effort |
| --- | --- | --- | --- | --- |
| L19 | [Count the turns](../exercises/L19-count-the-turns.md) | write code | Guided | easy |
| A11 | [Arrange: sum of squares](../exercises/A11-arrange-sum-of-squares.md) | arrange the lines | Guided | easy |
| A01 | [Sum from 1 to N](../exercises/A01-sum-1-to-n.md) | write code | Guided | easy |
| A13 | [Sum from a to b](../exercises/A13-sum-from-a-to-b.md) | write code | Guided | easy |
| A14 | [Sum the odd numbers](../exercises/A14-sum-odd-numbers.md) | write code | Guided | easy |
| A18 | [Sum of cubes](../exercises/A18-sum-of-cubes.md) | write code | Guided | easy |
| A20 | [Power of 2](../exercises/A20-powers-of-2.md) | write code | Guided | easy |
| A19 | [Product from a to b](../exercises/A19-product-from-a-to-b.md) | write code | Guided | easy |
| A04 | [Factorial](../exercises/A04-factorial.md) | write code | Independent | medium |
| A07 | [Integer power](../exercises/A07-integer-power.md) | write code | Independent | medium |
| A05 | [Sum and sum of squares](../exercises/A05-sum-square-difference.md) | write code | Independent | medium |
| A10 | [Sum of a series](../exercises/A10-sum-of-a-series.md) | write code | Challenge | medium |

</div>

## Keep only some

The same box, with an `if` inside the loop. Lesson: [Recipe 3 · Conditional accumulator](../cookbook/03-conditional-accumulator.md).

<ThemeExercises theme="loops" group="keep-only-some" />

<div class="gh-only">

| ID | Exercise | Kind | Level | Effort |
| --- | --- | --- | --- | --- |
| A02 | [Count multiples of 3](../exercises/A02-count-multiples-of-3.md) | write code | Guided | easy |
| A15 | [Count the even numbers](../exercises/A15-count-even-numbers.md) | write code | Guided | easy |
| A16 | [Count multiples of 5](../exercises/A16-count-multiples-of-5.md) | write code | Guided | easy |
| A21 | [Count the divisors](../exercises/A21-count-divisors.md) | write code | Guided | easy |
| A22 | [Sum of the divisors](../exercises/A22-sum-of-divisors.md) | write code | Guided | easy |
| A12 | [Fix: multiples of 7](../exercises/A12-fix-count-multiples-of-7.md) | fix the bugs | Guided | easy |
| A03 | [Sum of the even numbers](../exercises/A03-sum-even-values.md) | write code | Independent | easy |
| A17 | [Sum the multiples of k](../exercises/A17-sum-multiples-of-k.md) | write code | Independent | medium |
| A08 | [Multiples of 3 or 5](../exercises/A08-multiples-of-3-or-5.md) | write code | Challenge | medium |

</div>

## Until the user stops

Read values until a stop value, or until the input is valid. Lesson: [Recipe 10 · Sentinel loop](../cookbook/10-sentinel-loop.md).

<ThemeExercises theme="loops" group="until-the-user-stops" />

<div class="gh-only">

| ID | Exercise | Kind | Level | Effort |
| --- | --- | --- | --- | --- |
| L05 | [Until zero](../exercises/L05-until-zero.md) | write code | Independent | medium |
| A06 | [Average until zero](../exercises/A06-average-until-zero.md) | write code | Independent | medium |
| A09 | [Min and max until zero](../exercises/A09-min-and-max-until-zero.md) | write code | Independent | medium |
| L07 | [Ask until valid](../exercises/L07-ask-until-valid.md) | write code | Independent | medium |
| L08 | [Guess the number](../exercises/L08-guess-the-number.md) | write code | Challenge | medium |

</div>

## Draw rows and grids

One row, then the same row many times: a loop inside a loop. Lesson: [Recipe 8 · Nested grid](../cookbook/08-nested-grid.md).

<ThemeExercises theme="loops" group="draw-rows-and-grids" />

<div class="gh-only">

| ID | Exercise | Kind | Level | Effort |
| --- | --- | --- | --- | --- |
| L09 | [Draw one row](../exercises/L09-draw-a-row.md) | write code | Guided | easy |
| L10 | [Numbers on one line](../exercises/L10-numbers-on-one-line.md) | write code | Guided | easy |
| G07 | [Arrange: a square](../exercises/G07-arrange-a-square.md) | arrange the lines | Guided | easy |
| G08 | [Solid square](../exercises/G08-solid-square.md) | write code | Guided | easy |
| G01 | [Draw a rectangle](../exercises/G01-rectangle.md) | write code | Guided | easy |
| G09 | [Rows of numbers](../exercises/G09-number-rows.md) | write code | Guided | easy |
| G14 | [Numbers in columns](../exercises/G14-numbers-in-columns.md) | write code | Guided | easy |
| G03 | [Multiplication grid](../exercises/G03-multiplication-grid.md) | write code | Independent | medium |

</div>

## Draw shapes

The inner loop depends on the row, or an `if` picks the character. Lesson: [Recipe 8 · Nested grid](../cookbook/08-nested-grid.md).

<ThemeExercises theme="loops" group="draw-shapes" />

<div class="gh-only">

| ID | Exercise | Kind | Level | Effort |
| --- | --- | --- | --- | --- |
| G02 | [Draw a right triangle](../exercises/G02-right-triangle.md) | write code | Guided | medium |
| G10 | [Triangle of row numbers](../exercises/G10-row-number-triangle.md) | write code | Guided | easy |
| G11 | [Counting triangle](../exercises/G11-counting-triangle.md) | write code | Guided | easy |
| G12 | [Upside-down triangle](../exercises/G12-upside-down-triangle.md) | write code | Guided | easy |
| G04 | [Hollow rectangle](../exercises/G04-hollow-rectangle.md) | write code | Independent | medium |
| G13 | [Diagonal](../exercises/G13-diagonal.md) | write code | Independent | medium |
| G05 | [Checkerboard](../exercises/G05-checkerboard.md) | write code | Challenge | medium |
| G06 | [Pyramid](../exercises/G06-pyramid.md) | write code | Challenge | hard |

</div>

## Digits

`% 10` gives the last digit, `/ 10` removes it. Lesson: [Recipe 6 · Digit extraction](../cookbook/06-digit-extraction.md).

<ThemeExercises theme="loops" group="digits" />

<div class="gh-only">

| ID | Exercise | Kind | Level | Effort |
| --- | --- | --- | --- | --- |
| D01 | [Last digit](../exercises/D01-last-digit.md) | write code | Guided | easy |
| D02 | [Remove the last digit](../exercises/D02-remove-last-digit.md) | write code | Guided | easy |
| D03 | [Count the digits](../exercises/D03-count-digits.md) | write code | Guided | medium |
| D08 | [First digit](../exercises/D08-first-digit.md) | write code | Guided | easy |
| D04 | [Sum of the digits](../exercises/D04-digit-sum.md) | write code | Guided | medium |
| D09 | [Count the even digits](../exercises/D09-count-even-digits.md) | write code | Guided | easy |
| D10 | [Count one digit](../exercises/D10-count-a-digit.md) | write code | Guided | easy |
| D12 | [Product of the digits](../exercises/D12-product-of-digits.md) | write code | Guided | easy |
| D11 | [Largest digit](../exercises/D11-largest-digit.md) | write code | Independent | medium |
| D07 | [Fix: digit sum](../exercises/D07-fix-digit-sum.md) | fix the bugs | Independent | medium |
| D05 | [Reverse a number](../exercises/D05-reverse-a-number.md) | write code | Independent | medium |
| D06 | [Palindrome number](../exercises/D06-palindrome-number.md) | write code | Challenge | hard |

</div>

## Changing values

Keep the last values in variables, like Fibonacci. Lesson: [Recipe 7 · State update](../cookbook/07-state-update.md).

<ThemeExercises theme="loops" group="changing-values" />

<div class="gh-only">

| ID | Exercise | Kind | Level | Effort |
| --- | --- | --- | --- | --- |
| S01 | [Trace two variables](../exercises/S01-trace-updates.md) | paper | Guided | easy |
| S04 | [Doubling](../exercises/S04-doubling.md) | write code | Guided | easy |
| S02 | [Fibonacci](../exercises/S02-fibonacci.md) | write code | Independent | hard |
| S05 | [N-th Fibonacci](../exercises/S05-nth-fibonacci.md) | write code | Independent | medium |
| S03 | [Even Fibonacci sum](../exercises/S03-even-fibonacci-sum.md) | write code | Challenge | hard |

</div>

## Search and combine

A `bool` flag that starts false, `break` to stop early, then two recipes together. Lesson: [Recipe 5 · Flag/search](../cookbook/05-flag-search.md).

<ThemeExercises theme="loops" group="search-and-combine" />

<div class="gh-only">

| ID | Exercise | Kind | Level | Effort |
| --- | --- | --- | --- | --- |
| P03 | [Has a multiple of 7](../exercises/P03-has-a-multiple-of-7.md) | write code | Guided | easy |
| P04 | [Has an even digit](../exercises/P04-has-an-even-digit.md) | write code | Guided | easy |
| P07 | [All digits odd](../exercises/P07-all-digits-odd.md) | write code | Guided | easy |
| P05 | [First multiple](../exercises/P05-first-multiple.md) | write code | Guided | easy |
| P06 | [Smallest divisor](../exercises/P06-smallest-divisor.md) | write code | Guided | easy |
| P01 | [Is it prime?](../exercises/P01-is-it-prime.md) | write code | Independent | medium |
| P02 | [All primes up to N](../exercises/P02-primes-up-to-n.md) | write code | Challenge | hard |
| M01 | [Armstrong number](../exercises/M01-armstrong-number.md) | write code | Challenge | hard |
| M02 | [Armstrong in a range](../exercises/M02-armstrong-numbers-in-a-range.md) | write code | Challenge | hard |

</div>

## Ready for the next theme when

You can write factorial, a triangle and the digit sum from a blank file, and say if a number is prime.

---

Previous: [Basics](basics.md) · [Roadmap](../ROADMAP.md) · Next: [Arrays, text and lists](arrays.md)
