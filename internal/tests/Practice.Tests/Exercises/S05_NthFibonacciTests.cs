// Tests for S05 · N-th Fibonacci
// Exercise page: exercises/S05-nth-fibonacci.md
// Your code:     practice/S05_NthFibonacci.cs
// Run them:      ./ex check S05
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class S05_NthFibonacciTests
    {
        [Fact(DisplayName = "S05 example 1: Fibonacci(0) returns 0")]
        public void Example1() => Expect.Returns(0L, () => S05_NthFibonacci.Fibonacci(0));

        [Fact(DisplayName = "S05 example 2: Fibonacci(1) returns 1")]
        public void Example2() => Expect.Returns(1L, () => S05_NthFibonacci.Fibonacci(1));

        [Fact(DisplayName = "S05 example 3: Fibonacci(6) returns 8")]
        public void Example3() => Expect.Returns(8L, () => S05_NthFibonacci.Fibonacci(6));

        [Fact(DisplayName = "S05 example 4: Fibonacci(10) returns 55")]
        public void Example4() => Expect.Returns(55L, () => S05_NthFibonacci.Fibonacci(10));
    }
}
