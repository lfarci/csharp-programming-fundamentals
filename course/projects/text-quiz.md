[Home](../../README.md) › [Projects](README.md) › Quiz show

# Quiz show

<p class="project-meta">Just for fun · Level: Easy · Effort: 2 to 3 hours</p>

**Host your own TV quiz: jokers, streaks, a timer and a final score.**

Lights, music, the host smiles: *question number one...*. Build a quiz show in the terminal with points that grow with each streak, a 50/50 joker and questions loaded from a file, so your friends can write their own.

## A sample run

```text
*** WELCOME TO THE C# QUIZ SHOW ***
Question 1 of 5  (worth 100)
What does 17 % 5 give?
 a) 3   b) 2   c) 12   d) 3.4
Your answer (or J for the 50/50 joker): J
 b) 2   d) 3.4
Your answer: b
Correct! Streak: 1   Score: 100
Question 2 of 5  (worth 200)
Which type holds true or false?
 a) int   b) string   c) bool   d) char
Your answer: c
Correct! Streak: 2   Score: 300
...
FINAL SCORE: 1100   Rank: Code wizard
```

Your program does not have to look exactly like this: make it yours.

## What you will learn

- two arrays (questions and answers) walked with one index
- compare text without caring about case or spaces
- a streak counter that resets
- load data from a file

**Themes used:** [Arrays, text and lists](../themes/arrays.md), [Methods and errors](../themes/methods.md).

**Exercises that prepare it:** [R03 · Count matches](../exercises/R03-count-matches.md), [T01 · Count a letter](../exercises/T01-count-a-letter.md), [T02 · Remove spaces](../exercises/T02-remove-spaces.md), [N02 · A method that calls one](../exercises/N02-is-multiple-and-count.md).

## Milestones

From a tiny program to the complete game. After each milestone, the program runs: test it before you go on.

1. **One question.** Ask it, read the answer, print `Correct!` or the right answer.
2. **Many questions.** Questions, choices and answers in arrays of the same length; one loop.
3. **Forgiving answers.** ` B ` counts as `b`: `Trim()` and `ToLower()`.
4. **Points and streaks.** Each correct answer in a row is worth 100 more; a wrong answer resets the streak.
5. **The 50/50 joker.** Once per game, `J` hides two wrong choices.
6. **Rank.** At the end, a title from the score: `Beginner`, `Apprentice`, `Code wizard`.

## Stretch goals

Pick the ones you like, in any order. Links go to Microsoft Learn when a goal uses something the course has not shown.

- **Questions from a file:** `quiz.txt` with lines like `What does 17 % 5 give?|3|2|12|3.4|b`.
- **Shuffle:** a different order each game (swap random pairs in a loop).
- **Timer:** measure the answer time with [`DateTime`](https://learn.microsoft.com/en-us/dotnet/api/system.datetime) and give a bonus for quick answers.
- **Two players:** take turns, show both scores, announce the winner.
- **Hall of fame:** save the top 5 names and scores to a file.

## Hints (open one at a time)

<details><summary>Hint 1: Matching arrays</summary>

`questions[i]`, `choices[i]` and `answers[i]` belong together. One `for` loop with `i < questions.Length`.

</details>

<details><summary>Hint 2: Comparing</summary>

`bool IsRight(string typed, string expected) => typed.Trim().ToLower() == expected;`

</details>

<details><summary>Hint 3: The joker</summary>

A flag `bool jokerUsed = false;`. When used, print the right choice and one random wrong one, in their normal order.

</details>

<details><summary>Hint 4: Rank</summary>

An `if` / `else if` chain on the score, like [C04](../exercises/C04-grade-from-a-score.md).

</details>

There is no full solution on purpose: if your program does what the milestones say, it is right.

---

[Home](../../README.md) · [Projects](README.md) · Next: [Tiny dungeon](dungeon-crawler.md)
