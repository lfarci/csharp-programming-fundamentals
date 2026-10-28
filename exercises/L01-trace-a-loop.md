# L01 · Trace a loop (paper)

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | ⭐ | 4a · Repeat & count | [Counter loop](../cookbook/01-counter-loop.md) | [C01](C01-even-or-odd.md) | Custom |

## 🎯 Goal

Without running it, predict the output of this loop and fill a trace table.

```csharp
for (int i = 2; i <= 8; i += 2)
{
    Console.WriteLine(i);
}
```

Table columns: `turn`, `i at start`, `i <= 8?`, `output`, `i after step`.

## ⚠️ Edge cases to test

- What is the value of `i` when the loop stops? Is it printed?

## 📏 Rules

- Paper and pen only. Run the code **after** to check.
- No LINQ, no ready-made helpers that do the loop for you. The loop **is** the exercise.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats / what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

Start: `i = 2`. Test `2 <= 8` → yes → print 2 → step `i = 4`.

</details>

<details><summary>Hint 2</summary>

Keep going until the test is false. Write the line where the test fails too.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Predict `for (int i = 10; i > 0; i -= 3)` without running it.

## 🔑 Solution

Only after a real try: [L01-trace-a-loop](../solutions/L01-trace-a-loop.md). Your solution can be different and still correct!

⬅️ [Back to the inventory](README.md)
