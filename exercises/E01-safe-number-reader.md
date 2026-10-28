# E01 · Safe number reader

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Independent | ⭐⭐ | 7 · Exceptions | [Input validation](../cookbook/09-input-validation.md) | [L07](L07-ask-until-valid.md) | Custom |

## 🎯 Goal

Ask for a whole number. Use `int.Parse` inside `try`/`catch`: if it fails, print `That is not a number.` and ask again. At the end print `Thanks: X`.

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `abc`, `12x`, `42`

```text
That is not a number.
That is not a number.
Thanks: 42
```

## ⚠️ Edge cases to test

- Empty input also fails.

## 📏 Rules

- Use `try`/`catch (FormatException)` (not `TryParse`, which you used in L07).
- No LINQ, no ready-made helpers that do the loop for you. The loop **is** the exercise.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats / what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

Loop until it works: `while (true) { try { ... break; } catch (FormatException) { ... } }`.

</details>

<details><summary>Hint 2</summary>

`break` goes **after** the `int.Parse` line inside `try`: it only runs if parsing worked.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Also catch `OverflowException` (try `99999999999`) with its own message.

## 🔑 Solution

Only after a real try: [E01-safe-number-reader](../solutions/E01-safe-number-reader.cs). Your solution can be different and still correct!

⬅️ [Back to the inventory](README.md)
