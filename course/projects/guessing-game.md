[Home](../../README.md) › [Projects](README.md) › Guessing game

# Guessing game

<p class="project-meta">Terminal games · Level: Easy · Effort: 1 to 2 hours</p>

**The computer hides a number. Hot or cold? Find it in as few tries as you can.**

The computer thinks of a number from 1 to 100 and dares you to find it. Every guess gets an answer: higher, lower, and with the stretch goals, *hot* or *freezing*. Then you turn the tables and make the computer guess **your** number.

## A sample run

```text
=== GUESS MY NUMBER ===
I picked a number from 1 to 100. You have 7 tries.
Try 1: 50
Too high! (warm)
Try 2: banana
That is not a number. Bananas do not count.
Try 2: 25
Too low! (hot!)
Try 3: 31
*** YOU GOT IT in 3 tries! New best score! ***
Play again? (y/n) n
Best this session: 3 tries. Bye!
```

Your program does not have to look exactly like this: make it yours.

## What you will learn

- repeat until something happens with a `while` loop
- count tries and keep a best score
- read numbers safely with `int.TryParse`
- pick random numbers with `Random.Shared.Next`

**Themes used:** [Basics](../themes/basics.md), [Loops](../themes/loops.md), [Methods and errors](../themes/methods.md).

**Exercises that prepare it:** [L07 · Ask until valid](../exercises/L07-ask-until-valid.md), [L08 · Guess the number](../exercises/L08-guess-the-number.md), [E01 · Safe number reader](../exercises/E01-safe-number-reader.md).

## Milestones

From a tiny program to the complete game. After each milestone, the program runs: test it before you go on.

1. **Fixed secret.** The secret is 42. Read one guess and print `Too high!`, `Too low!` or `You got it!`.
2. **Loop.** Keep asking until the guess is right. Count the tries and print them.
3. **Random secret.** `Random.Shared.Next(1, 101)` gives 1 to 100 (the 101 is not included).
4. **Safe input.** Text or an empty line does not crash and does not count as a try.
5. **Limited tries.** 7 tries at most. When they run out, reveal the number.
6. **Play again.** Ask `Play again? (y/n)` and keep the best score of the session.

## Stretch goals

Pick the ones you like, in any order. Links go to Microsoft Learn when a goal uses something the course has not shown.

- **Hot or cold:** print `hot!` when the guess is within 5 of the secret, `warm` within 15, `freezing` otherwise.
- **Difficulty levels:** easy (1 to 50, 10 tries), normal, hard (1 to 1000, 10 tries).
- **Reverse mode:** you think of a number and the computer guesses it by halving the range. Can it always win in 10 tries for 1 to 1000? Why?
- **Colours:** green for a win, red for too high, blue for too low, with [`Console.ForegroundColor`](https://learn.microsoft.com/en-us/dotnet/api/system.console.foregroundcolor).
- **High score file:** save the best score in `best.txt` so it survives a restart ([`File.WriteAllLines`](https://learn.microsoft.com/en-us/dotnet/api/system.io.file.writealllines)).

## Hints (open one at a time)

<details><summary>Hint 1: Which loop?</summary>

You do not know how many guesses are needed: a `while` loop whose test is "not found yet and tries left". See the [sentinel loop](../cookbook/10-sentinel-loop.md) recipe.

</details>

<details><summary>Hint 2: Not counting bad input</summary>

`if (!int.TryParse(text, out int guess)) { ...; continue; }` jumps back to the top before `tries++`.

</details>

<details><summary>Hint 3: The best score</summary>

Start it at `int.MaxValue`; after a win, `if (tries < best) best = tries;`. That is the [min/max](../cookbook/04-min-max.md) recipe.

</details>

<details><summary>Hint 4: Reverse mode</summary>

Keep `low` and `high`. The computer guesses `(low + high) / 2`; on `higher` set `low = guess + 1`, on `lower` set `high = guess - 1`.

</details>

There is no full solution on purpose: if your program does what the milestones say, it is right.

---

[Home](../../README.md) · [Projects](README.md) · Next: [Hangman](hangman.md)
