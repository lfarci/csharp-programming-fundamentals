🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › D01

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
- No LINQ and no ready-made helpers: you write every step yourself.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

What is the remainder of 352 divided by 10? Do it on paper first.

</details>

<details><summary>Hint 2</summary>

The remainder operator is `%`: `352 % 10` gives `2`. No loop is needed here.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Print the **second to last** digit (352 → 5).

## 🔑 Solution

Only after a real try: [open the solution for D01](../solutions/D01-last-digit.cs). Your solution can be different and still correct!

---

⬅️ Previous: [G06 · Pyramid](G06-pyramid.md) · 📚 [All exercises](README.md) · Next: [D02 · Remove the last digit](D02-remove-last-digit.md) ➡️
