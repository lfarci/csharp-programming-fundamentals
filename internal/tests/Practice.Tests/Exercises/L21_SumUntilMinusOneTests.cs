// Tests for L21 · Sum until -1
// Exercise page: exercises/L21-sum-until-minus-one.md
// Your code:     practice/L21_SumUntilMinusOne.cs
// Run them:      ./ex check L21
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class L21_SumUntilMinusOneTests
    {
        [Fact(DisplayName = "L21 example 1: input 4, 7, 1, -1 prints \"Sum: 12\"")]
        public void Example1() => Expect.Output(
            input: ["4", "7", "1", "-1"],
            lines: ["Sum: 12"],
            run: () => L21_SumUntilMinusOne.Run());

        [Fact(DisplayName = "L21 example 2: input 10, 0, 5, -1 prints \"Sum: 15\"")]
        public void Example2() => Expect.Output(
            input: ["10", "0", "5", "-1"],
            lines: ["Sum: 15"],
            run: () => L21_SumUntilMinusOne.Run());

        [Fact(DisplayName = "L21 example 3: input -1 prints \"Sum: 0\"")]
        public void Example3() => Expect.Output(
            input: ["-1"],
            lines: ["Sum: 0"],
            run: () => L21_SumUntilMinusOne.Run());
    }
}
