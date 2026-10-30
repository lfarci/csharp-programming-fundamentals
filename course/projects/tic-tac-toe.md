[Home](../../README.md) › [Projects](README.md) › Tic-tac-toe

# Tic-tac-toe

<p class="project-meta">Terminal games · Level: Hard · Effort: 4 to 6 hours</p>

**X against O on a 3x3 grid, then against a computer that never loses.**

Everyone knows the game, and that is exactly why it is a great project: you know what *correct* looks like. Draw the grid, take turns, detect a win or a draw, then teach the computer to block you.

## A sample run

```text
 X | 2 | 3
---+---+---
 4 | X | 6
---+---+---
 O | 8 | 9
X, your square (1-9): 5
Square 5 is taken. Try again.
X, your square (1-9): 9
 X | 2 | 3
---+---+---
 4 | X | 6
---+---+---
 O | 8 | X
*** X WINS (1, 5, 9)! *** Score: X 1 - O 0 - draws 0
```

Your program does not have to look exactly like this: make it yours.

## What you will learn

- keep a board in an array of 9 cells
- draw a grid with loops
- check 8 winning lines with a loop over a table
- write a computer move from simple rules

**Themes used:** [Loops](../themes/loops.md), [Arrays, text and lists](../themes/arrays.md), [Methods and errors](../themes/methods.md).

**Exercises that prepare it:** [G01 · Draw a rectangle](../exercises/G01-rectangle.md), [R04 · Find the position](../exercises/R04-find-the-position.md), [P03 · Has a multiple of 7](../exercises/P03-has-a-multiple-of-7.md), [N01 · Armstrong with methods](../exercises/N01-armstrong-with-methods.md).

## Milestones

From a tiny program to the complete game. After each milestone, the program runs: test it before you go on.

1. **The board.** A `char[] board` of 9 cells with `'1'` to `'9'`. Print it as a 3x3 grid.
2. **One move.** Read a square from 1 to 9, put an `X` there. Refuse a number outside 1 to 9 or a square already taken.
3. **Take turns.** Switch between `X` and `O` after each move, for two human players.
4. **Winner.** After each move, check the 8 lines (3 rows, 3 columns, 2 diagonals). Stop on a win.
5. **Draw.** 9 moves and no winner: it is a draw.
6. **The computer.** O plays a random free square.
7. **A smarter computer.** O wins if it can, otherwise blocks X if X could win, otherwise takes the centre, otherwise random.

## Stretch goals

Pick the ones you like, in any order. Links go to Microsoft Learn when a goal uses something the course has not shown.

- **Score across games:** wins, losses and draws, and who starts alternates.
- **A real grid:** use a [2D arrays](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/arrays#multidimensional-arrays) `char[3, 3]` instead of 9 cells.
- **Bigger board:** 4x4, 4 in a row. What has to change in your code?
- **Colours:** X in blue, O in red ([`Console.ForegroundColor`](https://learn.microsoft.com/en-us/dotnet/api/system.console.foregroundcolor)), and [`Console.Clear()`](https://learn.microsoft.com/en-us/dotnet/api/system.console.clear) before each new board.
- **Unbeatable:** look up the *minimax* idea and make a computer that never loses (this one is hard: recursion).

## Hints (open one at a time)

<details><summary>Hint 1: The 8 lines</summary>

Write them once: `int[] lines = { 0,1,2, 3,4,5, 6,7,8, 0,3,6, 1,4,7, 2,5,8, 0,4,8, 2,4,6 };`. Line `k` is `lines[3*k]`, `lines[3*k+1]`, `lines[3*k+2]`.

</details>

<details><summary>Hint 2: Who won?</summary>

`char Winner(char[] board)`: for each line, if the 3 cells are equal, give back that cell; after the loop give back `' '`. That is the [flag/search](../cookbook/05-flag-search.md) recipe.

</details>

<details><summary>Hint 3: Win or block</summary>

Try each free square: put `O` there, ask `Winner`, then put the number back. If `O` wins, play it. Do the same with `X` to find the square to block.

</details>

<details><summary>Hint 4: Drawing the grid</summary>

A loop over the 3 rows; inside, the 3 cells of the row joined by ` | `; between rows, `---+---+---`.

</details>

There is no full solution on purpose: if your program does what the milestones say, it is right.

---

[Home](../../README.md) · [Projects](README.md) · Next: [Weather station](weather-station.md)
