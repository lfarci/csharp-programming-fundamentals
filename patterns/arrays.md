# Pattern: traverse an array

## Visual model: position, item, result

| Index | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Value | 4 | 9 | 2 |
| Cursor when i = 1 | visited | **current** | unvisited |

At this moment, i is **1** and values[i] is **9**. Before processing index 1, the sum is 4; afterwards it is 13. The next cursor position is 2. At i = 3, stop: there is no item at that index.

For a maximum, the result box means “largest value seen so far”. For -5, -2, -9: initialize to -5, compare -2 and replace the box with -2, then compare -9 and keep -2. A maximum needs a separate empty-input rule; these exercises assume a nonempty array.

**Mental model:** visit each item once and maintain whatever information the question asks for.

```csharp
int[] values = { 4, 9, 2 };
int total = 0;

for (int i = 0; i < values.Length; i++)
{
    total += values[i];
}
Console.WriteLine(total); // 15
```

**Recipe:** start at index 0, keep going while `i < values.Length`, and access `values[i]`. Indices start at zero.

When you only need each value, `foreach (int value in values)` is another option.

**Common mistakes:** `i <= values.Length` attempts an out-of-range index; confusing an index with a value; initializing a running maximum to 0 if all numbers could be negative. For a nonempty array, initialize the maximum to `values[0]`.

**Practice:** R01–R03. For book practice, see *The Replicator of D’To* and *The Laws of Freach* (Level 12).
