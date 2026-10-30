[Home](../../README.md) › [Projects](README.md) › Hangman

# Hangman

<p class="project-meta">Terminal games · Level: Medium · Effort: 3 to 4 hours</p>

**Guess the secret word letter by letter before the little man is drawn.**

A secret word, a row of underscores and a gallows that grows with every wrong letter. Hangman is the perfect game for working on text letter by letter, and the ASCII drawing is half the fun.

## A sample run

```text
  +---+
  |   |
  O   |
 /|   |
      |
=========
Word:   _ O _ _ _ A M
Missed: E, I, U  (3 of 6)
Your letter: r
Yes! R is in the word.
Word:   _ R O _ R A M
Your letter: p
Word:   P R O _ R A M
Your letter: g
Word:   P R O G R A M
*** You saved him! The word was PROGRAM. ***
```

Your program does not have to look exactly like this: make it yours.

## What you will learn

- walk through a string letter by letter
- keep the found letters in a `bool[]` or a `char[]`
- use a list for the letters already tried
- split a game into small methods

**Themes used:** [Loops](../themes/loops.md), [Arrays, text and lists](../themes/arrays.md), [Methods and errors](../themes/methods.md).

**Exercises that prepare it:** [T01 · Count a letter](../exercises/T01-count-a-letter.md), [R03 · Count matches](../exercises/R03-count-matches.md), [R04 · Find the position](../exercises/R04-find-the-position.md), [K01 · Shopping list](../exercises/K01-shopping-list.md).

## Milestones

From a tiny program to the complete game. After each milestone, the program runs: test it before you go on.

1. **One word, one letter.** The word is `PROGRAM`. Read one letter and say if it is in the word.
2. **Show the progress.** Print the word with `_` for the letters not found yet, like `_ R O _ R A M`.
3. **The game loop.** Repeat until every letter is found or 6 wrong letters were given.
4. **Already tried.** Keep a `List<char>` of tried letters; refuse the same letter twice and ignore upper/lower case.
5. **Random word.** Pick the word from an array of at least 10 words with `Random.Shared.Next`.
6. **The drawing.** Print the gallows with one more body part for each mistake: 7 small drawings in a `string[]`.

## Stretch goals

Pick the ones you like, in any order. Links go to Microsoft Learn when a goal uses something the course has not shown.

- **Categories:** animals, countries, programming words. The player picks one, the hint shows it.
- **Two players:** player 1 types the word (then [`Console.Clear()`](https://learn.microsoft.com/en-us/dotnet/api/system.console.clear) hides it), player 2 guesses.
- **Words from a file:** read `words.txt` with `File.ReadAllLines` so anyone can add words.
- **Score:** points for each found letter, a bonus for each unused life; keep a high score.
- **Colours:** found letters in green, missed ones in red ([`Console.ForegroundColor`](https://learn.microsoft.com/en-us/dotnet/api/system.console.foregroundcolor)).

## Hints (open one at a time)

<details><summary>Hint 1: Showing the word</summary>

Loop over the word: for each letter, print it if it was found, `_` otherwise. A `bool[] found` with the same length as the word remembers which positions are found.

</details>

<details><summary>Hint 2: Is the game won?</summary>

A flag: `bool allFound = true;` then one loop, `if (!found[i]) allFound = false;`. That is the [flag/search](../cookbook/05-flag-search.md) recipe.

</details>

<details><summary>Hint 3: Upper and lower case</summary>

`char.ToUpper(letter)` before comparing, and keep the words in capitals.

</details>

<details><summary>Hint 4: The drawing</summary>

`string[] stages = { "...", "..." };` with 7 multi-line strings (use `\n` or a raw string `"""`). Print `stages[mistakes]`.

</details>

There is no full solution on purpose: if your program does what the milestones say, it is right.

---

[Home](../../README.md) · [Projects](README.md) · Next: [Rock paper scissors+](rock-paper-scissors-lizard-spock.md)
