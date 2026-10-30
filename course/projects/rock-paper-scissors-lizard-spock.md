[Home](../../README.md) › [Projects](README.md) › Rock paper scissors+

# Rock paper scissors+

<p class="project-meta">Terminal games · Level: Easy · Effort: 2 to 3 hours</p>

**The classic game, then the 5-weapon version where Spock vaporizes rock.**

Start with rock, paper, scissors against the computer, best of 5. Then add two more weapons, lizard and Spock: now there are 25 possible duels and a big `if` chain gets messy. Time to think about a better way to decide who wins.

## A sample run

```text
ROCK PAPER SCISSORS LIZARD SPOCK - best of 5
Your move (r, p, s, l, k): k
You: SPOCK   Computer: ROCK
Spock vaporizes rock. You win this round!
Score: you 1 - 0 computer
Your move (r, p, s, l, k): l
You: LIZARD  Computer: SCISSORS
Scissors decapitate lizard. Computer wins this round.
Score: you 1 - 1 computer
...
*** You win the match 3 - 2! ***
```

Your program does not have to look exactly like this: make it yours.

## What you will learn

- turn the user's choice into a number and back into a name
- decide a winner with conditions, then with a table
- count rounds and scores
- write methods that give back a value

**Themes used:** [Basics](../themes/basics.md), [Loops](../themes/loops.md), [Methods and errors](../themes/methods.md).

**Exercises that prepare it:** [C02 · Largest of three](../exercises/C02-largest-of-three.md), [C03 · Ticket price](../exercises/C03-ticket-price.md), [N02 · A method that calls one](../exercises/N02-is-multiple-and-count.md).

## Milestones

From a tiny program to the complete game. After each milestone, the program runs: test it before you go on.

1. **One round.** Read `r`, `p` or `s`; the computer picks at random; print both moves and who wins.
2. **Refuse bad input.** Anything else: `Please type r, p or s.` and ask again.
3. **Best of 5.** Keep the score; stop when someone reaches 3 wins (draws do not count).
4. **Methods.** `string Name(int move)` and `int Winner(int a, int b)` (1, 2 or 0 for a draw).
5. **Lizard and Spock.** Add the two weapons: scissors cut paper, paper covers rock, rock crushes lizard, lizard poisons Spock, Spock smashes scissors, scissors decapitate lizard, lizard eats paper, paper disproves Spock, Spock vaporizes rock, rock crushes scissors.
6. **The funny line.** Print the right sentence for each win: `Paper disproves Spock.`

## Stretch goals

Pick the ones you like, in any order. Links go to Microsoft Learn when a goal uses something the course has not shown.

- **The clever trick:** number the weapons 0 to 4 in the order rock, Spock, paper, lizard, scissors. Then `(5 + a - b) % 5` is 1 or 2 when `a` wins, 3 or 4 when `b` wins. Why does it work?
- **A computer that learns:** count which move the player uses most, and play what beats it.
- **Statistics:** at the end, print how often the player used each weapon, as an ASCII bar chart.
- **Suspense:** print `Rock... paper... scissors...` with a pause ([`Thread.Sleep`](https://learn.microsoft.com/en-us/dotnet/api/system.threading.thread.sleep)).
- **Colours:** the winner of each round in green ([`Console.ForegroundColor`](https://learn.microsoft.com/en-us/dotnet/api/system.console.foregroundcolor)).

## Hints (open one at a time)

<details><summary>Hint 1: Moves as numbers</summary>

Store the move as an `int` (0 = rock, 1 = paper, 2 = scissors). A `string[] names = { "ROCK", "PAPER", "SCISSORS" };` turns it back into text.

</details>

<details><summary>Hint 2: Who wins with 3 weapons</summary>

With 0, 1, 2 in that order, each move beats the one before it: `a` wins when `(a - b + 3) % 3 == 1`.

</details>

<details><summary>Hint 3: Who wins with 5 weapons</summary>

A table: `bool[,] beats` or, simpler, a `string[]` of 10 lines like `"PAPER DISPROVES SPOCK"`. Look for the line that starts with your move and ends with the computer's.

</details>

<details><summary>Hint 4: Best of 5</summary>

`while (you < 3 && computer < 3)`: two counters, an `if` after each round.

</details>

There is no full solution on purpose: if your program does what the milestones say, it is right.

---

[Home](../../README.md) · [Projects](README.md) · Next: [Pig dice duel](pig-dice.md)
