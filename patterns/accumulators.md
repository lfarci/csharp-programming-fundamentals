# Patterns: counter, accumulator, running product

**Mental model:** keep a value that summarizes everything processed so far.

## Sum accumulator

```csharp
int total = 0;
for (int i = 1; i <= 4; i++)
{
    total += i;
}
Console.WriteLine(total); // 10
```

| i | total before | total after |
| --- | ---: | ---: |
| 1 | 0 | 1 |
| 2 | 1 | 3 |
| 3 | 3 | 6 |
| 4 | 6 | 10 |

**Recipe:** initialize to `0`; add a value once per iteration.

## Counter

```csharp
int matches = 0;
for (int i = 1; i <= 10; i++)
{
    if (i % 3 == 0)
    {
        matches++;
    }
}
Console.WriteLine(matches); // 3
```

**Recipe:** initialize to `0`; increment when an event or condition is true.

## Running product

```csharp
int product = 1;
for (int i = 1; i <= 5; i++)
{
    product *= i;
}
Console.WriteLine(product); // 120
```

**Recipe:** initialize to `1`, because starting at zero would always produce zero. This is the core of factorial; `0!` is `1`.

## Conditional accumulation

```csharp
int evenSum = 0;
for (int i = 1; i <= 6; i++)
{
    if (i % 2 == 0)
    {
        evenSum += i;
    }
}
Console.WriteLine(evenSum); // 12
```

**Check:** What is being counted or combined? What is the correct initial value? When does the running value change?

**Common mistakes:** resetting the total inside the loop; starting a product at zero; printing the running value when only the final answer is requested; mixing up `=` and `+=`.

**Practice:** A01–A05, then Project Euler #1.
