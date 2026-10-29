"""Method specs: the method(s) the learner writes, the given Run code, and test cases.

M[id] = dict(
  run   = body of Run(string[] args): reads input, calls the method, prints (given in the starter),
  methods = [(signature, solution body, starter return)],
  cases = [(method name, [args], expected)]   # checked by tests/Practice.Tests
)
Exercises without an entry are "output" exercises: the learner writes Run itself and
the tests compare what it prints with the examples.
"""
RA = '''Console.Write("How many numbers? ");
int count = int.Parse(Console.ReadLine()!);
int[] values = new int[count];
for (int i = 0; i < values.Length; i++)
{
    Console.Write($"Value {i}: ");
    values[i] = int.Parse(Console.ReadLine()!);
}
'''
def n_in(prompt="N"):
    return f'Console.Write("{prompt}: ");\nint n = int.Parse(Console.ReadLine()!);\n'

def lines(*ls):  # expected drawing: every line ends with a new line
    return "".join(l + "\n" for l in ls)

M = {}
M["B02"] = dict(run='''Console.Write("Width: ");
int width = int.Parse(Console.ReadLine()!);
Console.Write("Height: ");
int height = int.Parse(Console.ReadLine()!);
Console.WriteLine($"Area: {Area(width, height)}");
Console.WriteLine($"Perimeter: {Perimeter(width, height)}");
''', methods=[("public static int Area(int width, int height)", "return width * height;", "return 0;"),
              ("public static int Perimeter(int width, int height)", "return 2 * (width + height);", "return 0;")],
   cases=[("Area",[4,3],12),("Perimeter",[4,3],14),("Area",[5,5],25),("Perimeter",[5,5],20),("Area",[0,7],0)])
M["B03"] = dict(run='''Console.Write("Seconds: ");
int total = int.Parse(Console.ReadLine()!);
Console.WriteLine(Format(total));
''', methods=[("public static string Format(int totalSeconds)", '''int hours = totalSeconds / 3600;
int rest = totalSeconds % 3600;
int minutes = rest / 60;
int seconds = rest % 60;
return $"{hours} h {minutes} min {seconds} s";''', 'return "";')],
   cases=[("Format",[3725],"1 h 2 min 5 s"),("Format",[59],"0 h 0 min 59 s"),("Format",[7200],"2 h 0 min 0 s"),("Format",[0],"0 h 0 min 0 s")])
M["C01"] = dict(run=n_in("Number")+'''if (IsEven(n))
{
    Console.WriteLine($"{n} is even");
}
else
{
    Console.WriteLine($"{n} is odd");
}
''', methods=[("public static bool IsEven(int n)", "return n % 2 == 0;", "return false;")],
   cases=[("IsEven",[7],False),("IsEven",[0],True),("IsEven",[-4],True),("IsEven",[-3],False)])
M["C02"] = dict(run='''Console.Write("First: ");
int a = int.Parse(Console.ReadLine()!);
Console.Write("Second: ");
int b = int.Parse(Console.ReadLine()!);
Console.Write("Third: ");
int c = int.Parse(Console.ReadLine()!);
Console.WriteLine($"Largest: {Largest(a, b, c)}");
''', methods=[("public static int Largest(int a, int b, int c)", '''int largest = a;
if (b > largest)
{
    largest = b;
}
if (c > largest)
{
    largest = c;
}
return largest;''', "return 0;")],
   cases=[("Largest",[3,9,5],9),("Largest",[-1,-7,-3],-1),("Largest",[4,4,2],4),("Largest",[1,2,8],8)])
M["C03"] = dict(run='''Console.Write("Age: ");
int age = int.Parse(Console.ReadLine()!);
Console.WriteLine($"Price: {Price(age)}");
''', methods=[("public static int Price(int age)", '''if (age < 12)
{
    return 5;
}
else if (age >= 65)
{
    return 7;
}
else
{
    return 10;
}''', "return 0;")],
   cases=[("Price",[11],5),("Price",[12],10),("Price",[64],10),("Price",[65],7),("Price",[0],5)])

def simple(id_, name, ret, body, cases, prompt="N", label=None, fmt=None, ptype="int", pname="n"):
    parse = "long.Parse" if ptype == "long" else "int.Parse"
    run = f'Console.Write("{prompt}: ");\n{ptype} {pname} = {parse}(Console.ReadLine()!);\n'
    run += f'Console.WriteLine({fmt or chr(36) + chr(34) + label + ": {" + name + "(" + pname + ")}" + chr(34)});\n'
    todo = {"int":"return 0;","long":"return 0;","double":"return 0;","bool":"return false;","string":'return "";'}[ret]
    M[id_] = dict(run=run, methods=[(f"public static {ret} {name}({ptype} {pname})", body, todo)],
                  cases=[(name, [a], r) for a, r in cases])

simple("A01","SumTo","int",'''int sum = 0;
for (int i = 1; i <= n; i++)
{
    sum += i;
}
return sum;''', [(5,15),(1,1),(10,55),(0,0)], label="Sum")
simple("A02","CountMultiplesOf3","int",'''int count = 0;
for (int i = 1; i <= n; i++)
{
    if (i % 3 == 0)
    {
        count++;
    }
}
return count;''', [(10,3),(2,0),(9,3),(0,0)], label="Count")
simple("A03","SumOfEvens","int",'''int sum = 0;
for (int i = 1; i <= n; i++)
{
    if (i % 2 == 0)
    {
        sum += i;
    }
}
return sum;''', [(6,12),(7,12),(1,0),(10,30)], label="Sum")
simple("A04","Factorial","long",'''long product = 1;
for (int i = 1; i <= n; i++)
{
    product *= i;
}
return product;''', [(5,120),(0,1),(1,1),(12,479001600),(20,2432902008176640000)], fmt='$"{n}! = {Factorial(n)}"')
M["A07"] = dict(run='''Console.Write("Base: ");
int baseValue = int.Parse(Console.ReadLine()!);
Console.Write("Exponent: ");
int exponent = int.Parse(Console.ReadLine()!);
Console.WriteLine($"{baseValue}^{exponent} = {Power(baseValue, exponent)}");
''', methods=[("public static long Power(int baseValue, int exponent)", '''long result = 1;
for (int i = 0; i < exponent; i++)
{
    result *= baseValue;
}
return result;''', "return 0;")],
   cases=[("Power",[3,4],81),("Power",[2,10],1024),("Power",[5,0],1),("Power",[-2,3],-8)])
simple("A08","SumOfMultiples","int",'''int sum = 0;
for (int i = 1; i < n; i++)
{
    if (i % 3 == 0 || i % 5 == 0)
    {
        sum += i;
    }
}
return sum;''', [(10,23),(20,78),(1,0),(16,60)], label="Sum")
simple("A10","SeriesSum","double",'''double sum = 0;
for (int i = 1; i <= n; i++)
{
    sum += 1.0 / i;   // 1.0 makes it a double division
}
return sum;''', [(1,1.0),(2,1.5),(4,2.0833333333)], fmt='$"Sum: {SeriesSum(n):F4}"')
simple("D01","LastDigit","int","return n % 10;", [(352,2),(7,7),(0,0),(90,0)], label="Last digit")
simple("D02","RemoveLastDigit","int","return n / 10;", [(352,35),(7,0),(0,0),(1000,100)], label="Without last digit")
simple("D03","CountDigits","int",'''int digits = 0;
int remaining = n;
do
{
    digits++;
    remaining /= 10;
}
while (remaining > 0);
return digits;''', [(352,3),(0,1),(1000,4),(7,1)], label="Digits")
simple("D04","DigitSum","int",'''int sum = 0;
int remaining = n;
while (remaining > 0)
{
    int digit = remaining % 10;
    sum += digit;
    remaining /= 10;
}
return sum;''', [(352,10),(0,0),(9999,36),(7,7)], label="Digit sum")
simple("D05","ReverseNumber","int",'''int reversed = 0;
int remaining = n;
while (remaining > 0)
{
    int digit = remaining % 10;
    reversed = reversed * 10 + digit;
    remaining /= 10;
}
return reversed;''', [(352,253),(1200,21),(0,0),(7,7)], label="Reversed")
M["D06"] = dict(run=n_in()+'''if (IsPalindrome(n))
{
    Console.WriteLine($"{n} is a palindrome");
}
else
{
    Console.WriteLine($"{n} is not a palindrome");
}
''', methods=[("public static bool IsPalindrome(int n)", '''int reversed = 0;
int remaining = n;          // copy: we need n at the end
while (remaining > 0)
{
    reversed = reversed * 10 + remaining % 10;
    remaining /= 10;
}
return reversed == n;''', "return false;")],
   cases=[("IsPalindrome",[1221],True),("IsPalindrome",[123],False),("IsPalindrome",[7],True),("IsPalindrome",[0],True),("IsPalindrome",[10],False)])
simple("S03","EvenFibonacciSum","long",'''long previous = 0;
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
return sum;''', [(10,10),(100,44),(1,0),(34,44)], prompt="Limit", label="Sum", ptype="long", pname="limit")
M["P01"] = dict(run=n_in()+'''if (IsPrime(n))
{
    Console.WriteLine($"{n} is prime");
}
else
{
    Console.WriteLine($"{n} is not prime");
}
''', methods=[("public static bool IsPrime(int n)", '''bool isPrime = n >= 2;
for (int d = 2; d * d <= n; d++)
{
    if (n % d == 0)
    {
        isPrime = false;
        break;
    }
}
return isPrime;''', "return false;")],
   cases=[("IsPrime",[7],True),("IsPrime",[9],False),("IsPrime",[1],False),("IsPrime",[2],True),("IsPrime",[97],True),("IsPrime",[0],False)])
ARM = '''// 1. count the digits
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
return sum == n;'''
M["M01"] = dict(run=n_in()+'''if (IsArmstrong(n))
{
    Console.WriteLine($"{n} is an Armstrong number");
}
else
{
    Console.WriteLine($"{n} is not an Armstrong number");
}
''', methods=[("public static bool IsArmstrong(int n)", ARM, "return false;")],
   cases=[("IsArmstrong",[153],True),("IsArmstrong",[154],False),("IsArmstrong",[9474],True),("IsArmstrong",[0],True),("IsArmstrong",[10],False),("IsArmstrong",[370],True)])
M["N01"] = dict(run='''Console.Write("From: ");
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
''', methods=[("public static int CountDigits(int n)", '''int digits = 0;
do
{
    digits++;
    n /= 10;
}
while (n > 0);
return digits;''', "return 0;"),
 ("public static int Power(int baseValue, int exponent)", '''int result = 1;
for (int i = 0; i < exponent; i++)
{
    result *= baseValue;
}
return result;''', "return 0;"),
 ("public static bool IsArmstrong(int n)", '''int digits = CountDigits(n);
int sum = 0;
int remaining = n;
while (remaining > 0)
{
    sum += Power(remaining % 10, digits);
    remaining /= 10;
}
return sum == n;''', "return false;")],
   cases=[("CountDigits",[352],3),("CountDigits",[0],1),("Power",[3,4],81),("Power",[5,0],1),("IsArmstrong",[153],True),("IsArmstrong",[154],False),("IsArmstrong",[9474],True)])

# arrays
M["R01"] = dict(run=RA+'Console.WriteLine($"Sum: {Sum(values)}");\n', methods=[("public static int Sum(int[] values)", '''int sum = 0;
foreach (int value in values)
{
    sum += value;
}
return sum;''', "return 0;")], cases=[("Sum",[[4,9,2]],15),("Sum",[[-5]],-5),("Sum",[[]],0)])
M["R02"] = dict(run=RA+'''int index = IndexOfLargest(values);
Console.WriteLine($"Largest: {values[index]} at index {index}");
''', methods=[("public static int IndexOfLargest(int[] values)", '''int maxIndex = 0;
for (int i = 1; i < values.Length; i++)
{
    if (values[i] > values[maxIndex])
    {
        maxIndex = i;
    }
}
return maxIndex;''', "return 0;")], cases=[("IndexOfLargest",[[-5,-2,-9]],1),("IndexOfLargest",[[3,7,2,7,1]],1),("IndexOfLargest",[[4]],0),("IndexOfLargest",[[1,2,9]],2)])
M["R03"] = dict(run=RA+'''Console.Write("Target: ");
int target = int.Parse(Console.ReadLine()!);
Console.WriteLine($"{target} appears {CountMatches(values, target)} times");
''', methods=[("public static int CountMatches(int[] values, int target)", '''int matches = 0;
foreach (int value in values)
{
    if (value == target)
    {
        matches++;
    }
}
return matches;''', "return 0;")], cases=[("CountMatches",[[2,4,2,5,2],2],3),("CountMatches",[[1,1],9],0),("CountMatches",[[],3],0)])
M["R04"] = dict(run=RA+'''Console.Write("Target: ");
int target = int.Parse(Console.ReadLine()!);
int index = IndexOf(values, target);
if (index == -1)
{
    Console.WriteLine("Not found");
}
else
{
    Console.WriteLine($"First position: {index}");
}
''', methods=[("public static int IndexOf(int[] values, int target)", '''for (int i = 0; i < values.Length; i++)
{
    if (values[i] == target)
    {
        return i;
    }
}
return -1;''', "return -1;")], cases=[("IndexOf",[[7,3,9,3],3],1),("IndexOf",[[7,3,9,3],8],-1),("IndexOf",[[5],5],0),("IndexOf",[[],1],-1)])
M["R05"] = dict(run=RA+'''foreach (int value in Reversed(values))
{
    Console.Write(value + " ");
}
Console.WriteLine();
''', methods=[("public static int[] Reversed(int[] values)", '''int[] reversed = new int[values.Length];
for (int i = 0; i < values.Length; i++)
{
    reversed[values.Length - 1 - i] = values[i];
}
return reversed;''', "return new int[0];")], cases=[("Reversed",[[1,2,3,4]],[4,3,2,1]),("Reversed",[[8]],[8]),("Reversed",[[]],[])])
# text
M["T01"] = dict(run='''Console.Write("Text: ");
string text = Console.ReadLine()!;
Console.Write("Letter: ");
char letter = Console.ReadLine()![0];
Console.WriteLine($"{letter} appears {CountLetter(text, letter)} times");
''', methods=[("public static int CountLetter(string text, char letter)", '''int count = 0;
foreach (char c in text)
{
    if (c == letter)
    {
        count++;
    }
}
return count;''', "return 0;")], cases=[("CountLetter",["banana","a"],3),("CountLetter",["BANANA","a"],0),("CountLetter",["","a"],0)])
M["T02"] = dict(run='''Console.Write("Text: ");
string text = Console.ReadLine()!;
Console.WriteLine($"[{RemoveSpaces(text)}]");
''', methods=[("public static string RemoveSpaces(string text)", '''string result = "";
foreach (char c in text)
{
    if (c != ' ')
    {
        result += c;
    }
}
return result;''', 'return "";')], cases=[("RemoveSpaces",["a b c"],"abc"),("RemoveSpaces",["   "],""),("RemoveSpaces",["no-space"],"no-space")])
M["T03"] = dict(run='''Console.Write("Text: ");
string text = Console.ReadLine()!;
string kept = KeepDigits(text);
Console.WriteLine($"Digits: {kept.Length}");
Console.WriteLine($"Kept: {kept}");
''', methods=[("public static string KeepDigits(string text)", '''string kept = "";
foreach (char c in text)
{
    if (c >= '0' && c <= '9')
    {
        kept += c;
    }
}
return kept;''', 'return "";')], cases=[("KeepDigits",["a1 b2!"],"12"),("KeepDigits",["abc"],""),("KeepDigits",["2026"],"2026")])
# drawings: a void method that prints the picture; the tests capture what it prints
def draw(id_, name, params, read, body, cases):
    M[id_] = dict(run=read + f'{name}({", ".join(p.split()[1] for p in params)});\n',
                  methods=[(f"public static void {name}({', '.join(params)})", body, "")],
                  cases=[(name, a, r) for a, r in cases])
RW = '''Console.Write("Width: ");
int width = int.Parse(Console.ReadLine()!);
Console.Write("Height: ");
int height = int.Parse(Console.ReadLine()!);
'''
draw("G01","DrawRectangle",["int width","int height"],RW,'''for (int row = 1; row <= height; row++)
{
    for (int col = 1; col <= width; col++)
    {
        Console.Write("*");
    }
    Console.WriteLine();
}''', [([4,3],lines("****","****","****")),([1,2],lines("*","*"))])
draw("G02","DrawTriangle",["int height"],'Console.Write("Height: ");\nint height = int.Parse(Console.ReadLine()!);\n','''for (int row = 1; row <= height; row++)
{
    for (int col = 1; col <= row; col++)
    {
        Console.Write("*");
    }
    Console.WriteLine();
}''', [([4],lines("*","**","***","****")),([1],lines("*"))])
draw("G03","DrawGrid",["int n"],n_in(),'''for (int row = 1; row <= n; row++)
{
    for (int col = 1; col <= n; col++)
    {
        Console.Write($"{row * col,4}");
    }
    Console.WriteLine();
}''', [([4],lines("   1   2   3   4","   2   4   6   8","   3   6   9  12","   4   8  12  16")),([1],lines("   1"))])
draw("G04","DrawHollowRectangle",["int width","int height"],RW,'''for (int row = 1; row <= height; row++)
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
}''', [([5,4],lines("*****","*   *","*   *","*****")),([3,3],lines("***","* *","***"))])
draw("G05","DrawCheckerboard",["int size"],'Console.Write("Size: ");\nint size = int.Parse(Console.ReadLine()!);\n','''for (int row = 1; row <= size; row++)
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
}''', [([4],lines("#.#.",".#.#","#.#.",".#.#")),([1],lines("#"))])
draw("G06","DrawPyramid",["int height"],'Console.Write("Height: ");\nint height = int.Parse(Console.ReadLine()!);\n','''for (int row = 1; row <= height; row++)
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
}''', [([3],lines("  *"," ***","*****")),([1],lines("*"))])

# What the method must do, in plain words (shown on the page and in the starter instead of the
# "read … print …" story, because the method gets its input as parameters and returns its result).
GOALS = {
 "B02": "`Area` gives back width × height. `Perimeter` gives back 2 × (width + height).",
 "B03": "Turn a number of seconds into text like `1 h 2 min 5 s`. This trains `/` and `%`, the key tools of the digit recipe later.",
 "C01": "Give back `true` if `n` is even, `false` if it is odd.",
 "C02": "Give back the largest of the three numbers.",
 "C03": "A cinema ticket costs 5 for children under 12, 7 for people aged 65 or more, and 10 for everyone else. Give back the price for `age`.",
 "A01": "Give back the sum 1 + 2 + … + n.",
 "A02": "Count how many numbers from 1 to n (included) are divisible by 3.",
 "A03": "Give back the sum of the even numbers from 1 to n.",
 "A04": "Give back n! = 1 × 2 × … × n (0 ≤ n ≤ 20). By definition 0! = 1.",
 "A07": "Give back `baseValue` to the power `exponent` (exponent ≥ 0), using a loop.",
 "A08": "Give back the sum of all numbers **below** n that are multiples of 3 or 5.",
 "A10": "Give back the sum 1 + 1/2 + 1/3 + … + 1/n as a `double`.",
 "D01": "Give back the last digit of n (n ≥ 0).",
 "D02": "Give back n without its last digit (n ≥ 0).",
 "D03": "Give back how many digits n has (n ≥ 0). 0 has 1 digit.",
 "D04": "Give back the sum of the digits of n (n ≥ 0).",
 "D05": "Give back n with its digits in reverse order (n ≥ 0): 352 → 253.",
 "D06": "Give back `true` if n reads the same in both directions (n ≥ 0).",
 "S03": "Add up the **even** Fibonacci numbers that are **not greater** than `limit`, and give back the sum.",
 "P01": "Give back `true` if n is a prime number (≥ 2 and only divisible by 1 and itself).",
 "M01": "An Armstrong number equals the sum of its digits, each raised to the power **number of digits**. Give back `true` if n is one. Example: 153 → 3 digits → 1³ + 5³ + 3³ = 153, so yes.",
 "N01": "Split the Armstrong check into three small methods: `CountDigits`, `Power` and `IsArmstrong` (which uses the other two).",
 "R01": "Give back the sum of all values in the array.",
 "R02": "Give back the **position** (index) of the largest value in the array (the first one if it appears twice). The array has at least 1 value.",
 "R03": "Give back how many times `target` appears in the array.",
 "R04": "Give back the **first** index where `target` is, or -1 if it is not in the array.",
 "R05": "Give back a **new** array with the same values in reverse order.",
 "T01": "Give back how many times `letter` appears in `text` (case-sensitive).",
 "T02": "Give back `text` without its spaces.",
 "T03": "Give back a new text with only the digit characters of `text`, in order.",
 "G01": "Print a rectangle of `*`, `width` wide and `height` high.",
 "G02": "Print a right triangle of `height` rows: row 1 has 1 star, row 2 has 2 stars, …",
 "G03": "Print an n×n grid where the cell at row `r` and column `c` contains `r × c`. Each number takes 4 characters (right-aligned).",
 "G04": "Print only the border of a `width` × `height` rectangle with `*`; the inside is spaces.",
 "G05": "Print a size×size checkerboard with `#` and `.`, starting with `#` in the top-left corner.",
 "G06": "Print a centered pyramid of `*`, `height` rows high.",
}

# Rules that only made sense when the learner also wrote the input reading.
RULES = {
 "B02": ["Use `*`, `+` and `return`. No `if` needed."],
 "R01": ["One loop over the array. No LINQ (`.Sum()`)."],
}

# Hints that only made sense when the learner also wrote the input/output code.
HINTS = {
 'B02': ['Area = width × height. Perimeter = 2 × (width + height).', 'Each method is one line: `return width * height;`.'],
 'A01': ['Fill the trace table for N = 4 first: `i`, `sum before`, `sum after`.', 'The box `sum` is created **before** the loop and starts at 0.', 'Inside the loop: `sum += i;`. `return sum;` **after** the loop.'],
 'A10': ['The box is a `double` that starts at 0.', 'Each turn adds `1.0 / i`.', '`1 / i` with two `int`s is 0! Write `1.0 / i` to get a `double` division.'],
 'P01': ['Try every divisor `d` from 2 to N − 1. One divisor is enough to say "not prime".', 'Flag: `bool isPrime = n >= 2;` and set it to `false` when `n % d == 0`.', 'Do not `return true` inside the loop: you only know it is prime **after** checking every divisor.'],
 'R03': ['The array is already filled for you: it is the parameter `values`. Which recipe counts only *some* values?', 'Conditional accumulator: `if (value == target) count++;`'],
 'R04': ['Box `int index = -1;` (means not found).', 'When found: `index = i; break;`', 'You can `return i;` as soon as you find it. After the loop, `return -1;`.'],
 'T01': ["`letter` is a `char` (single quotes: `'a'`). Compare each `c` of the text with it: `c == letter`.", '`if (c == letter) count++;`'],
 'N01': ['`static int CountDigits(int n) { ... return digits; }`', '`IsArmstrong` calls the two others and returns a `bool`.', 'Test each method alone first: `./ex check` shows which one is wrong, and `./ex run` lets you try your own values.'],
}
