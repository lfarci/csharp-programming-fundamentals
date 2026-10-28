from data3 import ex, E

READ_ARRAY = r'''Console.Write("How many numbers? ");
int count = int.Parse(Console.ReadLine()!);
int[] values = new int[count];
for (int i = 0; i < values.Length; i++)
{
    Console.Write($"Value {i}: ");
    values[i] = int.Parse(Console.ReadLine()!);
}
'''
ARR_NOTE = "Input format: first how many numbers, then one number per line. Fill the array with a loop (see [array traversal](../cookbook/11-array-traversal.md))."

ex(id="R01", slug="sum-an-array", title="Sum of an array", level="Guided", stars=1, step="6 · Arrays", recipes=["11","02"], pre=["A01"],
   goal="Read numbers into an array, then print their sum. " + ARR_NOTE,
   examples=[(["3","4","9","2"], ["Sum: 15"]), (["1","-5"], ["Sum: -5"]), (["0"], ["Sum: 0"])],
   edge=["An empty array (0 numbers) → 0."],
   constraints=["Two loops: one to fill the array, one to sum it. No LINQ (`.Sum()`)."],
   hints=["Indexes go from 0 to `values.Length - 1`.", "Sum it with `foreach (int value in values)`."],
   mastery="Print the sum of the values at **even positions** (0, 2, 4…).",
   code=READ_ARRAY + r'''
int sum = 0;
foreach (int value in values)
{
    sum += value;
}
Console.WriteLine($"Sum: {sum}");
''')

ex(id="R02", slug="largest-in-an-array", title="Largest value in an array", level="Independent", stars=2, step="6 · Arrays", recipes=["11","04"], pre=["R01","C02"],
   goal="Read numbers into an array (at least 1). Print the largest value and its position (index). " + ARR_NOTE,
   examples=[(["3","-5","-2","-9"], ["Largest: -2 at index 1"]), (["5","3","7","2","7","1"], ["Largest: 7 at index 1"])],
   edge=["All negative.", "The max appears twice → give the **first** position."],
   constraints=["No `.Max()`. Start with `values[0]`, not 0."],
   hints=["Two boxes: `max = values[0]` and `maxIndex = 0`.",
          "Loop from index 1. Use `>` (not `>=`) to keep the first position."],
   mastery="Print the second largest value.",
   code=READ_ARRAY + r'''
int max = values[0];
int maxIndex = 0;
for (int i = 1; i < values.Length; i++)
{
    if (values[i] > max)
    {
        max = values[i];
        maxIndex = i;
    }
}
Console.WriteLine($"Largest: {max} at index {maxIndex}");
''')

ex(id="R03", slug="count-matches", title="Count matches in an array", level="Independent", stars=1, step="6 · Arrays", recipes=["11","03"], pre=["R01","A02"],
   goal="Read numbers into an array, then a target value. Print how many times the target appears. " + ARR_NOTE + " The last line is the target.",
   examples=[(["5","2","4","2","5","2","2"], ["2 appears 3 times"]), (["2","1","1","9"], ["9 appears 0 times"])],
   edge=["Target not present → 0."],
   constraints=["No LINQ (`.Count()`)."],
   hints=["Conditional accumulator: `if (value == target) count++;`"],
   mastery="Count the values **greater** than the target.",
   code=READ_ARRAY + r'''
Console.Write("Target: ");
int target = int.Parse(Console.ReadLine()!);

int matches = 0;
foreach (int value in values)
{
    if (value == target)
    {
        matches++;
    }
}
Console.WriteLine($"{target} appears {matches} times");
''')

ex(id="R04", slug="find-the-position", title="Find the position", level="Independent", stars=2, step="6 · Arrays", recipes=["11","05"], pre=["R03"],
   goal="Read numbers into an array, then a target. Print the **first** index where the target is, or `Not found`. " + ARR_NOTE,
   examples=[(["4","7","3","9","3","3"], ["First position: 1"]), (["4","7","3","9","3","8"], ["Not found"])],
   edge=["Target at index 0 (0 is a valid position: use -1 for \"not found\").", "Several matches → the first."],
   constraints=["No `Array.IndexOf`. Use `break`."],
   hints=["Box `int index = -1;` (means not found).",
          "When found: `index = i; break;`", "Decide what to print **after** the loop."],
   mastery="Print the **last** position instead (hint: loop backwards).",
   code=READ_ARRAY + r'''
Console.Write("Target: ");
int target = int.Parse(Console.ReadLine()!);

int index = -1;
for (int i = 0; i < values.Length; i++)
{
    if (values[i] == target)
    {
        index = i;
        break;
    }
}

if (index == -1)
{
    Console.WriteLine("Not found");
}
else
{
    Console.WriteLine($"First position: {index}");
}
''')

ex(id="R05", slug="reverse-an-array", title="Reverse an array", level="Challenge", stars=2, step="6 · Arrays", recipes=["11"], pre=["R01"],
   goal="Read numbers into an array. Build a **new** array with the values in reverse order, then print it on one line. " + ARR_NOTE,
   examples=[(["4","1","2","3","4"], ["4 3 2 1"]), (["1","8"], ["8"])],
   edge=["One element.", "Odd or even length."],
   constraints=["No `Array.Reverse`. Write into the new array with an index."],
   hints=["The new array has the same `Length`.",
          "Value at index `i` goes to index `values.Length - 1 - i`. Check with a 4-box drawing."],
   mastery="Reverse the array **in place** (swap first and last, then second and second-to-last…).",
   code=READ_ARRAY + r'''
int[] reversed = new int[values.Length];
for (int i = 0; i < values.Length; i++)
{
    reversed[values.Length - 1 - i] = values[i];
}

foreach (int value in reversed)
{
    Console.Write(value + " ");
}
Console.WriteLine();
''')

ex(id="T01", slug="count-a-letter", title="Count a letter", level="Guided", stars=1, step="6 · Arrays", recipes=["12","03"], pre=["R03"],
   goal="Read a text, then a letter. Print how many times the letter appears (case-sensitive).",
   examples=[(["banana","a"], ["a appears 3 times"]), (["BANANA","a"], ["a appears 0 times"]), (["","a"], ["a appears 0 times"])],
   edge=["Empty text.", "`'A'` is not `'a'`."],
   constraints=["`foreach (char c in text)`. No LINQ."],
   hints=["Get the letter with `char letter = Console.ReadLine()![0];`", "`if (c == letter) count++;`"],
   mastery="Count all vowels (a, e, i, o, u) in a text.",
   code=r'''Console.Write("Text: ");
string text = Console.ReadLine()!;
Console.Write("Letter: ");
char letter = Console.ReadLine()![0];

int count = 0;
foreach (char c in text)
{
    if (c == letter)
    {
        count++;
    }
}
Console.WriteLine($"{letter} appears {count} times");
''')

ex(id="T02", slug="remove-spaces", title="Remove spaces", level="Independent", stars=1, step="6 · Arrays", recipes=["12"], pre=["T01"],
   goal="Read a text. Print it without its spaces, between square brackets.",
   examples=[(["a b c"], ["[abc]"]), (["   "], ["[]"]), (["no-space"], ["[no-space]"])],
   edge=["Only spaces → empty result."],
   constraints=["Build a new string with `+=`. No `Replace`."],
   hints=["Box `result = \"\"`.", "Keep the character when `c != ' '`."],
   mastery="Reverse the text (`abc` → `cba`).",
   code=r'''Console.Write("Text: ");
string text = Console.ReadLine()!;

string result = "";
foreach (char c in text)
{
    if (c != ' ')
    {
        result += c;
    }
}
Console.WriteLine($"[{result}]");
''')

ex(id="T03", slug="count-and-keep-digits", title="Count and keep the digits", level="Challenge", stars=2, step="6 · Arrays", recipes=["12","02"], pre=["T02"],
   goal="Read a text. Count its digit characters and build a string with only those digits, in order.",
   examples=[(["a1 b2!"], ["Digits: 2","Kept: 12"]), (["abc"], ["Digits: 0","Kept: "])],
   edge=["No digit → 0 and empty text."],
   constraints=["One loop, two boxes. `char.IsDigit(c)` or `c >= '0' && c <= '9'`."],
   hints=["Two boxes: `count = 0` and `kept = \"\"`.", "Update **both** inside the same `if`."],
   mastery="Also compute the **sum** of those digits (`c - '0'` turns `'7'` into 7).",
   code=r'''Console.Write("Text: ");
string text = Console.ReadLine()!;

int count = 0;
string kept = "";
foreach (char c in text)
{
    if (c >= '0' && c <= '9')
    {
        count++;
        kept += c;
    }
}
Console.WriteLine($"Digits: {count}");
Console.WriteLine($"Kept: {kept}");
''')

ex(id="F01", slug="numbers-file", title="Save numbers to a file", level="Independent", stars=2, step="5 · Files", recipes=["10","11","02"], pre=["L05","R01"],
   goal="Read numbers until 0 and save them (one per line) in `numbers.txt`. Then read the file back and print how many lines it has and the sum.",
   examples=[(["4","7","1","0"], ["Lines: 3","Sum: 12"]), (["0"], ["Lines: 0","Sum: 0"])],
   edge=["No number → an empty file."],
   constraints=["`File.WriteAllLines` / `File.ReadAllLines`. No LINQ. Use a `List<string>` or build the text yourself."],
   hints=["Collect the lines in a `List<string>` (or a string with `\\n`), then write once.",
          "`string[] lines = File.ReadAllLines(\"numbers.txt\");` gives an array → [array traversal](../cookbook/11-array-traversal.md).",
          "Each line is text: `int.Parse(line)`."],
   mastery="When the program starts, if the file exists, first print the numbers saved last time.",
   code=r'''List<string> lines = new List<string>();
while (true)
{
    Console.Write("Number (0 to stop): ");
    string text = Console.ReadLine()!;
    if (text == "0")
    {
        break;
    }
    lines.Add(text);
}
File.WriteAllLines("numbers.txt", lines);

string[] saved = File.ReadAllLines("numbers.txt");
int sum = 0;
foreach (string line in saved)
{
    sum += int.Parse(line);
}
Console.WriteLine($"Lines: {saved.Length}");
Console.WriteLine($"Sum: {sum}");
''')

ex(id="E01", slug="safe-number-reader", title="Safe number reader", level="Independent", stars=2, step="7 · Exceptions", recipes=["09"], pre=["L07"],
   goal="Ask for a whole number. Use `int.Parse` inside `try`/`catch`: if it fails, print `That is not a number.` and ask again. At the end print `Thanks: X`.",
   examples=[(["abc","12x","42"], ["That is not a number.","That is not a number.","Thanks: 42"])],
   edge=["Empty input also fails."],
   constraints=["Use `try`/`catch (FormatException)` (not `TryParse`, which you used in L07)."],
   hints=["Loop until it works: `while (true) { try { ... break; } catch (FormatException) { ... } }`.",
          "`break` goes **after** the `int.Parse` line inside `try`: it only runs if parsing worked."],
   mastery="Also catch `OverflowException` (try `99999999999`) with its own message.",
   code=r'''int number;
while (true)
{
    Console.Write("Whole number: ");
    try
    {
        number = int.Parse(Console.ReadLine()!);
        break;
    }
    catch (FormatException)
    {
        Console.WriteLine("That is not a number.");
    }
}
Console.WriteLine($"Thanks: {number}");
''')

ex(id="K01", slug="shopping-list", title="Shopping list", level="Independent", stars=2, step="9 · Collections", recipes=["10","11"], pre=["R01","L05"],
   goal="Read items until the user types `done`. Store them in a `List<string>`. Print them numbered, then the total.",
   examples=[(["milk","eggs","bread","done"], ["1. milk","2. eggs","3. bread","Total: 3 items"]), (["done"], ["Total: 0 items"])],
   edge=["`done` right away."],
   constraints=["`List<string>`, `Add`, `Count`."],
   hints=["`List<string> items = new List<string>();`", "Sentinel loop with `\"done\"`.",
          "Numbering: a `for` loop with `i + 1`."],
   mastery="Do not add an item that is already in the list (`items.Contains(item)`).",
   code=r'''List<string> items = new List<string>();
while (true)
{
    Console.Write("Item (done to stop): ");
    string item = Console.ReadLine()!;
    if (item == "done")
    {
        break;
    }
    items.Add(item);
}

for (int i = 0; i < items.Count; i++)
{
    Console.WriteLine($"{i + 1}. {items[i]}");
}
Console.WriteLine($"Total: {items.Count} items");
''')

ex(id="N01", slug="armstrong-with-methods", title="Armstrong with methods", level="Challenge", stars=3, step="10 · Methods", recipes=["06","02"], pre=["M02"],
   goal="Rewrite M02 with three small methods: `CountDigits(int n)`, `Power(int b, int e)`, `IsArmstrong(int n)`. The main code only reads the bounds and loops.",
   examples=[(["100","999"], ["153 370 371 407"])],
   edge=["`CountDigits(0)` must return 1."],
   constraints=["Each method does **one** recipe. No `Math.Pow`."],
   hints=["`static int CountDigits(int n) { ... return digits; }`",
          "`IsArmstrong` calls the two others and returns a `bool`.",
          "Test each method alone first: `Console.WriteLine(Power(3, 4));` → 81."],
   mastery="Add `IsPalindrome(int n)` and print the numbers in the range that are both (hint: 1–9).",
   code=r'''Console.Write("From: ");
int lower = int.Parse(Console.ReadLine()!);
Console.Write("To: ");
int upper = int.Parse(Console.ReadLine()!);

for (int candidate = lower; candidate <= upper; candidate++)
{
    if (IsArmstrong(candidate))
    {
        Console.Write(candidate + " ");
    }
}
Console.WriteLine();

static int CountDigits(int n)
{
    int digits = 0;
    do
    {
        digits++;
        n /= 10;
    }
    while (n > 0);
    return digits;
}

static int Power(int baseValue, int exponent)
{
    int result = 1;
    for (int i = 0; i < exponent; i++)
    {
        result *= baseValue;
    }
    return result;
}

static bool IsArmstrong(int n)
{
    int digits = CountDigits(n);
    int sum = 0;
    int remaining = n;
    while (remaining > 0)
    {
        sum += Power(remaining % 10, digits);
        remaining /= 10;
    }
    return sum == n;
}
''')

# ---------- external exercises ----------
X = []
def ext(id, title, source, level, step, skills, pre, stars, url=None, note=""):
    X.append(dict(id=id, title=title, source=source, level=level, step=step, skills=skills, pre=pre, stars=stars, url=url, note=note))

ext("PE1","Multiples of 3 or 5","Project Euler #1","Challenge","4 · Loops","conditional accumulator","A08",2,"https://projecteuler.net/problem=1")
ext("PE6","Sum square difference","Project Euler #6","Challenge","4 · Loops","two accumulators","A05",2,"https://projecteuler.net/problem=6")
ext("PE2","Even Fibonacci numbers","Project Euler #2","Challenge","4 · Loops","state update + filter","S03",3,"https://projecteuler.net/problem=2")
ext("PE4","Largest palindrome product","Project Euler #4","Challenge","8 · Recap","nested loops + palindrome + max","D06, G03",3,"https://projecteuler.net/problem=4")
ext("PE5","Smallest multiple","Project Euler #5","Challenge","8 · Recap","flag/search + `while`","P01",3,"https://projecteuler.net/problem=5")
ext("TCH1","Factorial (teacher)","Teacher topic","Assessment","4 · Loops","product accumulator","A04",2,None,"Compare the exact teacher statement with A04")
ext("TCH2","Fibonacci (teacher)","Teacher topic","Assessment","4 · Loops","state update","S02",3,None,"Compare with S02 / S03")
ext("TCH3","Armstrong numbers (teacher test)","Teacher topic","Assessment","4 · Loops","digits + power + sum","M01",3,None,"Compare with M01 / M02")
