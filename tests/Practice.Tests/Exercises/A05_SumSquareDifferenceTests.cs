// Tests for A05 · Sum and sum of squares
// Exercise page: exercises/A05-sum-square-difference.md
// Your code:     practice/A05_SumSquareDifference.cs
// Run them:      ./ex check A05
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class A05_SumSquareDifferenceTests
    {
        [Fact(DisplayName = "A05 example 1: input 3 prints \"Difference: 22\"")]
        public void Example1() => Expect.Output(
            input: ["3"],
            lines: ["Sum: 6", "Sum of squares: 14", "Difference: 22"],
            run: () => A05_SumSquareDifference.Run());

        [Fact(DisplayName = "A05 example 2: input 10 prints \"Difference: 2640\"")]
        public void Example2() => Expect.Output(
            input: ["10"],
            lines: ["Sum: 55", "Sum of squares: 385", "Difference: 2640"],
            run: () => A05_SumSquareDifference.Run());
    }
}
