# D01 · Last digit

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | ⭐ | 4d · Digits | [Digit extraction](../cookbook/06-digit-extraction.md) | [B03](B03-seconds-to-hms.md) | Custom |

## 🎯 Goal

Read a whole number N ≥ 0. Print its last digit.

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `352`

```text
Last digit: 2
```

**Example 2** — input: `7`

```text
Last digit: 7
```

**Example 3** — input: `0`

```text
Last digit: 0
```

## ⚠️ Edge cases to test

- One-digit number → the number itself.

## 📏 Rules

- No string. Use `%`.
- No LINQ, no ready-made helpers that do the loop for you. The loop **is** the exercise.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats / what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

What is the remainder of 352 divided by 10?

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Print the **second to last** digit (352 → 5).

## 🔑 Solution

Only after a real try: [D01-last-digit](../solutions/D01-last-digit.cs). Your solution can be different and still correct!

⬅️ [Back to the inventory](README.md)
