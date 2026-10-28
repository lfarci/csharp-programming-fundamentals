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
- No LINQ, no ready-made helpers that do the loop for you. The loop **is** the exercise.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats / what stops? tiny example traced by hand?

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

Only after a real try: [T02-remove-spaces](../solutions/T02-remove-spaces.cs). Your solution can be different and still correct!

⬅️ [Back to the inventory](README.md)
