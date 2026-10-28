# Pattern: traverse an array

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
