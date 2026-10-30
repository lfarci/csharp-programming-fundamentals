// Tests for L12 · Count down
// Exercise page: exercises/L12-count-down.md
// Your code:     practice/L12_CountDown.cs
// Run them:      ./ex check L12
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class L12_CountDownTests
    {
        [Fact(DisplayName = "L12 example 1: CountDown(4) prints 4 lines")]
        public void Example1() => Expect.Prints(
            """
            4
            3
            2
            1
            """, () => L12_CountDown.CountDown(4));

        [Fact(DisplayName = "L12 example 2: CountDown(1) prints \"1\"")]
        public void Example2() => Expect.Prints("1", () => L12_CountDown.CountDown(1));

        [Fact(DisplayName = "L12 example 3: edge case, CountDown(0) prints nothing")]
        public void Edge1() => Expect.Prints("", () => L12_CountDown.CountDown(0), hint: "CountDown(0): the loop must not run at all. Is your test i >= 1 (or i > 0)?");
    }
}
