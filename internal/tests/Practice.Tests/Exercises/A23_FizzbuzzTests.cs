// Tests for A23 · FizzBuzz
// Exercise page: exercises/A23-fizzbuzz.md
// Your code:     practice/A23_Fizzbuzz.cs
// Run them:      ./ex check A23
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class A23_FizzbuzzTests
    {
        [Fact(DisplayName = "A23 example 1: PrintFizzBuzz(5) prints 5 lines")]
        public void Example1() => Expect.Prints(
            """
            1
            2
            Fizz
            4
            Buzz
            """, () => A23_Fizzbuzz.PrintFizzBuzz(5));

        [Fact(DisplayName = "A23 example 2: PrintFizzBuzz(15) prints 15 lines")]
        public void Example2() => Expect.Prints(
            """
            1
            2
            Fizz
            4
            Buzz
            Fizz
            7
            8
            Fizz
            Buzz
            11
            Fizz
            13
            14
            FizzBuzz
            """, () => A23_Fizzbuzz.PrintFizzBuzz(15));
    }
}
