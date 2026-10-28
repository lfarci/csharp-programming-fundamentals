# B02 · Rectangle calculator

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | ⭐ | 2 · Variables & expressions | — | [B01](B01-hello-you.md) | Custom |

## 🎯 Goal

Read the width and the height of a rectangle (whole numbers). Print its area and its perimeter.

## 🧪 Examples

The text of your questions (`N: `, `Width: `…) is up to you. The **results** must match.

**Example 1** — input: `4`, `3`

```text
Area: 12
Perimeter: 14
```

**Example 2** — input: `5`, `5`

```text
Area: 25
Perimeter: 20
```

## ⚠️ Edge cases to test

- A width of 0 gives an area of 0.

## 📏 Rules

- Use `int.Parse` to turn the text into an `int`.
- No LINQ, no ready-made helpers that do the loop for you. The loop **is** the exercise.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats / what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

Area = width × height. Perimeter = 2 × (width + height).

</details>

<details><summary>Hint 2</summary>

`int width = int.Parse(Console.ReadLine()!);`

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Do the same for a circle with a `double` radius (area = π × r², use `Math.PI`).

## 🔑 Solution

Only after a real try: [B02-rectangle-calculator](../solutions/B02-rectangle-calculator.cs). Your solution can be different and still correct!

⬅️ [Back to the inventory](README.md)
