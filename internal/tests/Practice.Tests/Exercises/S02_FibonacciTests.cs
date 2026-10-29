// Tests for S02 · Fibonacci
// Exercise page: exercises/S02-fibonacci.md
// Your code:     practice/S02_Fibonacci.cs
// Run them:      ./ex check S02
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class S02_FibonacciTests
    {
        [Fact(DisplayName = "S02 example 1: input 6 prints \"0 1 1 2 3 5\"")]
        public void Example1() => Expect.Output(
            input: ["6"],
            lines: ["0 1 1 2 3 5"],
            run: () => S02_Fibonacci.Run());

        [Fact(DisplayName = "S02 example 2: input 1 prints \"0\"")]
        public void Example2() => Expect.Output(
            input: ["1"],
            lines: ["0"],
            run: () => S02_Fibonacci.Run());

        [Fact(DisplayName = "S02 example 3: input 10 prints \"0 1 1 2 3 5 8 13 21 34\"")]
        public void Example3() => Expect.Output(
            input: ["10"],
            lines: ["0 1 1 2 3 5 8 13 21 34"],
            run: () => S02_Fibonacci.Run());
    }
}
