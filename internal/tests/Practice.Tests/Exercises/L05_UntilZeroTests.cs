// Tests for L05 · Until zero
// Exercise page: exercises/L05-until-zero.md
// Your code:     practice/L05_UntilZero.cs
// Run them:      ./ex check L05
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class L05_UntilZeroTests
    {
        [Fact(DisplayName = "L05 example 1: input 5, -2, 8, 0 prints \"You entered 3 numbers.\"")]
        public void Example1() => Expect.Output(
            input: ["5", "-2", "8", "0"],
            lines: ["You entered 3 numbers."],
            run: () => L05_UntilZero.Run());

        [Fact(DisplayName = "L05 example 2: input 0 prints \"You entered 0 numbers.\"")]
        public void Example2() => Expect.Output(
            input: ["0"],
            lines: ["You entered 0 numbers."],
            run: () => L05_UntilZero.Run());
    }
}
