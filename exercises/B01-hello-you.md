# B01 · Hello you

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | ⭐ | 1 · Hello World | — | — | Custom |

## 🎯 Goal

Ask the user for their name and greet them.

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `Ada`

```text
Hello, Ada!
```

**Example 2** — input: `Sam`

```text
Hello, Sam!
```

## ⚠️ Edge cases to test

- An empty name: what does your program print? (`Hello, !` is OK for now.)

## 📏 Rules

- Use `Console.Write`, `Console.ReadLine` and `Console.WriteLine`.
- No LINQ, no ready-made helpers that do the loop for you. The loop **is** the exercise.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats / what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

`Console.ReadLine()` gives you the text the user typed. Store it in a `string` variable.

</details>

<details><summary>Hint 2</summary>

Glue text together with `+`, or use interpolation: `$"Hello, {name}!"`.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Ask for a first name **and** a city, and print `Ada lives in Brussels.`

## 🔑 Solution

Only after a real try: [B01-hello-you](../solutions/B01-hello-you.cs). Your solution can be different and still correct!

⬅️ [Back to the inventory](README.md)
