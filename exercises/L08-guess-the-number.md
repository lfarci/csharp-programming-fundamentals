# L08 · Guess the number

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Challenge | ⭐⭐ | 4a · Repeat & count | [Input validation](../cookbook/09-input-validation.md), [Accumulator](../cookbook/02-accumulator.md) | [L07](L07-ask-until-valid.md) | Custom |

## 🎯 Goal

The secret number is 42. The user guesses until correct. After each wrong guess, print `Higher!` or `Lower!`. At the end print `Correct! You needed N tries.`

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `50`, `30`, `42`

```text
Lower!
Higher!
Correct! You needed 3 tries.
```

**Example 2** — input: `42`

```text
Correct! You needed 1 tries.
```

## ⚠️ Edge cases to test

- Right at the first try.

## 📏 Rules

- Use a loop + a counter.
- No LINQ, no ready-made helpers that do the loop for you. The loop **is** the exercise.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats / what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

You do not know how many guesses: `while` or `do … while`.

</details>

<details><summary>Hint 2</summary>

Keep a `tries` counter that goes up on every guess.

</details>

<details><summary>Hint 3</summary>

Loop condition: keep going while `guess != secret`.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Use a random secret: `int secret = Random.Shared.Next(1, 101);` and allow at most 7 tries.

## 🔑 Solution

Only after a real try: [L08-guess-the-number](../solutions/L08-guess-the-number.cs). Your solution can be different and still correct!

⬅️ [Back to the inventory](README.md)
