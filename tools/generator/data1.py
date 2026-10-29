E = []
def ex(**k): E.append(k)

ex(id="B01", slug="hello-you", title="Hello you", level="Guided", stars=1, theme="hello-world", recipes=[], pre=[],
   goal="Ask the user for their name and greet them.",
   examples=[(["Ada"], ["Hello, Ada!"]), (["Sam"], ["Hello, Sam!"])],
   edge=["An empty name: what does your program print? (`Hello, !` is OK for now.)"],
   constraints=["Use `Console.Write`, `Console.ReadLine` and `Console.WriteLine`."],
   hints=["`Console.ReadLine()` gives you the text the user typed. Store it in a `string` variable.",
          "Glue text together with `+`, or use interpolation: `$\"Hello, {name}!\"`."],
   mastery="Ask for a first name **and** a city, and print `Ada lives in Brussels.`",
   code=r'''Console.Write("What is your name? ");
string name = Console.ReadLine()!;
Console.WriteLine($"Hello, {name}!");
''')

ex(id="B02", slug="rectangle-calculator", title="Rectangle calculator", level="Guided", stars=1, theme="variables", recipes=[], pre=["B01"],
   goal="Read the width and the height of a rectangle (whole numbers). Print its area and its perimeter.",
   examples=[(["4","3"], ["Area: 12","Perimeter: 14"]), (["5","5"], ["Area: 25","Perimeter: 20"])],
   edge=["A width of 0 gives an area of 0."],
   constraints=["Use `int.Parse` to turn the text into an `int`."],
   hints=["Area = width × height. Perimeter = 2 × (width + height).",
          "`int width = int.Parse(Console.ReadLine()!);`"],
   mastery="Do the same for a circle with a `double` radius (area = π × r², use `Math.PI`).",
   code=r'''Console.Write("Width: ");
int width = int.Parse(Console.ReadLine()!);
Console.Write("Height: ");
int height = int.Parse(Console.ReadLine()!);

int area = width * height;
int perimeter = 2 * (width + height);

Console.WriteLine($"Area: {area}");
Console.WriteLine($"Perimeter: {perimeter}");
''')

ex(id="B03", slug="seconds-to-hms", title="Seconds to hours, minutes, seconds", level="Independent", stars=2, theme="variables", recipes=[], pre=["B02"],
   goal="Read a number of seconds. Print it as hours, minutes and seconds. This trains `/` and `%`, the key tools of the digit recipe later.",
   examples=[(["3725"], ["1 h 2 min 5 s"]), (["59"], ["0 h 0 min 59 s"]), (["7200"], ["2 h 0 min 0 s"])],
   edge=["0 seconds → `0 h 0 min 0 s`."],
   constraints=["No loop, no `if`. Only `/` and `%` on `int`."],
   hints=["1 hour = 3600 seconds. `3725 / 3600` is 1 (integer division drops the rest).",
          "What is left after the hours? `3725 % 3600` = 125.",
          "Then do the same with 60 on what is left: 125 / 60 = 2 minutes, 125 % 60 = 5 seconds."],
   mastery="Turn a number of days into weeks and days (`17` → `2 weeks 3 days`).",
   code=r'''Console.Write("Seconds: ");
int total = int.Parse(Console.ReadLine()!);

int hours = total / 3600;
int rest = total % 3600;
int minutes = rest / 60;
int seconds = rest % 60;

Console.WriteLine($"{hours} h {minutes} min {seconds} s");
''')

ex(id="C01", slug="even-or-odd", title="Even or odd", level="Guided", stars=1, theme="conditions", recipes=[], pre=["B02"],
   goal="Read a whole number and say if it is even or odd.",
   examples=[(["7"], ["7 is odd"]), (["0"], ["0 is even"]), (["-4"], ["-4 is even"])],
   edge=["0 is even.", "Negative numbers: `-3 % 2` is `-1`, not `1`!"],
   constraints=["Use `%` and `if`/`else`."],
   hints=["A number is even when the remainder of the division by 2 is 0.",
          "`if (n % 2 == 0) { ... } else { ... }`"],
   mastery="Say if a number is a multiple of 3, of 5, of both, or of none.",
   code=r'''Console.Write("Number: ");
int n = int.Parse(Console.ReadLine()!);

if (n % 2 == 0)
{
    Console.WriteLine($"{n} is even");
}
else
{
    Console.WriteLine($"{n} is odd");
}
''')

ex(id="C02", slug="largest-of-three", title="Largest of three", level="Independent", stars=2, theme="conditions", recipes=["04"], pre=["C01"],
   goal="Read three whole numbers and print the largest one.",
   examples=[(["3","9","5"], ["Largest: 9"]), (["-1","-7","-3"], ["Largest: -1"]), (["4","4","2"], ["Largest: 4"])],
   edge=["Two equal values.", "All negative values."],
   constraints=["No `Math.Max`. Use `if`."],
   hints=["You can keep a box `largest` that starts with the first number.",
          "Compare the second number with `largest`. If bigger, replace. Same for the third.",
          "This is the [min/max recipe](../cookbook/04-min-max.md) without a loop!"],
   mastery="Print the smallest of four numbers.",
   code=r'''Console.Write("First: ");
int a = int.Parse(Console.ReadLine()!);
Console.Write("Second: ");
int b = int.Parse(Console.ReadLine()!);
Console.Write("Third: ");
int c = int.Parse(Console.ReadLine()!);

int largest = a;
if (b > largest)
{
    largest = b;
}
if (c > largest)
{
    largest = c;
}

Console.WriteLine($"Largest: {largest}");
''')

ex(id="C03", slug="ticket-price", title="Ticket price", level="Independent", stars=2, theme="conditions", recipes=[], pre=["C01"],
   goal="A cinema ticket costs 5 for children under 12, 7 for people aged 65 or more, and 10 for everyone else. Read an age and print the price.",
   examples=[(["11"], ["Price: 5"]), (["12"], ["Price: 10"]), (["64"], ["Price: 10"]), (["65"], ["Price: 7"])],
   edge=["The boundaries 11/12 and 64/65: test them all!"],
   constraints=["Use `if` / `else if` / `else`."],
   hints=["Three categories → three branches.",
          "\"under 12\" means `age < 12`. \"65 or more\" means `age >= 65`."],
   mastery="Add a rule: on Wednesday (ask the day as a number 1-7) everybody pays 6.",
   code=r'''Console.Write("Age: ");
int age = int.Parse(Console.ReadLine()!);

int price;
if (age < 12)
{
    price = 5;
}
else if (age >= 65)
{
    price = 7;
}
else
{
    price = 10;
}

Console.WriteLine($"Price: {price}");
''')

ex(id="L01", slug="trace-a-loop", title="Trace a loop (paper)", level="Guided", stars=1, theme="loops-repeat", recipes=["01"], pre=["C01"], paper=True,
   goal="Without running it, predict the output of this loop and fill a trace table.\n\n```csharp\nfor (int i = 2; i <= 8; i += 2)\n{\n    Console.WriteLine(i);\n}\n```\n\nTable columns: `turn`, `i at start`, `i <= 8?`, `output`, `i after step`.",
   examples=[], edge=["What is the value of `i` when the loop stops? Is it printed?"],
   constraints=["Paper and pen only. Run the code **after** to check."],
   hints=["Start: `i = 2`. Test `2 <= 8` → yes → print 2 → step `i = 4`.",
          "Keep going until the test is false. Write the line where the test fails too."],
   mastery="Predict `for (int i = 10; i > 0; i -= 3)` without running it.",
   answer="""| Turn | `i` at start | `i <= 8`? | Output | `i` after step |
| ---: | ---: | --- | ---: | ---: |
| 1 | 2 | yes | 2 | 4 |
| 2 | 4 | yes | 4 | 6 |
| 3 | 6 | yes | 6 | 8 |
| 4 | 8 | yes | 8 | 10 |
| — | 10 | **no** → stop | | |

Output: `2 4 6 8` (one per line). The loop stops with `i = 10`, which is **not** printed.

Mastery check: `10 7 4 1` (then `i = -2`, test `-2 > 0` is false).""")

ex(id="L02", slug="boundaries", title="Boundaries: < or <= ? (paper)", level="Guided", stars=1, theme="loops-repeat", recipes=["01"], pre=["L01"], paper=True,
   goal="How many times does each loop run? What is the last value printed? Answer on paper first.\n\n```csharp\nfor (int i = 1; i < 5; i++) Console.WriteLine(i);   // loop A\nfor (int i = 1; i <= 5; i++) Console.WriteLine(i);  // loop B\nfor (int i = 0; i < 5; i++) Console.WriteLine(i);   // loop C\nfor (int i = 5; i >= 1; i--) Console.WriteLine(i);  // loop D\nint k = 10;\nwhile (k < 5) { Console.WriteLine(k); k++; }         // loop E\n```",
   examples=[], edge=["Loop E: can a loop run zero times?"],
   constraints=["Paper first. Then run to check."],
   hints=["For each loop: write the first value, the last value that passes the test, and count.",
          "`i < 5` and `i <= 4` mean the same thing for whole numbers."],
   mastery="Write 3 different `for` loops that all run exactly 7 times.",
   answer="""| Loop | Runs | Values printed | Last value |
| --- | ---: | --- | ---: |
| A `i < 5` from 1 | 4 | 1 2 3 4 | 4 |
| B `i <= 5` from 1 | 5 | 1 2 3 4 5 | 5 |
| C `i < 5` from 0 | 5 | 0 1 2 3 4 | 4 |
| D `i >= 1` from 5 down | 5 | 5 4 3 2 1 | 1 |
| E `k < 5` with k = 10 | **0** | nothing | — |

Rule of thumb: `for (int i = 0; i < n; i++)` and `for (int i = 1; i <= n; i++)` both run **n** times.""")

ex(id="L03", slug="count-up-and-down", title="Count up and down", level="Guided", stars=1, theme="loops-repeat", recipes=["01"], pre=["L01"],
   goal="Read a positive number N. Print the numbers from 1 to N on one line, then from N down to 1 on a second line.",
   examples=[(["4"], ["1 2 3 4","4 3 2 1"]), (["1"], ["1","1"])],
   edge=["N = 1."],
   constraints=["Two loops. Use `Console.Write` to stay on the same line."],
   hints=["Loop 1: start 1, test `i <= n`, step `i++`.",
          "Loop 2: start `n`, test `i >= 1`, step `i--`.",
          "`Console.Write(i + \" \");` then `Console.WriteLine();` after the loop."],
   mastery="Print the odd numbers from N down to 1.",
   code=r'''Console.Write("N: ");
int n = int.Parse(Console.ReadLine()!);

for (int i = 1; i <= n; i++)
{
    Console.Write(i + " ");
}
Console.WriteLine();

for (int i = n; i >= 1; i--)
{
    Console.Write(i + " ");
}
Console.WriteLine();
''')

ex(id="L04", slug="multiplication-table", title="Multiplication table", level="Independent", stars=1, theme="loops-repeat", recipes=["01"], pre=["L03"],
   goal="Read a number N and print its multiplication table from 1 to 10.",
   examples=[(["3"], ["3 x 1 = 3","3 x 2 = 6","3 x 10 = 30"]), (["7"], ["7 x 7 = 49"])],
   edge=["N = 0 → all results are 0."],
   constraints=["One `for` loop."],
   hints=["What changes from line to line? Only the second number (1 to 10).",
          "`Console.WriteLine($\"{n} x {i} = {n * i}\");`"],
   mastery="Read a second number M and print the table up to M instead of 10.",
   code=r'''Console.Write("N: ");
int n = int.Parse(Console.ReadLine()!);

for (int i = 1; i <= 10; i++)
{
    Console.WriteLine($"{n} x {i} = {n * i}");
}
''')

ex(id="L05", slug="until-zero", title="Until zero", level="Independent", stars=2, theme="loops-repeat", recipes=["10","02"], pre=["L03"],
   goal="Read whole numbers one by one. Stop when the user types 0. Print how many **non-zero** numbers were entered.",
   examples=[(["5","-2","8","0"], ["You entered 3 numbers."]), (["0"], ["You entered 0 numbers."])],
   edge=["The first number is already 0.", "Negative numbers count too."],
   constraints=["You do not know how many numbers will come: no `for`."],
   hints=["This is the [sentinel loop](../cookbook/10-sentinel-loop.md). 0 is the sentinel.",
          "`while (true) { read; if (value == 0) break; count++; }`",
          "Do not count the 0 itself."],
   mastery="Also print how many of the numbers were negative.",
   code=r'''int count = 0;
while (true)
{
    Console.Write("Number (0 to stop): ");
    int value = int.Parse(Console.ReadLine()!);
    if (value == 0)
    {
        break;
    }
    count++;
}
Console.WriteLine($"You entered {count} numbers.");
''')

ex(id="L06", slug="even-numbers", title="Even numbers", level="Guided", stars=1, theme="loops-repeat", recipes=["01"], pre=["L03"],
   goal="Read N. Print all even numbers from 2 to N on one line.",
   examples=[(["9"], ["2 4 6 8"]), (["10"], ["2 4 6 8 10"]), (["1"], [""])],
   edge=["N = 1 → nothing is printed.", "N is even → N is printed too."],
   constraints=["Write it **two ways**: (1) step `i += 2`, (2) step `i++` with an `if`."],
   hints=["Way 1: start at 2, step 2.", "Way 2: test every number with `i % 2 == 0`."],
   mastery="Print the multiples of 7 between 1 and N.",
   code=r'''Console.Write("N: ");
int n = int.Parse(Console.ReadLine()!);

// Way 1: jump by 2
for (int i = 2; i <= n; i += 2)
{
    Console.Write(i + " ");
}
Console.WriteLine();

// Way 2 (same output): visit every number, keep the even ones
// for (int i = 1; i <= n; i++)
// {
//     if (i % 2 == 0) Console.Write(i + " ");
// }
''')

ex(id="L07", slug="ask-until-valid", title="Ask until valid", level="Independent", stars=2, theme="loops-repeat", recipes=["09"], pre=["L05","C03"],
   goal="Ask for a number between 1 and 10. If the text is not a number, or is out of range, print `Invalid, try again.` and ask again. At the end print `You chose X`.",
   examples=[(["abc","42","7"], ["Invalid, try again.","Invalid, try again.","You chose 7"]), (["1"], ["You chose 1"])],
   edge=["`abc` must not crash the program.", "1 and 10 are valid; 0 and 11 are not."],
   constraints=["Use `do … while` and `int.TryParse`."],
   hints=["See the [input validation recipe](../cookbook/09-input-validation.md).",
          "`bool ok = int.TryParse(text, out int number);` gives `false` for `abc`.",
          "Loop condition: `while (!valid)`."],
   mastery="Ask for a password until it has at least 8 characters (`text.Length`).",
   code=r'''int number;
bool valid;
do
{
    Console.Write("Number between 1 and 10: ");
    string? text = Console.ReadLine();
    valid = int.TryParse(text, out number) && number >= 1 && number <= 10;
    if (!valid)
    {
        Console.WriteLine("Invalid, try again.");
    }
}
while (!valid);

Console.WriteLine($"You chose {number}");
''')

ex(id="L08", slug="guess-the-number", title="Guess the number", level="Challenge", stars=2, theme="loops-repeat", recipes=["09","02"], pre=["L07"],
   goal="The secret number is 42. The user guesses until correct. After each wrong guess, print `Higher!` or `Lower!`. At the end print `Correct! You needed N tries.`",
   examples=[(["50","30","42"], ["Lower!","Higher!","Correct! You needed 3 tries."]), (["42"], ["Correct! You needed 1 tries."])],
   edge=["Right at the first try."],
   constraints=["Use a loop + a counter."],
   hints=["You do not know how many guesses: `while` or `do … while`.",
          "Keep a `tries` counter that goes up on every guess.",
          "Loop condition: keep going while `guess != secret`."],
   mastery="Use a random secret: `int secret = Random.Shared.Next(1, 101);` and allow at most 7 tries.",
   code=r'''int secret = 42;     // later: Random.Shared.Next(1, 101)
int tries = 0;
int guess;
do
{
    Console.Write("Your guess: ");
    guess = int.Parse(Console.ReadLine()!);
    tries++;
    if (guess < secret)
    {
        Console.WriteLine("Higher!");
    }
    else if (guess > secret)
    {
        Console.WriteLine("Lower!");
    }
}
while (guess != secret);

Console.WriteLine($"Correct! You needed {tries} tries.");
''')
