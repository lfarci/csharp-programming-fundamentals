# Patterns: counter, accumulator, running product

## Visual model: a running summary

For values 4, 9, 2, think of a result box whose contents are replaced after each item:

| Moment | Current item | Already processed | Still to visit | Total box |
| --- | ---: | --- | --- | ---: |
| Start | — | none | 4, 9, 2 | 0 |
| After item 1 | 4 | 4 | 9, 2 | 4 |
| After item 2 | 9 | 4, 9 | 2 | 13 |
| After item 3 | 2 | 4, 9, 2 | none | 15 |

**Meaning of the box:** the sum of the items already processed. Read an update as “new total = old total + current item”.

| What the question asks | Initial box | Update for a qualifying item |
| --- | --- | --- |
| How many? | count = 0 | count ← count + 1 |
| How much in total? | total = 0 | total ← total + item |
| Product? | product = 1 | product ← product × item |
| Keep some text? | result = "" | result ← result + character |

For 4, 9, 2, counting all items produces **3**, summing produces **15**. Same traversal, different summary. For a condition, rejected items leave the box unchanged.

**Paper drill:** trace 3, 5, 2, first counting values above 2, then summing them. Predict 2 and 8. Explain why the update differs. Memorize the initial value and update only after you can explain the box.

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
