🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › T02

# T02 · Remove spaces

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Independent | ⭐ | 6 · Arrays | [Build a string](../cookbook/12-string-building.md) | [T01](T01-count-a-letter.md) | Custom |

## 🎯 Goal

Read a text. Print it without its spaces, between square brackets.

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `a b c`

```text
[abc]
```

**Example 2** — input: `   `

```text
[]
```

**Example 3** — input: `no-space`

```text
[no-space]
```

## ⚠️ Edge cases to test

- Only spaces → empty result.

## 📏 Rules

- Build a new string with `+=`. No `Replace`.
- No LINQ and no ready-made helpers: you write every step yourself.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

Box `result = ""`.

</details>

<details><summary>Hint 2</summary>

Keep the character when `c != ' '`.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Reverse the text (`abc` → `cba`).

## 🔑 Solution

Only after a real try: [open the solution for T02](../solutions/T02-remove-spaces.cs). Your solution can be different and still correct!

---

⬅️ Previous: [T01 · Count a letter](T01-count-a-letter.md) · 📚 [All exercises](README.md) · Next: [T03 · Count and keep the digits](T03-count-and-keep-digits.md) ➡️
