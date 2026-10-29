"""Exercises added by the 2026-10 review: flag/search drills before the prime check, and the first
Methods and Errors exercises. Same rules as data7.py: one new difficulty, near copies of a neighbour."""
from data4 import ex
from data5 import M, GOALS
import data7  # noqa: F401  (drill() and the drill bank must exist first)
from data7 import drill

S = "loops"
def flag(id_, slug, title, sig, body, cases, goal, hints, edge, mastery, pre, recipes=["05"], **k):
    drill(id_, slug, title, sig, body, cases, goal, hints, edge, mastery, S, recipes, pre, **k)

flag("P03", "has-a-multiple-of-7", "Has a multiple of 7", "bool HasMultipleOf7(int a, int b)",
"""bool found = false;
for (int i = a; i <= b; i++)
{
    if (i % 7 == 0)
    {
        found = true;
    }
}
return found;""", [([1, 6], False), ([1, 7], True), ([10, 20], True), ([15, 20], False)],
 "Give back `true` if at least one number from `a` to `b` is divisible by 7.",
 ["A flag box: `bool found = false;` before the loop. It means: not found yet.",
  "Inside the loop: `if (i % 7 == 0) found = true;`. After the loop: `return found;`."],
 ["`a` bigger than `b`: no number, so `false`."], "Give back `true` if at least one number from `a` to `b` is divisible by `k`.", ["A16"])
flag("P04", "has-an-even-digit", "Has an even digit", "bool HasEvenDigit(int n)",
"""bool found = false;
while (n > 0)
{
    if (n % 10 % 2 == 0)
    {
        found = true;
    }
    n /= 10;
}
return found;""", [([135], False), ([1352], True), ([8], True), ([7], False)],
 "Give back `true` if at least one digit of n is even (n > 0).",
 ["P03 with the digit loop of D09: `while (n > 0)`, the digit is `n % 10`, then `n /= 10;`.",
  "`found = true;` when the digit is even."],
 ["One digit: look at that digit only."], "Give back `true` if n has the digit 7.", ["P03", "D09"], recipes=["05", "06"])
flag("P07", "all-digits-odd", "All digits odd", "bool AllDigitsOdd(int n)",
"""bool allOdd = true;
while (n > 0)
{
    if (n % 10 % 2 == 0)
    {
        allOdd = false;
    }
    n /= 10;
}
return allOdd;""", [([1357], True), ([1352], False), ([7], True), ([20], False)],
 "Give back `true` if every digit of n is odd (n > 0).",
 ["The other way round: start with `bool allOdd = true;` (no even digit seen yet).",
  "One even digit is enough to make it `false`."],
 ["One even digit anywhere: `false`."], "Give back `true` if every digit of n is smaller than 5.", ["P04"], recipes=["05", "06"])
flag("P05", "first-multiple", "First multiple", "int FirstMultiple(int a, int b, int k)",
"""int position = -1;
for (int i = a; i <= b; i++)
{
    if (i % k == 0)
    {
        position = i;
        break;
    }
}
return position;""", [([10, 20, 7], 14), ([1, 5, 6], -1), ([6, 9, 3], 6), ([1, 30, 10], 10)],
 "Give back the first number from `a` to `b` that is divisible by `k` (k ≥ 1), or -1 if there is none.",
 ["The box starts at -1: it means not found.", "When you find one, keep it and stop the loop with `break;`."],
 ["None found: -1."], "Give back the **last** number from `a` to `b` divisible by `k` (loop backwards).", ["P03"])
flag("P06", "smallest-divisor", "Smallest divisor", "int SmallestDivisor(int n)",
"""int divisor = n;
for (int d = 2; d < n; d++)
{
    if (n % d == 0)
    {
        divisor = d;
        break;
    }
}
return divisor;""", [([15], 3), ([7], 7), ([2], 2), ([49], 7)],
 "Give back the smallest number bigger than 1 that divides n exactly (n ≥ 2).",
 ["P05 with `d` from 2 and the test `n % d == 0`.", "If no `d` below n works, the answer is n itself: start the box at n."],
 ["n is prime: the answer is n."], "Give back the largest divisor of n that is smaller than n.", ["P05", "A21"])

# ---------- Methods and Errors ----------
ex(id="N02", slug="is-multiple-and-count", title="A method that calls one", level="Guided", stars=1, recipes=["03"], pre=["A16"],
   goal="", examples=[], edge=["`k` bigger than n: 0."], constraints=["`CountMultiples` must call `IsMultiple`."],
   hints=["`IsMultiple` is one line: `return n % k == 0;`.",
          "`CountMultiples` is A16 with the test replaced by a call: `if (IsMultiple(i, k)) count++;`."],
   mastery="Write `IsEven(int n)` and use it in `SumOfEvens(int n)`.", code="")
M["N02"] = dict(run="", methods=[
    ("public static bool IsMultiple(int n, int k)", "return n % k == 0;", "return false;"),
    ("public static int CountMultiples(int n, int k)", '''int count = 0;
for (int i = 1; i <= n; i++)
{
    if (IsMultiple(i, k))
    {
        count++;
    }
}
return count;''', "return 0;")],
    cases=[("IsMultiple", [12, 3], True), ("IsMultiple", [7, 2], False), ("CountMultiples", [20, 5], 4), ("CountMultiples", [10, 3], 3), ("CountMultiples", [4, 5], 0)])
GOALS["N02"] = "Write two small methods. `IsMultiple(n, k)` gives back `true` if n is divisible by k. `CountMultiples(n, k)` counts the numbers from 1 to n divisible by k, by calling `IsMultiple`."

ex(id="E02", slug="parse-or-zero", title="Parse or zero", level="Guided", stars=1, recipes=[], pre=["L07"],
   goal="", examples=[], edge=["Empty text: 0.", "A negative number like `-7` is a number."],
   constraints=["Use `int.TryParse`, not `int.Parse`."],
   hints=["`int.TryParse(text, out int number)` gives back `true` and fills `number` when the text is a number.",
          "`if (int.TryParse(text, out int number)) return number;` then `return 0;` after it."],
   mastery="Write `ParseOrDefault(string text, int fallback)` that gives back `fallback` instead of 0.", code="")
M["E02"] = dict(run="", methods=[("public static int ParseOrZero(string text)", '''if (int.TryParse(text, out int number))
{
    return number;
}
return 0;''', "return 0;")],
    cases=[("ParseOrZero", ["42"], 42), ("ParseOrZero", ["abc"], 0), ("ParseOrZero", [""], 0), ("ParseOrZero", ["-7"], -7)])
GOALS["E02"] = "Give back the number written in `text`, or 0 when `text` is not a whole number. It must never crash."
