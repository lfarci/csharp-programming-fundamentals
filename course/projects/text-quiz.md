[Home](../../README.md) › [Projects](README.md) › Text quiz

# Text quiz

**Goal:** a quiz in the terminal. The program asks questions one by one, checks each answer, and prints a score and the questions you missed at the end.

**Themes used:** [Basics](../themes/basics.md), [Loops](../themes/loops.md) (counting, a `bool` flag), [Arrays, text and lists](../themes/arrays.md), [Methods and errors](../themes/methods.md).
**Exercises that prepare it:** [R03 Count matches](../exercises/R03-count-matches.md), [T01 Count a letter](../exercises/T01-count-a-letter.md), [T02 Remove spaces](../exercises/T02-remove-spaces.md), [N02 A method that calls one](../exercises/N02-is-multiple-and-count.md).

```text
Question 1 of 3: What keyword starts a loop that runs a known number of times?
> for
Right!
Question 2 of 3: What does 17 % 5 give?
> 3
Wrong. The answer was: 2
Question 3 of 3: Which type holds true or false?
>  Bool
Right!
Score: 2 / 3
To review: What does 17 % 5 give?
```

## Milestones

- [ ] **1. One question.** Ask one question, read the answer, print `Right!` or `Wrong.` with the correct answer.
- [ ] **2. Many questions.** Keep the questions in a `string[]` and the answers in another `string[]` of the same length. Loop over them and count the right answers.
- [ ] **3. Forgiving answers.** ` Bool ` counts as `bool`: ignore spaces at the ends and upper/lower case.
- [ ] **4. Review.** Remember which questions were missed and print them after the score.
- [ ] **5. Questions from a file.** Read the questions from `quiz.txt`, one per line like `What does 17 % 5 give?|2`.

## Stretch goals

- Shuffle the questions so the order changes each time.
- Multiple choice: show `a)`, `b)`, `c)` and accept only those letters.
- Give a second try for a wrong answer, worth half a point.

## Hints (open one at a time)

<details><summary>Hint 1: two arrays, one index</summary>

`questions[i]` and `answers[i]` belong together. One `for` loop with `i < questions.Length` visits both.

</details>

<details><summary>Hint 2: comparing answers</summary>

Write `bool IsRight(string typed, string expected)`. Inside, `typed.Trim().ToLower() == expected.ToLower()`.

</details>

<details><summary>Hint 3: the missed questions</summary>

A `List<string> missed`: `missed.Add(questions[i])` on a wrong answer. After the loop, print the list (or `Nothing to review!` when it is empty).

</details>

<details><summary>Hint 4: the file</summary>

`File.ReadAllLines("quiz.txt")` gives one string per line; `line.Split('|')` gives the question at `[0]` and the answer at `[1]`. Skip empty lines.

</details>

There is no full solution: if your program does what the example shows, it is right.

---

[Home](../../README.md) · [Projects](README.md) · Next: [Study skills](../docs/README.md)
