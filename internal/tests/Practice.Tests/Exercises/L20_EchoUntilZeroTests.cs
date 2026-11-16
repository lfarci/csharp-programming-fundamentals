// Tests for L20 · Echo until zero
// Exercise page: exercises/L20-echo-until-zero.md
// Your code:     practice/L20_EchoUntilZero.cs
// Run them:      ./ex check L20
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class L20_EchoUntilZeroTests
    {
        [Fact(DisplayName = "L20 example 1: input 5, 8, 0 prints \"Bye.\"")]
        public void Example1() => Expect.Output(
            input: ["5", "8", "0"],
            lines: ["You typed 5", "You typed 8", "Bye."],
            run: () => L20_EchoUntilZero.Run());

        [Fact(DisplayName = "L20 example 2: input -3, 0 prints \"Bye.\"")]
        public void Example2() => Expect.Output(
            input: ["-3", "0"],
            lines: ["You typed -3", "Bye."],
            run: () => L20_EchoUntilZero.Run());

        [Fact(DisplayName = "L20 example 3: input 0 prints \"Bye.\"")]
        public void Example3() => Expect.Output(
            input: ["0"],
            lines: ["Bye."],
            run: () => L20_EchoUntilZero.Run());
    }
}
