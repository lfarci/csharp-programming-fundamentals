"""Drill bank: many NEAR variations of one recipe, so the pattern sticks (part-task practice).

Each drill changes only the target (sum odds vs sum evens, count by 3 vs by 5).
One idea per drill. Keep goals to 1-2 short sentences.
DRILLS lists the drill sets shown in exercises/README.md: keep it up to date.
"""
from data4 import ex, E
from data5 import M, GOALS, lines
import data6  # noqa: F401  (C04, L09, L10, A11, A12, G07, D07, R06 must exist first)

TODO = {"int": "return 0;", "long": "return 0;", "bool": "return false;", "void": ""}

def drill(id_, slug, title, sig, body, cases, goal, hints, edge, mastery, theme, recipes, pre,
          level="Guided", stars=1, sort=None):
    ret = sig.split()[0]; name = sig.split()[1].split("(")[0]
    k = dict(id=id_, slug=slug, title=title, level=level, stars=stars, theme=theme, recipes=recipes, pre=pre,
             goal="", examples=[], edge=edge, constraints=["Write the loop yourself."], hints=hints,
             mastery=mastery, code="")
    if sort: k["sort"] = sort
    ex(**k)
    M[id_] = dict(run="", methods=[(f"public static {sig}", body, TODO[ret])],
                  cases=[(name, a, r) for a, r in cases])
    GOALS[id_] = goal

L4A, L4B, L4C, L4D = "loops-repeat", "loops-running-result", "loops-2d", "loops-digits"

# ---------- L · the loop itself: print / count / step ----------
def ploop(id_, slug, title, sig, body, cases, goal, hints, edge, mastery, pre, **k):
    drill(id_, slug, title, sig, body, [(a, lines(*map(str, r))) for a, r in cases], goal, hints, edge, mastery, L4A, ["01"], pre, **k)

ploop("L11", "count-from-a-to-b", "Count from a to b", "void PrintFromTo(int a, int b)",
"""for (int i = a; i <= b; i++)
{
    Console.WriteLine(i);
}""", [([3, 6], [3, 4, 5, 6]), ([5, 5], [5]), ([-2, 1], [-2, -1, 0, 1])],
 "Print the numbers from `a` to `b` (both included), one per line.",
 ["The counter starts at `a`, not at 1.", "The test is `i <= b`."],
 ["`a` equal to `b`: one line.", "`a` bigger than `b`: nothing is printed."],
 "Print from `a` to `b` but skip `a` itself.", ["L03"])
ploop("L12", "count-down", "Count down", "void CountDown(int n)",
"""for (int i = n; i >= 1; i--)
{
    Console.WriteLine(i);
}""", [([4], [4, 3, 2, 1]), ([1], [1])],
 "Print n, n−1, …, 1, one per line.",
 ["Start at `n`. Step with `i--`.", "Keep going while `i >= 1`."], ["`CountDown(0)` prints nothing."],
 "Count down from n to 0 (0 included).", ["L11"])
ploop("L13", "count-by-3", "Count by 3", "void CountBy3(int n)",
"""for (int i = 3; i <= n; i += 3)
{
    Console.WriteLine(i);
}""", [([10], [3, 6, 9]), ([3], [3]), ([12], [3, 6, 9, 12])],
 "Print 3, 6, 9, … up to n (included when it is a multiple of 3), one per line.",
 ["Start at 3. The step is `i += 3`.", "The test is `i <= n`."], ["n smaller than 3: nothing is printed."],
 "Count by 4 up to n.", ["L11"])
ploop("L14", "count-by-5", "Count by 5", "void CountBy5(int n)",
"""for (int i = 5; i <= n; i += 5)
{
    Console.WriteLine(i);
}""", [([22], [5, 10, 15, 20]), ([5], [5])],
 "Print 5, 10, 15, … up to n, one per line.",
 ["Same loop as L13: only the start and the step change.", "Start at 5, step `i += 5`."], ["n = 4: nothing."],
 "Count by 10 up to n.", ["L13"])
ploop("L15", "count-by-step", "Count by any step", "void CountByStep(int step, int n)",
"""for (int i = step; i <= n; i += step)
{
    Console.WriteLine(i);
}""", [([2, 7], [2, 4, 6]), ([4, 12], [4, 8, 12]), ([1, 3], [1, 2, 3])],
 "Print `step`, 2×`step`, 3×`step`, … up to n, one per line. (`step` is at least 1.)",
 ["L13 and L14 with the 3 or 5 replaced by `step`.", "Start at `step`, step `i += step`."], ["`step` bigger than n: nothing."],
 "Print the multiples of `step` from n down to `step`.", ["L14"], level="Independent", stars=2)
ploop("L16", "odd-numbers", "Odd numbers", "void PrintOdds(int n)",
"""for (int i = 1; i <= n; i += 2)
{
    Console.WriteLine(i);
}""", [([7], [1, 3, 5, 7]), ([8], [1, 3, 5, 7]), ([1], [1])],
 "Print the odd numbers 1, 3, 5, … up to n, one per line.",
 ["Start at 1, step `i += 2`.", "Compare with L06 (even numbers): only the start changes."], ["n even: the last number is n − 1."],
 "Print the odd numbers from n down to 1.", ["L11"])
ploop("L17", "count-down-by-2", "Count down by 2", "void CountDownBy2(int n)",
"""for (int i = n; i >= 1; i -= 2)
{
    Console.WriteLine(i);
}""", [([9], [9, 7, 5, 3, 1]), ([6], [6, 4, 2])],
 "Print n, n−2, n−4, … while the number is at least 1, one per line.",
 ["L12 with a step of `i -= 2`.", "Test `i >= 1`."], ["n = 1: one line."],
 "Count down by 3 from n.", ["L12"])
ploop("L18", "squares", "Square numbers", "void PrintSquares(int n)",
"""for (int i = 1; i <= n; i++)
{
    Console.WriteLine(i * i);
}""", [([4], [1, 4, 9, 16]), ([1], [1])],
 "Print 1², 2², …, n² (1, 4, 9, …), one per line.",
 ["A normal 1 to n loop.", "Print `i * i` instead of `i`."], ["n = 0: nothing."],
 "Print the cubes 1, 8, 27, … up to n³.", ["L11"])
drill("L19", "count-the-turns", "Count the turns", "int CountTurns(int a, int b)",
"""int turns = 0;
for (int i = a; i <= b; i++)
{
    turns++;
}
return turns;""", [([1, 5], 5), ([3, 3], 1), ([4, 10], 7), ([5, 4], 0)],
 "Give back how many times a loop from `a` to `b` (both included) runs. Count with a loop, not with a formula.",
 ["A counter box `turns = 0` before the loop.", "`turns++` inside the loop, `return turns;` after it."],
 ["`a` bigger than `b`: 0 turns."], "How many turns does a loop from `a` to `b` with step 2 do?", L4A, ["01", "02"], ["L11"])

# ---------- A · accumulators ----------
def acc(id_, slug, title, sig, body, cases, goal, hints, edge, mastery, pre, recipes=["02"], **k):
    drill(id_, slug, title, sig, body, cases, goal, hints, edge, mastery, L4B, recipes, pre, **k)

acc("A13", "sum-from-a-to-b", "Sum from a to b", "int SumFromTo(int a, int b)",
"""int sum = 0;
for (int i = a; i <= b; i++)
{
    sum += i;
}
return sum;""", [([3, 5], 12), ([1, 4], 10), ([7, 7], 7), ([5, 4], 0)],
 "Give back a + (a+1) + … + b.",
 ["A01 with the loop starting at `a`.", "`sum = 0` before, `sum += i` inside, `return sum` after."], ["`a` bigger than `b`: 0."],
 "Sum the numbers from `b` down to `a`.", ["A01"])
acc("A14", "sum-odd-numbers", "Sum the odd numbers", "int SumOfOdds(int n)",
"""int sum = 0;
for (int i = 1; i <= n; i += 2)
{
    sum += i;
}
return sum;""", [([5], 9), ([6], 9), ([1], 1), ([0], 0)],
 "Give back 1 + 3 + 5 + … (the odd numbers up to n).",
 ["Loop over 1, 3, 5, … with `i += 2` (like L16).", "Add each one to `sum`."], ["n = 0: 0."],
 "Do it again with `i++` and an `if (i % 2 != 0)`.", ["A01", "L16"])
acc("A15", "count-even-numbers", "Count the even numbers", "int CountEvens(int n)",
"""int count = 0;
for (int i = 1; i <= n; i++)
{
    if (i % 2 == 0)
    {
        count++;
    }
}
return count;""", [([10], 5), ([7], 3), ([1], 0)],
 "Give back how many numbers from 1 to n are even.",
 ["Like A02: only the test changes.", "`if (i % 2 == 0) count++;`"], ["n = 1: 0."],
 "Count the odd numbers from 1 to n.", ["A02"], recipes=["03"])
acc("A16", "count-multiples-of-5", "Count multiples of 5", "int CountMultiplesOf5(int n)",
"""int count = 0;
for (int i = 1; i <= n; i++)
{
    if (i % 5 == 0)
    {
        count++;
    }
}
return count;""", [([20], 4), ([4], 0), ([26], 5)],
 "Give back how many numbers from 1 to n are divisible by 5.",
 ["A02 with 5 instead of 3.", "`i % 5 == 0` means: divisible by 5."], ["n below 5: 0."],
 "Count the multiples of 7 from 1 to n.", ["A15"], recipes=["03"])
acc("A17", "sum-multiples-of-k", "Sum the multiples of k", "int SumMultiplesOf(int k, int n)",
"""int sum = 0;
for (int i = 1; i <= n; i++)
{
    if (i % k == 0)
    {
        sum += i;
    }
}
return sum;""", [([3, 10], 18), ([5, 20], 50), ([4, 3], 0)],
 "Give back the sum of the numbers from 1 to n that are divisible by k (k ≥ 1).",
 ["Like A03, with `k` instead of 2.", "`if (i % k == 0) sum += i;`"], ["k bigger than n: 0."],
 "Count them instead of adding them.", ["A03", "A16"], recipes=["03"], level="Independent", stars=2)
acc("A18", "sum-of-cubes", "Sum of cubes", "int SumOfCubes(int n)",
"""int sum = 0;
for (int i = 1; i <= n; i++)
{
    sum += i * i * i;
}
return sum;""", [([3], 36), ([1], 1), ([4], 100), ([0], 0)],
 "Give back 1³ + 2³ + … + n³.",
 ["A11 (squares) with `i * i * i`.", "Box before, add inside, return after."], ["n = 0: 0."],
 "Sum 1 + 4 + 9 + … from memory, without looking at A11.", ["A11"])
acc("A19", "product-from-a-to-b", "Product from a to b", "long ProductFromTo(int a, int b)",
"""long product = 1;
for (int i = a; i <= b; i++)
{
    product *= i;
}
return product;""", [([2, 4], 24), ([3, 3], 3), ([1, 5], 120), ([5, 4], 1)],
 "Give back a × (a+1) × … × b. If `a` is bigger than `b`, give back 1.",
 ["Like A04: the box starts at 1.", "The loop starts at `a`."], ["`a` bigger than `b`: 1 (nothing was multiplied)."],
 "Multiply only the even numbers from a to b.", ["A04"])
acc("A20", "powers-of-2", "Power of 2", "long PowerOf2(int n)",
"""long result = 1;
for (int i = 1; i <= n; i++)
{
    result *= 2;
}
return result;""", [([3], 8), ([0], 1), ([10], 1024)],
 "Give back 2 to the power n (n ≥ 0), by multiplying by 2, n times.",
 ["Product box `result = 1`.", "The loop runs n times; each turn: `result *= 2`."], ["n = 0: 1."],
 "Give back 3 to the power n.", ["A04"])
acc("A21", "count-divisors", "Count the divisors", "int CountDivisors(int n)",
"""int count = 0;
for (int d = 1; d <= n; d++)
{
    if (n % d == 0)
    {
        count++;
    }
}
return count;""", [([6], 4), ([7], 2), ([1], 1), ([12], 6)],
 "Give back how many numbers from 1 to n divide n exactly (n ≥ 1).",
 ["Loop d from 1 to n.", "`n % d == 0` means d divides n. Count it."], ["n = 1: 1 divisor."],
 "Give back how many divisors are even.", ["A16"], recipes=["03"])
acc("A22", "sum-of-divisors", "Sum of the divisors", "int SumOfDivisors(int n)",
"""int sum = 0;
for (int d = 1; d <= n; d++)
{
    if (n % d == 0)
    {
        sum += d;
    }
}
return sum;""", [([6], 12), ([7], 8), ([1], 1)],
 "Give back the sum of all numbers from 1 to n that divide n exactly (n ≥ 1).",
 ["A21 with `sum += d` instead of `count++`.", "`sum = 0` before the loop."], ["n = 1: 1."],
 "Sum the divisors below n only (6 → 1 + 2 + 3 = 6).", ["A21"], recipes=["03"])

# ---------- G · nested loops ----------
def grid(id_, slug, title, sig, body, cases, goal, hints, edge, mastery, pre, sort, **k):
    drill(id_, slug, title, sig, body, [(a, lines(*r)) for a, r in cases], goal, hints, edge, mastery, L4C, ["08"], pre, sort=sort, **k)

grid("G08", "solid-square", "Solid square", "void DrawSquare(int size)",
"""for (int row = 1; row <= size; row++)
{
    for (int col = 1; col <= size; col++)
    {
        Console.Write("*");
    }
    Console.WriteLine();
}""", [([3], ["***", "***", "***"]), ([1], ["*"])],
 "Print a square of `*`, `size` wide and `size` high.",
 ["G01 with width and height both equal to `size`.", "Inner loop: one row. Outer loop: repeat the row."], ["size = 1: one star."],
 "Print a square of `o`.", ["G01"], "G011")
grid("G09", "number-rows", "Rows of numbers", "void DrawNumberRows(int width, int height)",
"""for (int row = 1; row <= height; row++)
{
    for (int col = 1; col <= width; col++)
    {
        Console.Write(col);
    }
    Console.WriteLine();
}""", [([4, 2], ["1234", "1234"]), ([3, 3], ["123", "123", "123"])],
 "Print `height` rows; each row is `1234…` up to `width`.",
 ["G01, but print `col` instead of `*`.", "`Console.Write(col);`"], ["width = 1: every row is `1`."],
 "Print the row number instead: `111`, `222`, `333`.", ["G08"], "G012")
grid("G10", "row-number-triangle", "Triangle of row numbers", "void DrawRowTriangle(int height)",
"""for (int row = 1; row <= height; row++)
{
    for (int col = 1; col <= row; col++)
    {
        Console.Write(row);
    }
    Console.WriteLine();
}""", [([3], ["1", "22", "333"]), ([1], ["1"])],
 "Print a triangle where row r is the digit r, written r times: `1`, `22`, `333`.",
 ["G02 (triangle): the inner loop goes up to `row`.", "Print `row` instead of `*`."], ["height = 1: `1`."],
 "Print `1`, `12`, `123` instead.", ["G02"], "G021")
grid("G11", "counting-triangle", "Counting triangle", "void DrawCountingTriangle(int height)",
"""for (int row = 1; row <= height; row++)
{
    for (int col = 1; col <= row; col++)
    {
        Console.Write(col);
    }
    Console.WriteLine();
}""", [([4], ["1", "12", "123", "1234"]), ([1], ["1"])],
 "Print a triangle where row r is `12…r`: `1`, `12`, `123`.",
 ["G10, printing `col` instead of `row`.", "Inner loop: `col` from 1 to `row`."], ["height = 1: `1`."],
 "Print the same triangle upside down.", ["G10"], "G022")
grid("G12", "upside-down-triangle", "Upside-down triangle", "void DrawUpsideDown(int height)",
"""for (int row = height; row >= 1; row--)
{
    for (int col = 1; col <= row; col++)
    {
        Console.Write("*");
    }
    Console.WriteLine();
}""", [([3], ["***", "**", "*"]), ([1], ["*"])],
 "Print a triangle whose first row has `height` stars, then one less on each row.",
 ["Make the outer loop count down: `row = height; row >= 1; row--`.", "The inner loop stays `col <= row`."], ["height = 1: one star."],
 "Print the counting triangle (G11) upside down.", ["G02", "L12"], "G023")
grid("G13", "diagonal", "Diagonal", "void DrawDiagonal(int size)",
"""for (int row = 1; row <= size; row++)
{
    for (int col = 1; col <= size; col++)
    {
        if (row == col)
        {
            Console.Write("*");
        }
        else
        {
            Console.Write(".");
        }
    }
    Console.WriteLine();
}""", [([3], ["*..", ".*.", "..*"]), ([1], ["*"])],
 "Print a `size` × `size` square of `.` with `*` on the diagonal (where row equals column).",
 ["G08 square, with an `if` inside the inner loop.", "`if (row == col)` print `*`, else `.`."], ["size = 1: `*`."],
 "Put the `*` on the other diagonal (`row + col == size + 1`).", ["G08", "G04"], "G041", level="Independent", stars=2)

# ---------- D · digits ----------
def dig(id_, slug, title, sig, body, cases, goal, hints, edge, mastery, pre, sort, recipes=["06"], **k):
    drill(id_, slug, title, sig, body, cases, goal, hints, edge, mastery, L4D, recipes, pre, sort=sort, **k)

dig("D08", "first-digit", "First digit", "int FirstDigit(int n)",
"""while (n >= 10)
{
    n /= 10;
}
return n;""", [([352], 3), ([7], 7), ([1000], 1), ([90], 9)],
 "Give back the first (leftmost) digit of n (n ≥ 0).",
 ["Remove the last digit (`/ 10`) again and again.", "Stop when only one digit is left: `while (n >= 10)`."], ["One digit: n itself."],
 "Give back the second digit from the left.", ["D03"], "D035")
dig("D09", "count-even-digits", "Count the even digits", "int CountEvenDigits(int n)",
"""int count = 0;
while (n > 0)
{
    if (n % 10 % 2 == 0)
    {
        count++;
    }
    n /= 10;
}
return count;""", [([2468], 4), ([135], 0), ([1234], 2)],
 "Give back how many digits of n are even (n > 0).",
 ["The D04 loop: take the last digit with `int digit = n % 10;`, then remove it with `n /= 10;`.", "Between the two, count it only if `digit % 2 == 0`."], ["No even digit: 0."],
 "Count the odd digits.", ["D04"], "D041", recipes=["06", "03"])
dig("D10", "count-a-digit", "Count one digit", "int CountDigit(int n, int digit)",
"""int count = 0;
while (n > 0)
{
    if (n % 10 == digit)
    {
        count++;
    }
    n /= 10;
}
return count;""", [([1717, 7], 2), ([123, 9], 0), ([555, 5], 3)],
 "Give back how many times `digit` appears in n (n > 0).",
 ["D09 with the test `n % 10 == digit`.", "Do not forget `n /= 10`."], ["The digit is not there: 0."],
 "Give back `true` if the digit appears at least once.", ["D09"], "D042", recipes=["06", "03"])
dig("D11", "largest-digit", "Largest digit", "int LargestDigit(int n)",
"""int max = 0;
while (n > 0)
{
    if (n % 10 > max)
    {
        max = n % 10;
    }
    n /= 10;
}
return max;""", [([3829], 9), ([111], 1), ([5], 5), ([2061], 6)],
 "Give back the largest digit of n (n > 0).",
 ["The D04 loop, with a max box instead of a sum.", "A digit is never below 0, so `max = 0` is a safe start."], ["One digit: itself."],
 "Give back the smallest digit.", ["D04", "C02"], "D043", recipes=["06", "04"], level="Independent", stars=2)
dig("D12", "product-of-digits", "Product of the digits", "int ProductOfDigits(int n)",
"""int product = 1;
while (n > 0)
{
    product *= n % 10;
    n /= 10;
}
return product;""", [([234], 24), ([5], 5), ([105], 0), ([1111], 1)],
 "Give back the product of the digits of n (n > 0): 234 → 2 × 3 × 4 = 24.",
 ["D04 with a product box: start at 1.", "`product *= n % 10;`"], ["A 0 digit makes the product 0."],
 "Give back the sum of the digits squared.", ["D04"], "D044", recipes=["06", "02"])

# ---------- S · changing state ----------
drill("S04", "doubling", "Doubling", "void PrintDoubling(int start, int count)",
"""int value = start;
for (int i = 1; i <= count; i++)
{
    Console.WriteLine(value);
    value = value * 2;
}""", [([1, 5], lines("1", "2", "4", "8", "16")), ([3, 3], lines("3", "6", "12"))],
 "Print `count` values: `start`, then each value doubled (`3, 6, 12`).",
 ["One box `value`, starting at `start`.", "Each turn: print it, then `value = value * 2;`."], ["count = 0: nothing."],
 "Each value is the previous one plus 3.", "loops-state", ["07"], ["L11"], sort="S015")
drill("S05", "nth-fibonacci", "The n-th Fibonacci number", "long Fibonacci(int n)",
"""long previous = 0;
long current = 1;
for (int i = 0; i < n; i++)
{
    long next = previous + current;
    previous = current;
    current = next;
}
return previous;""", [([0], 0), ([1], 1), ([6], 8), ([10], 55)],
 "Give back the Fibonacci number at position n: position 0 is 0, position 1 is 1, then 1, 2, 3, 5, 8, …",
 ["S02 without printing: do the same 3 moves n times.", "After the loop, `previous` holds the answer."], ["n = 0: 0."],
 "Give back the sum of the first n Fibonacci numbers.", "loops-state", ["07"], ["S02"], level="Independent", stars=2, sort="S025")

# ---------- drill sets (shown in exercises/README.md) ----------
DRILLS = [
 ("Counter loop (print, count, step)", "01", ["L03", "L11", "L12", "L13", "L14", "L16", "L17", "L18", "L15", "L19", "L06"]),
 ("Accumulator (sum, product)", "02", ["A11", "A01", "A13", "A14", "A18", "A04", "A19", "A20", "A07", "A10"]),
 ("Count or sum only some values", "03", ["A02", "A15", "A16", "A03", "A17", "A21", "A22", "A12", "A08"]),
 ("Nested loops (draw)", "08", ["L09", "L10", "G07", "G01", "G08", "G09", "G02", "G10", "G11", "G12", "G04", "G13", "G05"]),
 ("Digits", "06", ["D01", "D02", "D03", "D08", "D04", "D09", "D10", "D11", "D12", "D07", "D05"]),
 ("Changing state", "07", ["S01", "S04", "S02", "S05", "S03"]),
]

# ---------- G14: column formatting alone, before G03 needs it inside a grid ----------
drill("G14", "numbers-in-columns", "Numbers in columns", "void PrintInColumns(int n)",
"""for (int i = 1; i <= n; i++)
{
    Console.Write($"{i * 10,4}");
}
Console.WriteLine();""", [([3], lines("  10  20  30")), ([1], lines("  10")), ([12], lines("  10  20  30  40  50  60  70  80  90 100 110 120"))],
 "Print 10, 20, …, n × 10 on **one** line, each number in a column 4 characters wide.",
 ["`$\"{x,4}\"` writes x right-aligned in 4 characters: `10` becomes `  10` (2 spaces + 2 digits).",
  "L10 with `Console.Write($\"{i * 10,4}\")` and no extra spaces.", "One `Console.WriteLine()` after the loop."],
 ["n = 12: `100` takes 3 characters, so it gets 1 space."], "Print 1, 4, 9, …, n² in columns 5 wide.",
 L4C, ["01", "08"], ["L10"], sort="G029")
for e in E:
    if e["id"] == "G03" and "G14" not in e["pre"]: e["pre"] = e["pre"] + ["G14"]
CHECK = {
 "A11": "every line you need is already in the file. Check the order: the box line before the loop, the update between { and }, the return after the loop. Did you remove every // and the line return -1; ?",
 "G07": "every line is already in the file. The inner for (col) goes inside the outer for (row). Console.WriteLine(); goes after the inner loop's }, still inside the outer loop. Did you remove every // ?",
 "A12": "the code has 2 bugs. Trace the failing call on paper. Look at the start value of the box, then at the loop test (< or <=).",
 "D07": "the code has 2 bugs. Trace DigitSum(123) with a table. Which operator gives the last digit (%) and which removes it (/)? Does the loop run for 10?",
 "R06": "the code has 2 bugs. The last index is values.Length - 1. And try [-5, -2, -9]: why is 0 a bad start value for max?",
}
for e in E:
    if e["id"] in CHECK: e["check_hint"] = CHECK[e["id"]]
for i, (name, r, ids) in enumerate(DRILLS):
    if r == "08": DRILLS[i] = (name, r, ids[:-1] + ["G14", "G03"] + ids[-1:])
