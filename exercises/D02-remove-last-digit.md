🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › D02

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
- No LINQ and no ready-made helpers: you write every step yourself.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

What is 352 divided by 10, if you throw away everything after the decimal point?

</details>

<details><summary>Hint 2</summary>

With two `int`s, `/` drops the rest: `352 / 10` gives `35`, not `35.2`.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Print the first digit of a 3-digit number using only `/`.

## 🔑 Solution

Only after a real try: [open the solution for D02](../solutions/D02-remove-last-digit.cs). Your solution can be different and still correct!

---

⬅️ Previous: [D01 · Last digit](D01-last-digit.md) · 📚 [All exercises](README.md) · Next: [D03 · Count the digits](D03-count-digits.md) ➡️
