from data1 import ex, E

ex(id="A01", slug="sum-1-to-n", title="Sum from 1 to N", level="Guided", stars=1, theme="loops-running-result", recipes=["01","02"], pre=["L03"],
   goal="Read N and print the sum 1 + 2 + … + N.",
   examples=[(["5"], ["Sum: 15"]), (["1"], ["Sum: 1"]), (["10"], ["Sum: 55"]), (["0"], ["Sum: 0"])],
   edge=["N = 0 → the loop runs 0 times → sum stays 0."],
   constraints=["Use a loop. No formula `n * (n + 1) / 2` (you can use it to **check** your answer)."],
   hints=["Fill the trace table for N = 4 first: `i`, `sum before`, `sum after`.",
          "The box `sum` is created **before** the loop and starts at 0.",
          "Inside the loop: `sum += i;`. Print **after** the loop."],
   mastery="Sum from A to B (read both). Then: sum of the squares 1² + 2² + … + N².",
   code=r'''Console.Write("N: ");
int n = int.Parse(Console.ReadLine()!);

int sum = 0;
for (int i = 1; i <= n; i++)
{
    sum += i;
}
Console.WriteLine($"Sum: {sum}");
''')

ex(id="A02", slug="count-multiples-of-3", title="Count multiples of 3", level="Guided", stars=1, theme="loops-running-result", recipes=["03"], pre=["A01","C01"],
   goal="Read N. Count how many numbers from 1 to N (included) are divisible by 3.",
   examples=[(["10"], ["Count: 3"]), (["2"], ["Count: 0"]), (["9"], ["Count: 3"])],
   edge=["N smaller than 3 → 0.", "N itself divisible by 3 → counted."],
   constraints=["Loop + `if` + counter. No division trick (`n / 3`) except to check."],
   hints=["Divisible by 3: `i % 3 == 0`.", "Box: `count = 0`, `count++` only when the `if` is true."],
   mastery="Count the numbers from 1 to N that are divisible by 3 **but not** by 2.",
   code=r'''Console.Write("N: ");
int n = int.Parse(Console.ReadLine()!);

int count = 0;
for (int i = 1; i <= n; i++)
{
    if (i % 3 == 0)
    {
        count++;
    }
}
Console.WriteLine($"Count: {count}");
''')

ex(id="A03", slug="sum-even-values", title="Sum of the even numbers", level="Independent", stars=1, theme="loops-running-result", recipes=["03"], pre=["A02"],
   goal="Read N. Print the sum of the even numbers from 1 to N.",
   examples=[(["6"], ["Sum: 12"]), (["7"], ["Sum: 12"]), (["1"], ["Sum: 0"])],
   edge=["N = 1 → 0."],
   constraints=["Loop + `if` + accumulator."],
   hints=["Same loop as A02 (loop + `if (i % 2 == 0)`).", "The box is `sum`, not `count`: inside the `if`, write `sum += i;` instead of `count++;`."],
   mastery="Print the sum of the even numbers AND the sum of the odd numbers with **one** loop.",
   code=r'''Console.Write("N: ");
int n = int.Parse(Console.ReadLine()!);

int sum = 0;
for (int i = 1; i <= n; i++)
{
    if (i % 2 == 0)
    {
        sum += i;
    }
}
Console.WriteLine($"Sum: {sum}");
''')

ex(id="A04", slug="factorial", title="Factorial", level="Independent", stars=2, theme="loops-running-result", recipes=["02"], pre=["A01"], teacher="Factorial",
   goal="Read N (0 ≤ N ≤ 20) and print N! = 1 × 2 × … × N. By definition 0! = 1.",
   examples=[(["5"], ["5! = 120"]), (["0"], ["0! = 1"]), (["12"], ["12! = 479001600"]), (["20"], ["20! = 2432902008176640000"])],
   edge=["N = 0 → 1 (the loop runs 0 times, the box keeps its start value).", "13! does not fit in an `int` → use `long`."],
   constraints=["A loop, no recursion, no library."],
   hints=["Trace 4! on paper: 1 → 1 → 2 → 6 → 24.",
          "Product box. What must it start at? (Not 0!)",
          "`long product = 1; for (int i = 1; i <= n; i++) product *= i;`"],
   mastery="Print every factorial from 0! to N! (one per line), with **one** loop.",
   code=r'''Console.Write("N: ");
int n = int.Parse(Console.ReadLine()!);

long product = 1;
for (int i = 1; i <= n; i++)
{
    product *= i;
}
Console.WriteLine($"{n}! = {product}");
''')

ex(id="A05", slug="sum-square-difference", title="Two accumulators: sum and squares", level="Independent", stars=2, theme="loops-running-result", recipes=["02"], pre=["A01"], euler=6,
   goal="Read N. With **one** loop compute the sum 1+…+N and the sum of squares 1²+…+N². Print both, then (sum)² − (sum of squares).",
   examples=[(["3"], ["Sum: 6","Sum of squares: 14","Difference: 22"]), (["10"], ["Sum: 55","Sum of squares: 385","Difference: 2640"])],
   edge=["N = 1 → 1, 1, 0."],
   constraints=["One loop, two boxes."],
   hints=["Two boxes before the loop: `sum = 0`, `squares = 0`.", "`squares += i * i;`",
          "The difference is computed **after** the loop: `sum * sum - squares`."],
   mastery="Now solve [Project Euler #6](https://projecteuler.net/problem=6) (N = 100). Use `long` if needed.",
   code=r'''Console.Write("N: ");
int n = int.Parse(Console.ReadLine()!);

long sum = 0;
long squares = 0;
for (int i = 1; i <= n; i++)
{
    sum += i;
    squares += i * i;
}
Console.WriteLine($"Sum: {sum}");
Console.WriteLine($"Sum of squares: {squares}");
Console.WriteLine($"Difference: {sum * sum - squares}");
''')

ex(id="A06", slug="average-until-zero", title="Average until zero", level="Independent", stars=2, theme="loops-running-result", recipes=["10","02"], pre=["L05","A01"],
   goal="Read whole numbers until 0. Print their average. If no number was entered, print `No numbers.`",
   examples=[(["4","7","1","0"], ["Average: 4"]), (["1","2","0"], ["Average: 1.5"]), (["0"], ["No numbers."])],
   edge=["First value 0 → never divide by 0!", "The average can have decimals."],
   constraints=["Sentinel loop + two boxes (`sum`, `count`)."],
   hints=["Average = sum / count, so you need **both** boxes.",
          "`(double)sum / count` keeps the decimals. `sum / count` with two `int`s does not.",
          "Check `count == 0` **after** the loop."],
   mastery="Also print how many numbers were above the average. (Why is that hard without an array? You will see in the Arrays theme.)",
   note="On a computer set to French/Dutch, `1.5` may print as `1,5`. Both are correct.",
   code=r'''int sum = 0;
int count = 0;
while (true)
{
    Console.Write("Number (0 to stop): ");
    int value = int.Parse(Console.ReadLine()!);
    if (value == 0)
    {
        break;
    }
    sum += value;
    count++;
}

if (count == 0)
{
    Console.WriteLine("No numbers.");
}
else
{
    double average = (double)sum / count;
    Console.WriteLine($"Average: {average}");
}
''')

ex(id="A07", slug="integer-power", title="Integer power", level="Independent", stars=2, theme="loops-running-result", recipes=["02"], pre=["A04"],
   goal="Read a base and an exponent (exponent ≥ 0). Print base^exponent using a loop.",
   examples=[(["3","4"], ["3^4 = 81"]), (["2","10"], ["2^10 = 1024"]), (["5","0"], ["5^0 = 1"])],
   edge=["Exponent 0 → 1.", "Base 0 → 0 (except 0^0 = 1 by our convention)."],
   constraints=["No `Math.Pow`. A loop with a product box."],
   hints=["3^4 = 3 × 3 × 3 × 3: multiply by the **same** number, exponent times.",
          "Difference with factorial: you multiply by `baseValue`, not by `i`.",
          "`for (int i = 0; i < exponent; i++) result *= baseValue;`"],
   mastery="Print all powers of 2 from 2^0 to 2^N, with only one multiplication per turn.",
   code=r'''Console.Write("Base: ");
int baseValue = int.Parse(Console.ReadLine()!);
Console.Write("Exponent: ");
int exponent = int.Parse(Console.ReadLine()!);

long result = 1;
for (int i = 0; i < exponent; i++)
{
    result *= baseValue;
}
Console.WriteLine($"{baseValue}^{exponent} = {result}");
''')

ex(id="A08", slug="multiples-of-3-or-5", title="Multiples of 3 or 5", level="Challenge", stars=2, theme="loops-running-result", recipes=["03"], pre=["A03"], euler=1,
   goal="Read N. Print the sum of all numbers **below** N that are multiples of 3 or 5.",
   examples=[(["10"], ["Sum: 23"]), (["20"], ["Sum: 78"]), (["1"], ["Sum: 0"])],
   edge=["15 is a multiple of 3 **and** 5: count it once.", "\"below N\" → N itself is not included."],
   constraints=["One loop, one `if` with `||`."],
   hints=["Below 10: 3, 5, 6, 9 → 23. Write them on paper first.",
          "Filter: `i % 3 == 0 || i % 5 == 0`.", "\"below N\": `i < n`."],
   mastery="Solve [Project Euler #1](https://projecteuler.net/problem=1) (N = 1000).",
   code=r'''Console.Write("N: ");
int n = int.Parse(Console.ReadLine()!);

int sum = 0;
for (int i = 1; i < n; i++)
{
    if (i % 3 == 0 || i % 5 == 0)
    {
        sum += i;
    }
}
Console.WriteLine($"Sum: {sum}");
''')

ex(id="A09", slug="min-and-max-until-zero", title="Smallest and largest until zero", level="Independent", stars=2, theme="loops-running-result", recipes=["10","04"], pre=["A06","C02"],
   goal="Read whole numbers until 0. Print the smallest and the largest. If no number was entered, print `No numbers.`",
   examples=[(["4","-2","9","0"], ["Min: -2","Max: 9"]), (["-5","-3","0"], ["Min: -5","Max: -3"]), (["0"], ["No numbers."])],
   edge=["Only negative numbers → max must not be 0!", "Only one number → min = max."],
   constraints=["No array, no list."],
   hints=["What do `min` and `max` start at? Not 0. Idea: the first value read.",
          "Use a counter: when `count == 1`, set both `min` and `max` to the value.",
          "Or start with `min = int.MaxValue` and `max = int.MinValue`."],
   mastery="Also print the **position** (1st, 2nd, …) of the largest number.",
   code=r'''int count = 0;
int min = 0;
int max = 0;
while (true)
{
    Console.Write("Number (0 to stop): ");
    int value = int.Parse(Console.ReadLine()!);
    if (value == 0)
    {
        break;
    }
    count++;
    if (count == 1)
    {
        min = value;   // the first value is both the smallest and the largest so far
        max = value;
    }
    else
    {
        if (value < min) min = value;
        if (value > max) max = value;
    }
}

if (count == 0)
{
    Console.WriteLine("No numbers.");
}
else
{
    Console.WriteLine($"Min: {min}");
    Console.WriteLine($"Max: {max}");
}
''')

ex(id="A10", slug="sum-of-a-series", title="Sum of a series", level="Challenge", stars=2, theme="loops-running-result", recipes=["02"], pre=["A01"],
   goal="Read N. Print the sum 1 + 1/2 + 1/3 + … + 1/N with 4 decimals.",
   examples=[(["1"], ["Sum: 1.0000"]), (["2"], ["Sum: 1.5000"]), (["4"], ["Sum: 2.0833"])],
   edge=["`1 / 2` with two `int`s is **0**! Use `1.0 / i`."],
   constraints=["A loop with a `double` box."],
   hints=["The box is a `double` that starts at 0.",
          "Each turn adds `1.0 / i`.",
          "Print with 4 decimals: `{sum:F4}`."],
   mastery="Compute 1 − 1/2 + 1/3 − 1/4 + … (the sign changes every turn). Hint: a `sign` box that flips with `sign = -sign`.",
   note="On a French/Dutch computer the output is `2,0833`. That is fine.",
   code=r'''Console.Write("N: ");
int n = int.Parse(Console.ReadLine()!);

double sum = 0;
for (int i = 1; i <= n; i++)
{
    sum += 1.0 / i;   // 1.0 makes it a double division
}
Console.WriteLine($"Sum: {sum:F4}");
''')
