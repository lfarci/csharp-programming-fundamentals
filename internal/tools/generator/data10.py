"""Exercises added on 2026-10-30. All original text and code, written for this course and inspired by
classic, public-domain programming problems (no text or code copied from any book or site):
- A23 FizzBuzz: the classic counting game (folk children's game; widely used as a first loop exercise).
- A24 Perfect number: Euclid's perfect numbers (6 = 1 + 2 + 3), ancient mathematics.
- S06 Collatz steps: the Collatz "3n + 1" sequence (Lothar Collatz, 1937), a classic while-loop problem.
- S07 Greatest common divisor: Euclid's algorithm (Elements, Book VII), by repeated remainders.
- D13 Digital root: repeat the digit sum until one digit remains, a classic arithmetic puzzle.
- R07 Count the even values, R08 Is it sorted?: classic array traversal and flag problems.
Same rules as data7.py and data8.py: one new difficulty each, near a neighbour that prepares it.
"""
from data5 import lines
from data7 import drill

drill("A23", "fizzbuzz", "FizzBuzz", "void PrintFizzBuzz(int n)",
"""for (int i = 1; i <= n; i++)
{
    if (i % 15 == 0)
    {
        Console.WriteLine("FizzBuzz");
    }
    else if (i % 3 == 0)
    {
        Console.WriteLine("Fizz");
    }
    else if (i % 5 == 0)
    {
        Console.WriteLine("Buzz");
    }
    else
    {
        Console.WriteLine(i);
    }
}""", [([5], lines("1", "2", "Fizz", "4", "Buzz")),
       ([15], lines("1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"))],
 "Print the numbers from 1 to n, one per line. But print `Fizz` instead of a multiple of 3, `Buzz` instead of a multiple of 5, and `FizzBuzz` instead of a multiple of both.",
 ["One counter loop from 1 to n, with an `if` / `else if` chain inside.",
  "Test \"multiple of both\" (`i % 15 == 0`) **first**: if `i % 3 == 0` comes first, 15 prints `Fizz`."],
 ["n = 15: the last line is `FizzBuzz`, not `Fizz`.", "n = 0: nothing is printed."],
 "Add `Bazz` for multiples of 7 (and `FizzBazz`, `BuzzBazz`… for the combinations).", "loops", ["01", "03"], ["L11", "A02"], level="Independent", stars=2)

drill("A24", "perfect-number", "Perfect number", "bool IsPerfect(int n)",
"""int sum = 0;
for (int d = 1; d < n; d++)
{
    if (n % d == 0)
    {
        sum += d;
    }
}
return sum == n;""", [([6], True), ([28], True), ([12], False), ([1], False), ([496], True)],
 "A number is **perfect** when it equals the sum of its divisors smaller than itself: 6 = 1 + 2 + 3. Give back `true` if n is perfect (n ≥ 1).",
 ["This is A22 (sum of the divisors) with one change: stop **before** n (`d < n`).",
  "After the loop, compare: `return sum == n;`."],
 ["n = 1: there is no divisor smaller than 1, the sum is 0, so `false`."],
 "Print every perfect number up to 10 000 (there are 4).", "loops", ["03"], ["A22"], level="Independent", stars=2)

drill("S06", "collatz-steps", "Collatz steps", "int CollatzSteps(int n)",
"""int steps = 0;
while (n != 1)
{
    if (n % 2 == 0)
    {
        n = n / 2;
    }
    else
    {
        n = 3 * n + 1;
    }
    steps++;
}
return steps;""", [([1], 0), ([2], 1), ([6], 8), ([7], 16), ([27], 111)],
 "Start from n (n ≥ 1). If it is even, halve it; if it is odd, change it to 3 × n + 1. Repeat until you reach 1, and give back how many steps it took. 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1 is 8 steps.",
 ["You do not know how many turns: use `while (n != 1)`.",
  "Inside: change `n` (half or 3n + 1), then `steps++`."],
 ["n = 1: already 1, so 0 steps (the loop never runs)."],
 "Find the number below 100 that takes the most steps.", "loops", ["07"], ["S04", "C01"], level="Independent", stars=2)

drill("S07", "greatest-common-divisor", "Greatest common divisor", "int Gcd(int a, int b)",
"""while (b != 0)
{
    int rest = a % b;
    a = b;
    b = rest;
}
return a;""", [([12, 18], 6), ([18, 12], 6), ([7, 5], 1), ([10, 10], 10), ([9, 0], 9)],
 "Give back the greatest common divisor of a and b (a ≥ 1, b ≥ 0) with Euclid's method: while `b` is not 0, replace `(a, b)` by `(b, a % b)`. When `b` is 0, the answer is `a`.",
 ["Same idea as Fibonacci (S02): a temporary box keeps a value before you overwrite it.",
  "`int rest = a % b; a = b; b = rest;` in this order."],
 ["b = 0: the loop never runs, the answer is a."],
 "Write `Lcm(a, b)` = a / Gcd(a, b) × b.", "loops", ["07"], ["S02", "D01"], level="Independent", stars=2)

drill("D13", "digital-root", "Digital root", "int DigitalRoot(int n)",
"""while (n >= 10)
{
    int sum = 0;
    while (n > 0)
    {
        sum += n % 10;
        n /= 10;
    }
    n = sum;
}
return n;""", [([7], 7), ([38], 2), ([9875], 2), ([10], 1), ([999], 9)],
 "Add the digits of n (n ≥ 0), then add the digits of the result, and so on, until one digit remains. Give it back. 9875 → 29 → 11 → 2.",
 ["The inner loop is D04 (sum of the digits).",
  "The outer loop repeats while the number still has 2 digits or more: `while (n >= 10)`."],
 ["n already has one digit: give it back as it is."],
 "Count how many rounds it takes (the additive persistence: 9875 takes 3).", "loops", ["06"], ["D04"], level="Independent", stars=2)

drill("R07", "count-the-even-values", "Count the even values", "int CountEven(int[] values)",
"""int count = 0;
for (int i = 0; i < values.Length; i++)
{
    if (values[i] % 2 == 0)
    {
        count++;
    }
}
return count;""", [([[1, 2, 3, 4]], 2), ([[2, 4, 6]], 3), ([[1, 3]], 0), ([[]], 0), ([[-2, 0, 5]], 2)],
 "Give back how many values in the array are even.",
 ["A15 (count the even numbers) with `values[i]` instead of `i`.",
  "The loop goes from 0 to `values.Length - 1`: `i < values.Length`."],
 ["An empty array: 0.", "Negative even values and 0 are even too."],
 "Give back the sum of the odd values as well.", "arrays", ["11", "03"], ["R01", "A15"], level="Independent", stars=2)

drill("R08", "is-it-sorted", "Is it sorted?", "bool IsSorted(int[] values)",
"""for (int i = 1; i < values.Length; i++)
{
    if (values[i] < values[i - 1])
    {
        return false;
    }
}
return true;""", [([[1, 2, 2, 5]], True), ([[3, 1, 2]], False), ([[1, 2, 4, 3]], False), ([[7]], True), ([[]], True)],
 "Give back `true` if every value is bigger than or equal to the one before it (smallest to largest).",
 ["Compare each value with the one before: start at `i = 1` and look at `values[i - 1]`.",
  "One pair in the wrong order is enough: `return false;` right away. After the loop: `return true;`."],
 ["0 or 1 value: nothing to compare, so `true`.", "Starting at `i = 0` reads `values[-1]` and crashes."],
 "Also accept arrays sorted from largest to smallest.", "arrays", ["11", "05"], ["R02", "P03"], level="Independent", stars=2)
