[Home](../README.md) › Exercises

# Exercises

96 small exercises in 15 themes. Do the themes in order; inside a theme, do the exercises from top to bottom. Each one adds **one** new difficulty.

Start one with `./ex start A04`, check it with `./ex check`. New here? Read [Getting started](../docs/getting-started.md) first.

<ExercisesOverview />

<div class="gh-only">

| # | Theme | What you practise | Exercises |
| ---: | --- | --- | ---: |
| 1 | [Hello World](../themes/hello-world.md) | Print text and read what the user types. | 1 |
| 2 | [Variables and expressions](../themes/variables.md) | Store values, compute with them, turn text into numbers. | 2 |
| 3 | [Conditions](../themes/conditions.md) | Choose between cases with `if`. | 4 |
| 4 | [Loops: repeat and count](../themes/loops-repeat.md) | Make the computer repeat something, and trace it on paper. | 17 |
| 5 | [Loops: keep a running result](../themes/loops-running-result.md) | Add up, count or multiply while you loop. | 22 |
| 6 | [Loops: draw in 2D](../themes/loops-2d.md) | Draw rows and columns with a loop inside a loop. | 16 |
| 7 | [Loops: take digits apart](../themes/loops-digits.md) | Read the digits of a number one by one with `% 10` and `/ 10`. | 12 |
| 8 | [Loops: remember changing values](../themes/loops-state.md) | Keep the last values in variables, like Fibonacci. | 5 |
| 9 | [Loops: search](../themes/loops-search.md) | Answer a yes-or-no question with a loop: is it there? is it prime? | 2 |
| 10 | [Combine recipes](../themes/combine.md) | Glue two or three recipes together, like the Armstrong check. | 2 |
| 11 | [Arrays and text](../themes/arrays.md) | Keep many values in one variable, and work on text letter by letter. | 9 |
| 12 | [Files](../themes/files.md) | Save lines to a file and read them back. | 1 |
| 13 | [Exceptions](../themes/exceptions.md) | Stop bad input from crashing your program. | 1 |
| 14 | [Collections](../themes/collections.md) | Use a `List` that can grow. | 1 |
| 15 | [Methods](../themes/methods.md) | Give a recipe a name: parameters and `return`. | 1 |

</div>

## Levels

- **Guided**: small steps, the hints help a lot.
- **Independent**: the same idea, alone.
- **Challenge**: a new problem; combine recipes.

## Drill sets (same pattern, many times)

Want to practise one pattern today? Do **one row**, in order. The exercises change only small details, so you see the **same pattern** again and again.

| Drill | Recipe | Exercises, in order |
| --- | --- | --- |
| Counter loop (print, count, step) | [Counter loop](../cookbook/01-counter-loop.md) | [L03](L03-count-up-and-down.md), [L11](L11-count-from-a-to-b.md), [L12](L12-count-down.md), [L13](L13-count-by-3.md), [L14](L14-count-by-5.md), [L16](L16-odd-numbers.md), [L17](L17-count-down-by-2.md), [L18](L18-squares.md), [L15](L15-count-by-step.md), [L19](L19-count-the-turns.md), [L06](L06-even-numbers.md) |
| Accumulator (sum, product) | [Accumulator](../cookbook/02-accumulator.md) | [A11](A11-arrange-sum-of-squares.md), [A01](A01-sum-1-to-n.md), [A13](A13-sum-from-a-to-b.md), [A14](A14-sum-odd-numbers.md), [A18](A18-sum-of-cubes.md), [A04](A04-factorial.md), [A19](A19-product-from-a-to-b.md), [A20](A20-powers-of-2.md), [A07](A07-integer-power.md), [A10](A10-sum-of-a-series.md) |
| Count or sum only some values | [Conditional accumulator](../cookbook/03-conditional-accumulator.md) | [A02](A02-count-multiples-of-3.md), [A15](A15-count-even-numbers.md), [A16](A16-count-multiples-of-5.md), [A03](A03-sum-even-values.md), [A17](A17-sum-multiples-of-k.md), [A21](A21-count-divisors.md), [A22](A22-sum-of-divisors.md), [A12](A12-fix-count-multiples-of-7.md), [A08](A08-multiples-of-3-or-5.md) |
| Nested loops (draw) | [Nested grid](../cookbook/08-nested-grid.md) | [L09](L09-draw-a-row.md), [L10](L10-numbers-on-one-line.md), [G07](G07-arrange-a-square.md), [G01](G01-rectangle.md), [G08](G08-solid-square.md), [G09](G09-number-rows.md), [G02](G02-right-triangle.md), [G10](G10-row-number-triangle.md), [G11](G11-counting-triangle.md), [G12](G12-upside-down-triangle.md), [G04](G04-hollow-rectangle.md), [G13](G13-diagonal.md), [G14](G14-numbers-in-columns.md), [G03](G03-multiplication-grid.md), [G05](G05-checkerboard.md) |
| Digits | [Digit extraction](../cookbook/06-digit-extraction.md) | [D01](D01-last-digit.md), [D02](D02-remove-last-digit.md), [D03](D03-count-digits.md), [D08](D08-first-digit.md), [D04](D04-digit-sum.md), [D09](D09-count-even-digits.md), [D10](D10-count-a-digit.md), [D11](D11-largest-digit.md), [D12](D12-product-of-digits.md), [D07](D07-fix-digit-sum.md), [D05](D05-reverse-a-number.md) |
| Changing state | [State update](../cookbook/07-state-update.md) | [S01](S01-trace-updates.md), [S04](S04-doubling.md), [S02](S02-fibonacci.md), [S05](S05-nth-fibonacci.md), [S03](S03-even-fibonacci-sum.md) |

## Extra challenges

Bigger problems for later, once their theme feels easy.

| Problem | Theme | Do first |
| --- | --- | --- |
| [Project Euler #1: Multiples of 3 or 5](https://projecteuler.net/problem=1) | Loops: keep a running result | A08 |
| [Project Euler #6: Sum square difference](https://projecteuler.net/problem=6) | Loops: keep a running result | A05 |
| [Project Euler #2: Even Fibonacci numbers](https://projecteuler.net/problem=2) | Loops: keep a running result | S03 |
| [Project Euler #4: Largest palindrome product](https://projecteuler.net/problem=4) | Combine recipes | D06, G03 |
| [Project Euler #5: Smallest multiple](https://projecteuler.net/problem=5) | Combine recipes | P01 |

## When you are stuck

1. Read the recipe again in the [cookbook](../cookbook/README.md).
2. Solve a smaller example on paper with a trace table.
3. Open **one** hint. Wait. Try again.
4. Still stuck? Do the exercise listed in *Do these first*.
