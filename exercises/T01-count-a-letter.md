🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › T01

# T01 · Count a letter

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | ⭐ | 6 · Arrays | [Build a string](../cookbook/12-string-building.md), [Conditional accumulator](../cookbook/03-conditional-accumulator.md) | [R03](R03-count-matches.md) | Custom |

## 🎯 Goal

Read a text, then a letter. Print how many times the letter appears (case-sensitive).

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `banana`, `a`

```text
a appears 3 times
```

**Example 2** — input: `BANANA`, `a`

```text
a appears 0 times
```

**Example 3** — input: *(empty)*, `a`

```text
a appears 0 times
```

## ⚠️ Edge cases to test

- Empty text.
- `'A'` is not `'a'`.

## 📏 Rules

- `foreach (char c in text)`. No LINQ.
- No LINQ and no ready-made helpers: you write every step yourself.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

Get the letter with `char letter = Console.ReadLine()![0];`

</details>

<details><summary>Hint 2</summary>

`if (c == letter) count++;`

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Count all vowels (a, e, i, o, u) in a text.

## 🔑 Solution

Only after a real try: [open the solution for T01](../solutions/T01-count-a-letter.cs). Your solution can be different and still correct!

---

⬅️ Previous: [R05 · Reverse an array](R05-reverse-an-array.md) · 📚 [All exercises](README.md) · Next: [T02 · Remove spaces](T02-remove-spaces.md) ➡️
