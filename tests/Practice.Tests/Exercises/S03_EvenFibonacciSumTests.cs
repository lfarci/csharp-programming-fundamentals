// Tests for S03 · Even Fibonacci sum
// Exercise page: exercises/S03-even-fibonacci-sum.md
// Your code:     practice/S03_EvenFibonacciSum.cs
// Run them:      ./ex check S03
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class S03_EvenFibonacciSumTests
    {
        [Fact(DisplayName = "S03 example 1: EvenFibonacciSum(10) returns 10")]
        public void Example1() => Expect.Returns(10L, () => S03_EvenFibonacciSum.EvenFibonacciSum(10L));

        [Fact(DisplayName = "S03 example 2: EvenFibonacciSum(100) returns 44")]
        public void Example2() => Expect.Returns(44L, () => S03_EvenFibonacciSum.EvenFibonacciSum(100L));

        [Fact(DisplayName = "S03 example 3: EvenFibonacciSum(1) returns 0")]
        public void Example3() => Expect.Returns(0L, () => S03_EvenFibonacciSum.EvenFibonacciSum(1L));

        [Fact(DisplayName = "S03 example 4: EvenFibonacciSum(34) returns 44")]
        public void Example4() => Expect.Returns(44L, () => S03_EvenFibonacciSum.EvenFibonacciSum(34L));
    }
}
