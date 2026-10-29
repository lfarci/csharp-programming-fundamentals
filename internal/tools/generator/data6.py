"""Exercises added for the lesson-format update: ladder gaps, Parsons (arrange the lines) and debugging.

task="parsons": the starter holds the right lines, mixed up, as comments. She puts them in order.
task="debug":   the starter holds code that compiles but has bugs. She finds and fixes them.
sort=...:       where the exercise sits in the path (default: its ID). Lets a bridge exercise sit
                just before the family it prepares, e.g. L09 right before G01.
"""
from data4 import ex, E
from data5 import M, GOALS, lines

def same(*_): pass
NOTE_P = "//! "  # starter text after this marker is used as is (no TODO line added)

# ---------- ladder: conditions ----------
ex(id="C04", slug="grade-from-a-score", title="Grade from a score", level="Independent", stars=2, recipes=[], pre=["C03"],
   goal="", examples=[], edge=["Exactly 90, 80, 70 and 50: which grade? Test the borders.", "0 and 100."],
   constraints=["Use one `if` / `else if` / `else` chain. Test the biggest border first."],
   hints=["Write the borders on a number line first: 0 … 50 … 70 … 80 … 90 … 100.",
          "Start with `if (score >= 90) return \"A\";`. The next test only runs when the first one was false, so `else if (score >= 80)` already means 80 to 89.",
          "The last case (below 50) needs no test: a plain `else` or a final `return \"F\";`."],
   mastery="Write `Season(int month)`: 12, 1, 2 → `\"winter\"`, 3–5 → `\"spring\"`, 6–8 → `\"summer\"`, 9–11 → `\"autumn\"`.",
   code="")
M["C04"] = dict(run="", methods=[("public static string Grade(int score)", '''if (score >= 90)
{
    return "A";
}
else if (score >= 80)
{
    return "B";
}
else if (score >= 70)
{
    return "C";
}
else if (score >= 50)
{
    return "D";
}
else
{
    return "F";
}''', 'return "";')], cases=[("Grade",[95],"A"),("Grade",[90],"A"),("Grade",[89],"B"),("Grade",[80],"B"),("Grade",[75],"C"),("Grade",[50],"D"),("Grade",[49],"F"),("Grade",[0],"F")])
GOALS["C04"] = "Give back the grade for a score from 0 to 100: 90 or more → `\"A\"`, 80–89 → `\"B\"`, 70–79 → `\"C\"`, 50–69 → `\"D\"`, below 50 → `\"F\"`."

# ---------- ladder: one loop on one line, before nested loops ----------
ex(id="L09", slug="draw-a-row", title="Draw one row", level="Guided", stars=1, recipes=["01","08"], pre=["L03"],
   goal="", examples=[], edge=["`DrawRow(0)` prints only the line break."],
   constraints=["Use `Console.Write` inside the loop and **one** `Console.WriteLine()` after it."],
   hints=["`Console.Write(\"*\")` prints a star and stays on the same line. `Console.WriteLine()` ends the line.",
          "The loop runs `width` times. Where does the line break go: inside or after the loop?"],
   mastery="Write `DrawDashes(int width)` that prints `-*-*-` style rows: a dash at odd positions, a star at even ones.",
   code="")
M["L09"] = dict(run="", methods=[("public static void DrawRow(int width)", '''for (int col = 1; col <= width; col++)
{
    Console.Write("*");
}
Console.WriteLine();''', "")], cases=[("DrawRow",[5],lines("*****")),("DrawRow",[1],lines("*")),("DrawRow",[0],lines(""))])
GOALS["L09"] = "Print `width` stars **on one line**, then end the line. `DrawRow(5)` prints `*****`. This is the inside of every 2D drawing."

ex(id="L10", slug="numbers-on-one-line", title="Numbers on one line", level="Guided", stars=1, recipes=["01","08"], pre=["L09"],
   goal="", examples=[], edge=["`PrintNumbers(1)` prints just `1`: no space at the end.", "`PrintNumbers(0)` prints only the line break."],
   constraints=["No space after the last number. Use one `if` inside the loop."],
   hints=["Print the number with `Console.Write(i)`.",
          "A space goes **between** numbers: before every number except the first (`if (i > 1)`).",
          "After the loop, one `Console.WriteLine()`."],
   mastery="Print `n` down to 1 on one line, separated by `, ` (`3, 2, 1`).",
   code="")
M["L10"] = dict(run="", methods=[("public static void PrintNumbers(int n)", '''for (int i = 1; i <= n; i++)
{
    if (i > 1)
    {
        Console.Write(" ");
    }
    Console.Write(i);
}
Console.WriteLine();''', "")], cases=[("PrintNumbers",[4],lines("1 2 3 4")),("PrintNumbers",[1],lines("1")),("PrintNumbers",[0],lines(""))])
GOALS["L10"] = "Print the numbers 1 to n on one line, with one space between them, then end the line. `PrintNumbers(4)` prints `1 2 3 4`."

# ---------- Parsons: arrange the lines ----------
ex(id="A11", slug="arrange-sum-of-squares", title="Arrange: sum of squares", level="Guided", stars=1, recipes=["02"], pre=["L03"], task="parsons",
   goal="", examples=[], edge=["`SumOfSquares(0)` must give 0: does your order still work?"],
   constraints=["Use **every** line once. Do not add new lines; you only remove the `//` and change the order."],
   hints=["Which line must come before the loop? Which one after it?",
          "The `{` and `}` lines show what is inside the loop.",
          "Order: box, loop header, `{`, update, `}`, return."],
   mastery="On paper, mix up the 6 lines of A04 factorial and give them to a friend (or to yourself tomorrow) to arrange.",
   code="")
M["A11"] = dict(run="", methods=[("public static int SumOfSquares(int n)", '''int sum = 0;
for (int i = 1; i <= n; i++)
{
    sum += i * i;
}
return sum;''', NOTE_P + '''Put these lines in the right order, then remove the // in front of them.
// Delete the line "return -1;" at the end when you are done.
//
//     sum += i * i;
// return sum;
// {
// int sum = 0;
// }
// for (int i = 1; i <= n; i++)
return -1;''')], cases=[("SumOfSquares",[3],14),("SumOfSquares",[1],1),("SumOfSquares",[0],0),("SumOfSquares",[10],385)])
GOALS["A11"] = "Give back 1² + 2² + … + n². `SumOfSquares(3)` is 1 + 4 + 9 = 14. All the lines are given, mixed up: put them in order."

ex(id="G07", slug="arrange-a-square", title="Arrange: a square", level="Guided", stars=1, recipes=["08"], pre=["L09"], task="parsons",
   goal="", examples=[], edge=["`DrawSquare(1)` prints one `#`."],
   constraints=["Use every line once. You only remove the `//` and change the order."],
   hints=["Start from [L09 Draw one row](L09-draw-a-row.md): the inner loop is that row.",
          "The outer loop repeats the whole row `size` times.",
          "The `Console.WriteLine();` belongs to the outer loop, after the inner loop's `}`."],
   mastery="Without looking, write `DrawRectangle(width, height)` from G01 on paper.",
   code="")
M["G07"] = dict(run="", methods=[("public static void DrawSquare(int size)", '''for (int row = 1; row <= size; row++)
{
    for (int col = 1; col <= size; col++)
    {
        Console.Write("#");
    }
    Console.WriteLine();
}''', NOTE_P + '''Put these lines in the right order, then remove the // in front of them.
//
//     Console.WriteLine();
// for (int row = 1; row <= size; row++)
//     {
//         Console.Write("#");
// }
//     for (int col = 1; col <= size; col++)
// {
//     }''')], cases=[("DrawSquare",[3],lines("###","###","###")),("DrawSquare",[1],lines("#"))])
GOALS["G07"] = "Print a square of `#`, `size` wide and `size` high. All the lines are given, mixed up: put them in order."

# ---------- debugging: fix the bugs ----------
DEBUG_RULE = "The file already has code. It compiles, but it has bugs. Change as **little** as you can."
ex(id="A12", slug="fix-count-multiples-of-7", title="Fix: multiples of 7", level="Guided", stars=1, recipes=["03"], pre=["A02"], task="debug",
   goal="", examples=[], edge=["`CountMultiplesOf7(7)`: is 7 itself counted?"],
   constraints=[DEBUG_RULE, "There are **2** bugs."],
   hints=["Run `./ex check A12` first and read which example fails. Then trace `CountMultiplesOf7(7)` on paper.",
          "Look at the start value of the box. What should a count be before you have seen anything?",
          "Look at the loop test. Is n itself included?"],
   mastery="Explain each bug in one sentence, using the words *start value* and *boundary*.",
   code="")
M["A12"] = dict(run="", methods=[("public static int CountMultiplesOf7(int n)", '''int count = 0;
for (int i = 1; i <= n; i++)
{
    if (i % 7 == 0)
    {
        count++;
    }
}
return count;''', NOTE_P + '''This code has 2 bugs. Find them and fix them.
int count = 1;
for (int i = 1; i < n; i++)
{
    if (i % 7 == 0)
    {
        count++;
    }
}
return count;''')], cases=[("CountMultiplesOf7",[7],1),("CountMultiplesOf7",[20],2),("CountMultiplesOf7",[6],0),("CountMultiplesOf7",[21],3)])
GOALS["A12"] = "`CountMultiplesOf7(n)` should count the numbers from 1 to n (included) divisible by 7. The code is written, but it has 2 bugs. Fix them."

ex(id="D07", slug="fix-digit-sum", title="Fix: digit sum", level="Independent", stars=2, recipes=["06"], pre=["D04"], task="debug",
   goal="", examples=[], edge=["`DigitSum(10)`: the loop must still run for the 1.", "`DigitSum(0)` is 0."],
   constraints=[DEBUG_RULE, "There are **2** bugs."],
   hints=["Trace `DigitSum(123)` with a table: `n`, `n % 10`, `sum`.",
          "Which operator gives the **last digit**, and which one **removes** it?",
          "Trace `DigitSum(10)`: does the loop run at all?"],
   mastery="Write a trace table for `DigitSum(907)` with the fixed code.",
   code="")
M["D07"] = dict(run="", methods=[("public static int DigitSum(int n)", '''int sum = 0;
while (n > 0)
{
    sum += n % 10;
    n = n / 10;
}
return sum;''', NOTE_P + '''This code has 2 bugs. Find them and fix them.
int sum = 0;
while (n > 10)
{
    sum += n / 10;
    n = n % 10;
}
return sum;''')], cases=[("DigitSum",[123],6),("DigitSum",[10],1),("DigitSum",[7],7),("DigitSum",[0],0),("DigitSum",[9045],18)])
GOALS["D07"] = "`DigitSum(n)` should give back the sum of the digits of n (n ≥ 0). The code is written, but it has 2 bugs. Fix them."

ex(id="R06", slug="fix-largest-value", title="Fix: largest value", level="Independent", stars=2, recipes=["11","04"], pre=["R02"], task="debug",
   goal="", examples=[], edge=["All values negative.", "One value only."],
   constraints=[DEBUG_RULE, "There are **2** bugs. One makes the program crash."],
   hints=["Read the crash message from `./ex check R06`: *index outside the bounds* means the loop goes one step too far.",
          "The last index of an array is `values.Length - 1`.",
          "Try `[-5, -2, -9]` on paper. Why does a start value of 0 give a wrong answer?"],
   mastery="Explain why the best start value for a max is the first value of the array.",
   code="")
M["R06"] = dict(run="", methods=[("public static int Largest(int[] values)", '''int max = values[0];
for (int i = 1; i < values.Length; i++)
{
    if (values[i] > max)
    {
        max = values[i];
    }
}
return max;''', NOTE_P + '''This code has 2 bugs. Find them and fix them.
int max = 0;
for (int i = 0; i <= values.Length; i++)
{
    if (values[i] > max)
    {
        max = values[i];
    }
}
return max;''')], cases=[("Largest",[[3,7,2]],7),("Largest",[[-5,-2,-9]],-2),("Largest",[[4]],4),("Largest",[[1,2,9]],9)])
GOALS["R06"] = "`Largest(values)` should give back the largest value of the array (at least 1 value). The code is written, but it has 2 bugs. Fix them."

# bridges: the first drawing now builds on one row
for e in E:
    if e["id"] == "G01" and "L09" not in e["pre"]: e["pre"] = ["L09"]
