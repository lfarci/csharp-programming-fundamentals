// Tests for L04 · Multiplication table
// Exercise page: exercises/L04-multiplication-table.md
// Your code:     practice/L04_MultiplicationTable.cs
// Run them:      ./ex check L04
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class L04_MultiplicationTableTests
    {
        [Fact(DisplayName = "L04 example 1: input 3 prints \"3 x 10 = 30\"")]
        public void Example1() => Expect.Output(
            input: ["3"],
            lines: ["3 x 1 = 3", "3 x 2 = 6", "3 x 10 = 30"],
            run: () => L04_MultiplicationTable.Run());

        [Fact(DisplayName = "L04 example 2: input 7 prints \"7 x 7 = 49\"")]
        public void Example2() => Expect.Output(
            input: ["7"],
            lines: ["7 x 7 = 49"],
            run: () => L04_MultiplicationTable.Run());

        [Fact(DisplayName = "L04 example 3: edge case, input 0 prints \"0 x 10 = 0\"")]
        public void Edge1() => Expect.Output(
            input: ["0"],
            lines: ["0 x 1 = 0", "0 x 10 = 0"],
            run: () => L04_MultiplicationTable.Run(), hint: "N = 0 is allowed: the table still has 10 lines, all results are 0.");
    }
}
