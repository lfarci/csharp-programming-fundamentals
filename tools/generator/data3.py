from data2 import ex, E

ex(id="G01", slug="rectangle", title="Draw a rectangle", level="Guided", stars=1, step="4c · Draw in 2D", recipes=["08"], pre=["L03"],
   goal="Read a width and a height. Draw a rectangle of `*`.",
   examples=[(["4","3"], ["****","****","****"]), (["1","2"], ["*","*"])],
   edge=["Width 1 → a vertical line."],
   constraints=["Two nested `for` loops. Print one `*` at a time."],
   hints=["Step 1: print **one** line of `width` stars with one loop.",
          "Step 2: repeat that line `height` times → put it in another loop.",
          "`Console.Write(\"*\")` in the inner loop, `Console.WriteLine()` after it."],
   mastery="Read the character to use too (`#`, `o`, …).",
   code=r'''Console.Write("Width: ");
int width = int.Parse(Console.ReadLine()!);
Console.Write("Height: ");
int height = int.Parse(Console.ReadLine()!);

for (int row = 1; row <= height; row++)
{
    for (int col = 1; col <= width; col++)
    {
        Console.Write("*");
    }
    Console.WriteLine();
}
''')

ex(id="G02", slug="right-triangle", title="Draw a right triangle", level="Independent", stars=2, step="4c · Draw in 2D", recipes=["08"], pre=["G01"],
   goal="Read a height. Draw a right triangle: row 1 has 1 star, row 2 has 2 stars, …",
   examples=[(["4"], ["*","**","***","****"]), (["1"], ["*"])],
   edge=["Height 1."],
   constraints=["Nested loops."],
   hints=["Make a table: row → number of stars. Row 3 has 3 stars.",
          "Only the **test** of the inner loop changes compared to G01: `col <= row`."],
   mastery="Draw it upside down (4 stars, then 3, 2, 1).",
   code=r'''Console.Write("Height: ");
int height = int.Parse(Console.ReadLine()!);

for (int row = 1; row <= height; row++)
{
    for (int col = 1; col <= row; col++)
    {
        Console.Write("*");
    }
    Console.WriteLine();
}
''')

ex(id="G03", slug="multiplication-grid", title="Multiplication grid", level="Independent", stars=2, step="4c · Draw in 2D", recipes=["08"], pre=["G01","L04"],
   goal="Read N. Print an N×N grid where the cell at row `r` and column `c` contains `r × c`. Each number takes 4 characters (right-aligned).",
   examples=[(["4"], ["   1   2   3   4","   2   4   6   8","   3   6   9  12","   4   8  12  16"])],
   edge=["N = 1 → one cell."],
   constraints=["Nested loops."],
   hints=["Same skeleton as G01, but print a number instead of a star.",
          "Right-align on 4 characters: `Console.Write($\"{row * col,4}\");`"],
   mastery="Only print the cells where `c <= r` (a triangle of numbers).",
   code=r'''Console.Write("N: ");
int n = int.Parse(Console.ReadLine()!);

for (int row = 1; row <= n; row++)
{
    for (int col = 1; col <= n; col++)
    {
        Console.Write($"{row * col,4}");
    }
    Console.WriteLine();
}
''')

ex(id="G04", slug="hollow-rectangle", title="Hollow rectangle", level="Independent", stars=2, step="4c · Draw in 2D", recipes=["08"], pre=["G01"],
   goal="Read a width and a height. Draw only the border of the rectangle with `*`; the inside is spaces.",
   examples=[(["5","4"], ["*****","*   *","*   *","*****"]), (["3","3"], ["***","* *","***"])],
   edge=["Height 1 or 2 → no inside."],
   constraints=["Nested loops + one `if` inside."],
   hints=["A cell is on the border if it is in the first row, the last row, the first column or the last column.",
          "`if (row == 1 || row == height || col == 1 || col == width)`."],
   mastery="Draw an X inside a square (cells where `row == col` or `row + col == size + 1`).",
   code=r'''Console.Write("Width: ");
int width = int.Parse(Console.ReadLine()!);
Console.Write("Height: ");
int height = int.Parse(Console.ReadLine()!);

for (int row = 1; row <= height; row++)
{
    for (int col = 1; col <= width; col++)
    {
        if (row == 1 || row == height || col == 1 || col == width)
        {
            Console.Write("*");
        }
        else
        {
            Console.Write(" ");
        }
    }
    Console.WriteLine();
}
''')

ex(id="G05", slug="checkerboard", title="Checkerboard", level="Challenge", stars=2, step="4c · Draw in 2D", recipes=["08"], pre=["G04","C01"],
   goal="Read a size. Draw a size×size checkerboard with `#` and `.`, starting with `#` in the top-left corner.",
   examples=[(["4"], ["#.#.",".#.#","#.#.",".#.#"]), (["1"], ["#"])],
   edge=["Odd size."],
   constraints=["Nested loops. No `string` tricks."],
   hints=["Look at `row + col` for every `#` cell. What do they have in common?",
          "Even sum → `#`, odd sum → `.` (with rows and columns starting at 1)."],
   mastery="Make each square 2×2 characters big.",
   code=r'''Console.Write("Size: ");
int size = int.Parse(Console.ReadLine()!);

for (int row = 1; row <= size; row++)
{
    for (int col = 1; col <= size; col++)
    {
        if ((row + col) % 2 == 0)
        {
            Console.Write("#");
        }
        else
        {
            Console.Write(".");
        }
    }
    Console.WriteLine();
}
''')

ex(id="G06", slug="pyramid", title="Pyramid", level="Challenge", stars=3, step="4c · Draw in 2D", recipes=["08"], pre=["G02"],
   goal="Read a height. Draw a centered pyramid of `*`.",
   examples=[(["3"], ["  *"," ***","*****"]), (["1"], ["*"])],
   edge=["Height 1."],
   constraints=["Nested loops: **two** inner loops (spaces, then stars)."],
   hints=["Make a table for height 3: row → spaces → stars. Row 1: 2 spaces, 1 star. Row 2: 1 space, 3 stars. Row 3: 0, 5.",
          "Spaces = `height - row`. Stars = `2 * row - 1`.",
          "Inside the row loop: first a loop for the spaces, then a loop for the stars, then `WriteLine()`."],
   mastery="Draw a diamond (a pyramid, then the same pyramid upside down).",
   code=r'''Console.Write("Height: ");
int height = int.Parse(Console.ReadLine()!);

for (int row = 1; row <= height; row++)
{
    for (int s = 1; s <= height - row; s++)
    {
        Console.Write(" ");
    }
    for (int star = 1; star <= 2 * row - 1; star++)
    {
        Console.Write("*");
    }
    Console.WriteLine();
}
''')

ex(id="D01", slug="last-digit", title="Last digit", level="Guided", stars=1, step="4d · Digits", recipes=["06"], pre=["B03"],
   goal="Read a whole number N ≥ 0. Print its last digit.",
   examples=[(["352"], ["Last digit: 2"]), (["7"], ["Last digit: 7"]), (["0"], ["Last digit: 0"])],
   edge=["One-digit number → the number itself."],
   constraints=["No string. Use `%`."],
   hints=["What is the remainder of 352 divided by 10?"],
   mastery="Print the **second to last** digit (352 → 5).",
   code=r'''Console.Write("N: ");
int n = int.Parse(Console.ReadLine()!);
Console.WriteLine($"Last digit: {n % 10}");
''')

ex(id="D02", slug="remove-last-digit", title="Remove the last digit", level="Guided", stars=1, step="4d · Digits", recipes=["06"], pre=["D01"],
   goal="Read N ≥ 0. Print N without its last digit.",
   examples=[(["352"], ["Without last digit: 35"]), (["7"], ["Without last digit: 0"])],
   edge=["One digit → 0."],
   constraints=["No string. Use integer `/`."],
   hints=["352 / 10 with two `int`s gives 35, not 35.2."],
   mastery="Print the first digit of a 3-digit number using only `/`.",
   code=r'''Console.Write("N: ");
int n = int.Parse(Console.ReadLine()!);
Console.WriteLine($"Without last digit: {n / 10}");
''')

ex(id="D03", slug="count-digits", title="Count the digits", level="Independent", stars=2, step="4d · Digits", recipes=["06","02"], pre=["D02","L05"],
   goal="Read N ≥ 0. Print how many digits it has.",
   examples=[(["352"], ["Digits: 3"]), (["0"], ["Digits: 1"]), (["1000"], ["Digits: 4"])],
   edge=["**0 has 1 digit** (a plain `while (n > 0)` loop says 0)."],
   constraints=["A loop. No `ToString().Length`, no `Math.Log10`."],
   hints=["How many times can you remove the last digit before the number becomes 0?",
          "Trace 352 → 35 → 3 → 0: three removals.",
          "For 0: a `do … while` runs at least once, so it counts 1."],
   mastery="Count how many digits of N are even.",
   code=r'''Console.Write("N: ");
int n = int.Parse(Console.ReadLine()!);

int digits = 0;
int remaining = n;
do
{
    digits++;
    remaining /= 10;
}
while (remaining > 0);

Console.WriteLine($"Digits: {digits}");
''')

ex(id="D04", slug="digit-sum", title="Sum of the digits", level="Independent", stars=2, step="4d · Digits", recipes=["06","02"], pre=["D03"],
   goal="Read N ≥ 0. Print the sum of its digits.",
   examples=[(["352"], ["Digit sum: 10"]), (["0"], ["Digit sum: 0"]), (["9999"], ["Digit sum: 36"])],
   edge=["0 → 0."],
   constraints=["A loop with `% 10` and `/ 10`. No string."],
   hints=["Fill the trace table: `remaining`, `digit`, `sum`.",
          "Three lines in the loop: take the digit, add it, remove it."],
   mastery="Repeat the digit sum until one digit is left (9875 → 29 → 11 → 2).",
   code=r'''Console.Write("N: ");
int n = int.Parse(Console.ReadLine()!);

int sum = 0;
int remaining = n;
while (remaining > 0)
{
    int digit = remaining % 10;
    sum += digit;
    remaining /= 10;
}
Console.WriteLine($"Digit sum: {sum}");
''')

ex(id="D05", slug="reverse-a-number", title="Reverse a number", level="Independent", stars=2, step="4d · Digits", recipes=["06"], pre=["D04"],
   goal="Read N ≥ 0. Print the number with its digits in reverse order.",
   examples=[(["352"], ["Reversed: 253"]), (["1200"], ["Reversed: 21"]), (["0"], ["Reversed: 0"])],
   edge=["Trailing zeros disappear (1200 → 21)."],
   constraints=["Build an `int`, not a string."],
   hints=["The digits come out in the order 2, 5, 3. That is already the reversed order!",
          "To add a digit at the right of a number: `reversed * 10 + digit`.",
          "Trace: 0 → 2 → 25 → 253."],
   mastery="Explain why 1200 → 21 and not 0021.",
   code=r'''Console.Write("N: ");
int n = int.Parse(Console.ReadLine()!);

int reversed = 0;
int remaining = n;
while (remaining > 0)
{
    int digit = remaining % 10;
    reversed = reversed * 10 + digit;
    remaining /= 10;
}
Console.WriteLine($"Reversed: {reversed}");
''')

ex(id="D06", slug="palindrome-number", title="Palindrome number", level="Challenge", stars=3, step="4d · Digits", recipes=["06"], pre=["D05"],
   goal="Read N ≥ 0. Say if it reads the same in both directions.",
   examples=[(["1221"], ["1221 is a palindrome"]), (["123"], ["123 is not a palindrome"]), (["7"], ["7 is a palindrome"])],
   edge=["One digit → palindrome.", "Keep the original `n` to compare at the end!"],
   constraints=["No string. Reuse D05."],
   hints=["Palindrome ⇔ the reversed number equals the original.",
          "Work on a copy `remaining`, so `n` is still there at the end."],
   mastery="Find all palindrome numbers between 100 and 200.",
   code=r'''Console.Write("N: ");
int n = int.Parse(Console.ReadLine()!);

int reversed = 0;
int remaining = n;          // copy: we need n at the end
while (remaining > 0)
{
    reversed = reversed * 10 + remaining % 10;
    remaining /= 10;
}

if (reversed == n)
{
    Console.WriteLine($"{n} is a palindrome");
}
else
{
    Console.WriteLine($"{n} is not a palindrome");
}
''')

ex(id="S01", slug="trace-updates", title="Trace two changing variables (paper)", level="Guided", stars=1, step="4d · State", recipes=["07"], pre=["L01"], paper=True,
   goal="Without running it, fill a trace table (`turn`, `next`, `a`, `b`) for this code. Then run it to check.\n\n```csharp\nint a = 1;\nint b = 2;\nfor (int i = 1; i <= 3; i++)\n{\n    int next = a + b;\n    a = b;\n    b = next;\n    Console.WriteLine($\"a={a} b={b}\");\n}\n```\n\nThen swap the two middle lines (`b = next;` before `a = b;`). What changes? Why?",
   examples=[], edge=["Order of the assignments."],
   constraints=["Paper first."],
   hints=["Each line runs **one after the other**, not all at the same time.",
          "Turn 1: next = 1 + 2 = 3, then a = 2, then b = 3."],
   mastery="Predict the output when `a = 0` and `b = 1` and the loop runs 6 times. Which famous sequence is it?",
   answer="""| Turn | `next` | `a` after | `b` after | Output |
| ---: | ---: | ---: | ---: | --- |
| 1 | 3 | 2 | 3 | `a=2 b=3` |
| 2 | 5 | 3 | 5 | `a=3 b=5` |
| 3 | 8 | 5 | 8 | `a=5 b=8` |

With the lines swapped (`b = next; a = b;`): turn 1 → b = 3, then a = 3 (the **new** b!). Output `a=3 b=3`, then `a=6 b=6`, `a=12 b=12`. The old value of `b` was lost.

Mastery check: `a` and `b` go through 1 1, 1 2, 2 3, 3 5, 5 8, 8 13 → it is the **Fibonacci** sequence.""")

ex(id="S02", slug="fibonacci", title="Fibonacci", level="Independent", stars=3, step="4d · State", recipes=["07"], pre=["S01","A01"], teacher="Fibonacci",
   goal="Read N. Print the first N Fibonacci numbers on one line, starting with 0 and 1. Each number is the sum of the two before it.",
   examples=[(["6"], ["0 1 1 2 3 5"]), (["1"], ["0"]), (["10"], ["0 1 1 2 3 5 8 13 21 34"])],
   edge=["N = 0 → nothing.", "N = 1 → only 0.", "N = 2 → 0 1."],
   constraints=["No array, no recursion. Variables `previous`, `current`, `next`."],
   hints=["Write the first 8 numbers on paper. Which two numbers do you need to make the next one?",
          "Print `previous` at the start of each turn, then compute `next`, then slide.",
          "Order: `next = previous + current; previous = current; current = next;`"],
   mastery="Print the N-th Fibonacci number only (position 0 is 0, position 1 is 1, position 10 is 55).",
   code=r'''Console.Write("N: ");
int n = int.Parse(Console.ReadLine()!);

long previous = 0;
long current = 1;
for (int i = 0; i < n; i++)
{
    Console.Write(previous + " ");
    long next = previous + current;
    previous = current;
    current = next;
}
Console.WriteLine();
''')

ex(id="S03", slug="even-fibonacci-sum", title="Even Fibonacci sum", level="Challenge", stars=3, step="4d · State", recipes=["07","03"], pre=["S02","A03"], euler=2,
   goal="Read a limit. Add up the **even** Fibonacci numbers that are **not greater** than the limit.",
   examples=[(["10"], ["Sum: 10"]), (["100"], ["Sum: 44"]), (["1"], ["Sum: 0"])],
   edge=["The limit itself counts if it is an even Fibonacci number (limit 8 → 2 + 8 = 10)."],
   constraints=["`while` loop (you do not know how many terms)."],
   hints=["Up to 100: 0 1 1 2 3 5 8 13 21 34 55 89 → even ones 0, 2, 8, 34 → 44.",
          "Stop condition: `while (previous <= limit)`.",
          "Inside: `if (previous % 2 == 0) sum += previous;` then slide like S02."],
   mastery="Solve [Project Euler #2](https://projecteuler.net/problem=2) (limit four million). Use `long`.",
   code=r'''Console.Write("Limit: ");
long limit = long.Parse(Console.ReadLine()!);

long previous = 0;
long current = 1;
long sum = 0;
while (previous <= limit)
{
    if (previous % 2 == 0)
    {
        sum += previous;
    }
    long next = previous + current;
    previous = current;
    current = next;
}
Console.WriteLine($"Sum: {sum}");
''')

ex(id="P01", slug="is-it-prime", title="Is it prime?", level="Independent", stars=2, step="4d · Search", recipes=["05"], pre=["A02"],
   goal="Read N. Say if it is a prime number (≥ 2 and only divisible by 1 and itself).",
   examples=[(["7"], ["7 is prime"]), (["9"], ["9 is not prime"]), (["1"], ["1 is not prime"]), (["2"], ["2 is prime"]), (["97"], ["97 is prime"])],
   edge=["0 and 1 are not prime.", "2 is the only even prime."],
   constraints=["A loop with a `bool` flag. No library."],
   hints=["Try every divisor `d` from 2 to N − 1. One divisor is enough to say \"not prime\".",
          "Flag: `bool isPrime = n >= 2;` and set it to `false` when `n % d == 0`.",
          "Do not print inside the loop. Decide **after** the loop."],
   mastery="Make it faster: stop at `d * d <= n`. Why does that work?",
   code=r'''Console.Write("N: ");
int n = int.Parse(Console.ReadLine()!);

bool isPrime = n >= 2;
for (int d = 2; d * d <= n; d++)
{
    if (n % d == 0)
    {
        isPrime = false;
        break;
    }
}

Console.WriteLine(isPrime ? $"{n} is prime" : $"{n} is not prime");
''')

ex(id="P02", slug="primes-up-to-n", title="All primes up to N", level="Challenge", stars=3, step="4d · Search", recipes=["01","05","02"], pre=["P01"],
   goal="Read N. Print all prime numbers from 2 to N on one line, then how many there are.",
   examples=[(["20"], ["2 3 5 7 11 13 17 19","Count: 8"]), (["2"], ["2","Count: 1"]), (["1"], ["Count: 0"])],
   edge=["N < 2 → none."],
   constraints=["Nested loops: the P01 test inside a counter loop."],
   hints=["Outer loop: `candidate` from 2 to N.",
          "Inner part: copy your P01 code, with `candidate` instead of `n`.",
          "The flag must be **reset** for every candidate (declare it inside the outer loop)."],
   mastery="Print the first N primes (not the primes up to N).",
   code=r'''Console.Write("N: ");
int n = int.Parse(Console.ReadLine()!);

int count = 0;
for (int candidate = 2; candidate <= n; candidate++)
{
    bool isPrime = true;               // reset for every candidate
    for (int d = 2; d * d <= candidate; d++)
    {
        if (candidate % d == 0)
        {
            isPrime = false;
            break;
        }
    }
    if (isPrime)
    {
        Console.Write(candidate + " ");
        count++;
    }
}
Console.WriteLine();
Console.WriteLine($"Count: {count}");
''')

ex(id="M01", slug="armstrong-number", title="Armstrong number", level="Challenge", stars=3, step="4 · Combine", recipes=["06","02"], pre=["D03","D04","A07"], teacher="Armstrong",
   goal="Read N ≥ 0. An Armstrong number equals the sum of its digits, each raised to the power **number of digits**. Say if N is one.\n\n153 → 3 digits → 1³ + 5³ + 3³ = 153 ✅. 9474 → 4 digits → 9⁴ + 4⁴ + 7⁴ + 4⁴ = 9474 ✅.",
   examples=[(["153"], ["153 is an Armstrong number"]), (["154"], ["154 is not an Armstrong number"]), (["9474"], ["9474 is an Armstrong number"]), (["0"], ["0 is an Armstrong number"]), (["10"], ["10 is not an Armstrong number"])],
   edge=["Every 1-digit number is an Armstrong number (5¹ = 5).", "The power is the number of digits, **not always 3**."],
   constraints=["No string, no `Math.Pow`. Reuse D03 (count), D04 (digits) and A07 (power)."],
   hints=["Cut the problem: (1) count the digits, (2) for each digit, (3) compute digit^count, (4) add, (5) compare. See [Combining recipes](../cookbook/combining-recipes.md).",
          "Step (1) empties your copy. Make a **new** copy of `n` for step (2).",
          "The power is a small product loop **inside** the digit loop: `power = 1; for (i = 0; i < digits; i++) power *= digit;`"],
   mastery="Solve it again from a blank file two days later, without looking.",
   code=r'''Console.Write("N: ");
int n = int.Parse(Console.ReadLine()!);

// 1. count the digits
int digits = 0;
int remaining = n;
do
{
    digits++;
    remaining /= 10;
}
while (remaining > 0);

// 2-4. add digit^digits for every digit
int sum = 0;
remaining = n;
while (remaining > 0)
{
    int digit = remaining % 10;
    int power = 1;
    for (int i = 0; i < digits; i++)
    {
        power *= digit;
    }
    sum += power;
    remaining /= 10;
}

// 5. compare
if (sum == n)
{
    Console.WriteLine($"{n} is an Armstrong number");
}
else
{
    Console.WriteLine($"{n} is not an Armstrong number");
}
''')

ex(id="M02", slug="armstrong-numbers-in-a-range", title="All Armstrong numbers in a range", level="Challenge", stars=3, step="4 · Combine", recipes=["01","06","02"], pre=["M01"],
   goal="Read a lower and an upper bound. Print every Armstrong number between them (both included).",
   examples=[(["100","999"], ["153 370 371 407"]), (["1","9"], ["1 2 3 4 5 6 7 8 9"]), (["1000","9999"], ["1634 8208 9474"])],
   edge=["Bounds included."],
   constraints=["Your M01 code inside a counter loop. Beware: the inner variables must be reset for every candidate."],
   hints=["Outer loop: `candidate` from `lower` to `upper`.",
          "Paste M01 inside and replace `n` by `candidate`.",
          "Declare `digits`, `sum`, `remaining` **inside** the outer loop so they restart at 0."],
   mastery="Count how many Armstrong numbers exist below 100000.",
   code=r'''Console.Write("From: ");
int lower = int.Parse(Console.ReadLine()!);
Console.Write("To: ");
int upper = int.Parse(Console.ReadLine()!);

for (int candidate = lower; candidate <= upper; candidate++)
{
    int digits = 0;
    int remaining = candidate;
    do
    {
        digits++;
        remaining /= 10;
    }
    while (remaining > 0);

    int sum = 0;
    remaining = candidate;
    while (remaining > 0)
    {
        int digit = remaining % 10;
        int power = 1;
        for (int i = 0; i < digits; i++)
        {
            power *= digit;
        }
        sum += power;
        remaining /= 10;
    }

    if (sum == candidate)
    {
        Console.Write(candidate + " ");
    }
}
Console.WriteLine();
''')
