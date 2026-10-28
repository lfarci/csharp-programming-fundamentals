# D02 · Remove the last digit

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | ⭐ | 4d · Digits | [Digit extraction](../cookbook/06-digit-extraction.md) | [D01](D01-last-digit.md) | Custom |

## 🎯 Goal

Read N ≥ 0. Print N without its last digit.

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `352`

```text
Without last digit: 35
```

**Example 2** — input: `7`

```text
Without last digit: 0
```

## ⚠️ Edge cases to test

- One digit → 0.

## 📏 Rules

- No string. Use integer `/`.
- No LINQ, no ready-made helpers that do the loop for you. The loop **is** the exercise.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats / what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

352 / 10 with two `int`s gives 35, not 35.2.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Print the first digit of a 3-digit number using only `/`.

## 🔑 Solution

Only after a real try: [D02-remove-last-digit](../solutions/D02-remove-last-digit.cs). Your solution can be different and still correct!

⬅️ [Back to the inventory](README.md)
