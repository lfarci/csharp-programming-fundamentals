[Home](../../README.md) › [Projects](README.md) › Guessing game

# Guessing game

**Goal:** the computer picks a secret number from 1 to 100. The player guesses until they find it. After each guess the program says `Higher!` or `Lower!`, and at the end how many tries it took.

**Themes used:** [Basics](../themes/basics.md), [Loops](../themes/loops.md) (until the user stops, input validation), [Methods and errors](../themes/methods.md).
**Exercises that prepare it:** [L07 Ask until valid](../exercises/L07-ask-until-valid.md), [L08 Guess the number](../exercises/L08-guess-the-number.md), [E01 Safe number reader](../exercises/E01-safe-number-reader.md).

```text
I picked a number from 1 to 100.
Your guess: 50
Lower!
Your guess: abc
That is not a number.
Your guess: 25
Higher!
Your guess: 31
Correct! You needed 3 tries.
```

## Milestones

Do them in order. After each one, the program runs.

- [ ] **1. Fixed secret.** The secret is 42. Read one guess and print `Correct!`, `Higher!` or `Lower!`.
- [ ] **2. Loop.** Keep asking until the guess is right. Count the tries and print them at the end.
- [ ] **3. Random secret.** Use `Random.Shared.Next(1, 101)` (the 101 is *not* included).
- [ ] **4. Safe input.** Typing `abc` or an empty line must not crash: say so, ask again, and do not count it as a try.
- [ ] **5. Play again.** At the end ask `Play again? (y/n)`. Keep the best score of the session and print it when the player quits.

## Stretch goals

- Let the player choose the range (for example 1 to 1000) and give a limit of tries.
- Turn it around: **you** think of a number and the computer guesses it, halving the range each time. How many tries does it need for 1 to 1000, at most?
- Split the program into methods: `ReadGuess()`, `PlayOneRound()` (gives back the number of tries).

## Hints (open one at a time)

<details><summary>Hint 1: which loop?</summary>

You do not know how many guesses are needed: this is a `while` loop (see [Sentinel loop](../cookbook/10-sentinel-loop.md)). The test is "the guess is not the secret".

</details>

<details><summary>Hint 2: the counter</summary>

A counter box `int tries = 0;` before the loop, `tries++` once per **valid** guess.

</details>

<details><summary>Hint 3: safe input</summary>

`int.TryParse(text, out int guess)` gives back `false` for `abc`. Use `continue` to go back to the top of the loop without counting the try (see [Input validation](../cookbook/09-input-validation.md)).

</details>

<details><summary>Hint 4: play again</summary>

Put the whole game inside an outer `do … while` loop that repeats while the answer is `y`. The best score starts at `int.MaxValue`.

</details>

There is no full solution: if your program does what the example shows, it is right.

---

[Home](../../README.md) · [Projects](README.md) · Next: [Expense tracker](expense-tracker.md)
