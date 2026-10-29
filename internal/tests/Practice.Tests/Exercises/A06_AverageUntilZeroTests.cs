// Tests for A06 · Average until zero
// Exercise page: exercises/A06-average-until-zero.md
// Your code:     practice/A06_AverageUntilZero.cs
// Run them:      ./ex check A06
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class A06_AverageUntilZeroTests
    {
        [Fact(DisplayName = "A06 example 1: input 4, 7, 1, 0 prints \"Average: 4\"")]
        public void Example1() => Expect.Output(
            input: ["4", "7", "1", "0"],
            lines: ["Average: 4"],
            run: () => A06_AverageUntilZero.Run());

        [Fact(DisplayName = "A06 example 2: input 1, 2, 0 prints \"Average: 1.5\"")]
        public void Example2() => Expect.Output(
            input: ["1", "2", "0"],
            lines: ["Average: 1.5"],
            run: () => A06_AverageUntilZero.Run());

        [Fact(DisplayName = "A06 example 3: input 0 prints \"No numbers.\"")]
        public void Example3() => Expect.Output(
            input: ["0"],
            lines: ["No numbers."],
            run: () => A06_AverageUntilZero.Run());
    }
}
