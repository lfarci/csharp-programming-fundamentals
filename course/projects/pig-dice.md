[Home](../../README.md) › [Projects](README.md) › Pig dice duel

# Pig dice duel

<p class="project-meta">Terminal games · Level: Medium · Effort: 2 to 3 hours</p>

**Roll again or bank your points? One 1 and you lose the whole turn.**

Pig is an old folk dice game with a single cruel rule: roll as often as you like and add up the dice, but if you roll a 1 your turn's points are gone. First to 100 wins. It is a game about greed, chance and, later, strategy.

## A sample run

```text
=== PIG === first to 100 wins
You: 0   Computer: 0
You roll... 5   (turn: 5)   Roll again? (y/n) y
You roll... 6   (turn: 11)  Roll again? (y/n) y
You roll... 4   (turn: 15)  Roll again? (y/n) n
You bank 15. You: 15
Computer rolls... 3, 6, 2, 1  -> PIG! It loses 11 points.
You roll... 1  -> PIG! Turn over.
Computer rolls... 6, 5, 4, 6  and banks 21. Computer: 21
...
*** You win 102 to 87! ***
```

Your program does not have to look exactly like this: make it yours.

## What you will learn

- simulate dice with `Random`
- nest a turn loop inside a game loop
- update several variables in the right order
- write a simple computer strategy

**Themes used:** [Loops](../themes/loops.md), [Methods and errors](../themes/methods.md).

**Exercises that prepare it:** [S04 · Doubling](../exercises/S04-doubling.md), [A06 · Average until zero](../exercises/A06-average-until-zero.md), [L08 · Guess the number](../exercises/L08-guess-the-number.md).

## Milestones

From a tiny program to the complete game. After each milestone, the program runs: test it before you go on.

1. **One roll.** Print a random number from 1 to 6, many times, to check that 1 and 6 both appear.
2. **One turn.** Roll, add to the turn total, ask `Roll again?`. A 1 ends the turn with 0 points.
3. **Bank.** Saying `n` adds the turn total to your score.
4. **The game.** Repeat turns until someone reaches 100. Print both scores after each turn.
5. **The computer.** Its strategy: keep rolling until its turn total is 20 or more, then bank.
6. **Polish.** Show every die of the computer's turn on one line, and announce the winner in style.

## Stretch goals

Pick the ones you like, in any order. Links go to Microsoft Learn when a goal uses something the course has not shown.

- **Two dice:** a 1 loses the turn; double 1 loses the **whole score**.
- **Smarter computer:** if it is far behind, it takes more risks (banks at 30).
- **Simulation:** make two computer players with different limits (15, 20, 25) play 10 000 games without printing. Which limit wins most? You just did science.
- **ASCII dice:** draw each die as a 3x3 box of dots.
- **More players:** 2 to 4 humans, names in a `List<string>`, scores in a `List<int>`.

## Hints (open one at a time)

<details><summary>Hint 1: A die</summary>

`int die = Random.Shared.Next(1, 7);` gives 1 to 6.

</details>

<details><summary>Hint 2: Two loops</summary>

The outer loop runs while nobody has 100. Inside, one turn is another loop that runs until the player stops or rolls a 1.

</details>

<details><summary>Hint 3: Two players, one code</summary>

Write `int PlayHumanTurn()` and `int PlayComputerTurn()`; both give back the points to bank (0 after a 1).

</details>

<details><summary>Hint 4: The simulation</summary>

Turn the computer turn into a method with the limit as a parameter, then call it in a `for` loop 10 000 times and count wins.

</details>

There is no full solution on purpose: if your program does what the milestones say, it is right.

---

[Home](../../README.md) · [Projects](README.md) · Next: [Tic-tac-toe](tic-tac-toe.md)
