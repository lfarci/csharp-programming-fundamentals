# Pattern: extract digits

![352 is split into remaining digits and one last digit at each step.](../assets/digit-extraction.svg)

## Visual model: split off one digit

| Number before | Remaining part after integer division by 10 | Detached digit (remainder 10) |
| ---: | ---: | ---: |
| 352 | 35 | 2 |
| 35 | 3 | 5 |
| 3 | 0 | 3 |

At every split: **old number = remaining part × 10 + detached digit**. The order of processing is 2, 5, 3: right to left. A sum ignores order; constructing reversed digits does not. Keep the original number in another box if you need it later.

**Mental model:** peel the last digit from a nonnegative integer, process it, and repeat with the remaining number.

```csharp
int remaining = 352;
int sum = 0;

while (remaining > 0)
{
    int digit = remaining % 10;
    sum += digit;
    remaining /= 10;
}
Console.WriteLine(sum); // 10
```

| Iteration | remaining before | digit | sum after | remaining after |
| --- | ---: | ---: | ---: | ---: |
| 1 | 352 | 2 | 2 | 35 |
| 2 | 35 | 5 | 7 | 3 |
| 3 | 3 | 3 | 10 | 0 |

**Recipe:** `number % 10` gets the last digit; integer `number / 10` removes it. The `while` loop ends when the remaining number is zero.

**Boundary:** zero has one decimal digit, even though the loop above executes zero times for input 0. Decide how to handle zero explicitly in digit-counting exercises. Negative numbers are outside the first exercises' scope.

**Common mistakes:** modifying the original value before saving it for comparison; accidentally using floating-point division; forgetting to remove a digit, causing an infinite loop.

**Practice:** D01–D04. Later combine with powers and an accumulator for an Armstrong number.
