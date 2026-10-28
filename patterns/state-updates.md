# Pattern: update multiple pieces of state

**Mental model:** each iteration advances from the current state to the next one. Sometimes the next state depends on *both* old values.

Fibonacci starts with `0, 1`; every following value is the sum of the previous two.

```csharp
int previous = 0;
int current = 1;

for (int i = 0; i < 6; i++)
{
    Console.WriteLine(previous);

    int next = previous + current;
    previous = current;
    current = next;
}
```

Output: `0, 1, 1, 2, 3, 5` (one number per line).

| Iteration | previous printed | current before | next calculated |
| --- | ---: | ---: | ---: |
| 1 | 0 | 1 | 1 |
| 2 | 1 | 1 | 2 |
| 3 | 1 | 2 | 3 |
| 4 | 2 | 3 | 5 |
| 5 | 3 | 5 | 8 |
| 6 | 5 | 8 | 13 |

**Why a temporary variable?** If you overwrite `previous` first and then compute `previous + current`, you lose one of the old values. Calculate `next` before shifting the variables. Multiple assignment is possible in C#, but explicit steps are easier to trace at first.

**Practice:** S01–S02. Afterwards attempt Project Euler #2 in smaller steps.
