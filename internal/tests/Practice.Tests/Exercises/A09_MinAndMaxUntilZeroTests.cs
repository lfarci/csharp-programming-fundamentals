// Tests for A09 · Min and max until zero
// Exercise page: exercises/A09-min-and-max-until-zero.md
// Your code:     practice/A09_MinAndMaxUntilZero.cs
// Run them:      ./ex check A09
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class A09_MinAndMaxUntilZeroTests
    {
        [Fact(DisplayName = "A09 example 1: input 4, -2, 9, 0 prints \"Max: 9\"")]
        public void Example1() => Expect.Output(
            input: ["4", "-2", "9", "0"],
            lines: ["Min: -2", "Max: 9"],
            run: () => A09_MinAndMaxUntilZero.Run());

        [Fact(DisplayName = "A09 example 2: input -5, -3, 0 prints \"Max: -3\"")]
        public void Example2() => Expect.Output(
            input: ["-5", "-3", "0"],
            lines: ["Min: -5", "Max: -3"],
            run: () => A09_MinAndMaxUntilZero.Run());

        [Fact(DisplayName = "A09 example 3: input 0 prints \"No numbers.\"")]
        public void Example3() => Expect.Output(
            input: ["0"],
            lines: ["No numbers."],
            run: () => A09_MinAndMaxUntilZero.Run());
    }
}
