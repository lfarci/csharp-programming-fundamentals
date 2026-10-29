// Tests for L03 · Count up and down
// Exercise page: exercises/L03-count-up-and-down.md
// Your code:     practice/L03_CountUpAndDown.cs
// Run them:      ./ex check L03
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class L03_CountUpAndDownTests
    {
        [Fact(DisplayName = "L03 example 1: input 4 prints \"4 3 2 1\"")]
        public void Example1() => Expect.Output(
            input: ["4"],
            lines: ["1 2 3 4", "4 3 2 1"],
            run: () => L03_CountUpAndDown.Run());

        [Fact(DisplayName = "L03 example 2: input 1 prints \"1\"")]
        public void Example2() => Expect.Output(
            input: ["1"],
            lines: ["1", "1"],
            run: () => L03_CountUpAndDown.Run());
    }
}
