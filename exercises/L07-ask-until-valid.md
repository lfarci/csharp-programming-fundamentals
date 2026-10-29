🏠 [Home](../README.md) › 🗺️ [Roadmap](../ROADMAP.md) › 📚 [Exercises](README.md) › L07

# L07 · Ask until valid

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Independent | ⭐⭐ | 4a · Repeat & count | [Input validation](../cookbook/09-input-validation.md) | [L05](L05-until-zero.md), [C03](C03-ticket-price.md) | Custom |

## 🎯 Goal

Ask for a number between 1 and 10. If the text is not a number, or is out of range, print `Invalid, try again.` and ask again. At the end print `You chose X`.

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `abc`, `42`, `7`

```text
Invalid, try again.
Invalid, try again.
You chose 7
```

**Example 2** — input: `1`

```text
You chose 1
```

## ⚠️ Edge cases to test

- `abc` must not crash the program.
- 1 and 10 are valid; 0 and 11 are not.

## 📏 Rules

- Use `do … while` and `int.TryParse`.
- No LINQ and no ready-made helpers: you write every step yourself.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats and what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

See the [input validation recipe](../cookbook/09-input-validation.md).

</details>

<details><summary>Hint 2</summary>

`bool ok = int.TryParse(text, out int number);` gives `false` for `abc`.

</details>

<details><summary>Hint 3</summary>

Loop condition: `while (!valid)`.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Ask for a password until it has at least 8 characters (`text.Length`).

## 🔑 Solution

Only after a real try: [open the solution for L07](../solutions/L07-ask-until-valid.cs). Your solution can be different and still correct!

---

⬅️ Previous: [L06 · Even numbers](L06-even-numbers.md) · 📚 [All exercises](README.md) · Next: [L08 · Guess the number](L08-guess-the-number.md) ➡️
