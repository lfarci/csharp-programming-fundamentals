# S01 · Trace two changing variables (paper)

| Level | Difficulty | Roadmap step | Recipes | Do these first | Source |
| --- | --- | --- | --- | --- | --- |
| Guided | ⭐ | 4d · State | [State update](../cookbook/07-state-update.md) | [L01](L01-trace-a-loop.md) | Custom |

## 🎯 Goal

Without running it, fill a trace table (`turn`, `next`, `a`, `b`) for this code. Then run it to check.

```csharp
int a = 1;
int b = 2;
for (int i = 1; i <= 3; i++)
{
    int next = a + b;
    a = b;
    b = next;
    Console.WriteLine($"a={a} b={b}");
}
```

Then swap the two middle lines (`b = next;` before `a = b;`). What changes? Why?

## ⚠️ Edge cases to test

- Order of the assignments.

## 📏 Rules

- Paper first.
- No LINQ, no ready-made helpers that do the loop for you. The loop **is** the exercise.

## 🗺️ Before coding

Fill the [recipe card](../cookbook/README.md): result? recipe? boxes and start values? what repeats / what stops? tiny example traced by hand?

## 💡 Hints (open one at a time)

<details><summary>Hint 1</summary>

Each line runs **one after the other**, not all at the same time.

</details>

<details><summary>Hint 2</summary>

Turn 1: next = 1 + 2 = 3, then a = 2, then b = 3.

</details>

## ✅ Mastery check

Solve this variation **alone**, on another day:

Predict the output when `a = 0` and `b = 1` and the loop runs 6 times. Which famous sequence is it?

## 🔑 Solution

Only after a real try: [S01-trace-updates](../solutions/S01-trace-updates.md). Your solution can be different and still correct!

⬅️ [Back to the inventory](README.md)
