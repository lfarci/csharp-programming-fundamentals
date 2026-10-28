# D06 · Palindrome number

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Challenge | ⭐⭐⭐ | 4d · Digits | [Digit extraction](../cookbook/06-digit-extraction.md) | [D05](D05-reverse-a-number.md) | Custom |

## 🎯 Goal

Read N ≥ 0. Say if it reads the same in both directions.

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `1221`

```text
1221 is a palindrome
```

**Example 2** — input: `123`

```text
123 is not a palindrome
```

**Example 3** — input: `7`

```text
7 is a palindrome
```

## ⚠️ Edge cases to test

- One digit → palindrome.
- Keep the original `n` to compare at the end!

## 📏 Rules

- No string. Reuse D05.
- No LINQ, no ready-made helpers that do the loop for you. The loop **is** the exercise.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats / what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

Palindrome ⇔ the reversed number equals the original.

</details>

<details><summary>Hint 2</summary>

Work on a copy `remaining`, so `n` is still there at the end.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Find all palindrome numbers between 100 and 200.

## 🔑 Solution

Only after a real try: [D06-palindrome-number](../solutions/D06-palindrome-number.cs). Your solution can be different and still correct!

⬅️ [Back to the inventory](README.md)
