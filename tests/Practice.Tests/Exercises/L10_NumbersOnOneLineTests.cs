// Tests for L10 · Numbers on one line
// Exercise page: exercises/L10-numbers-on-one-line.md
// Your code:     practice/L10_NumbersOnOneLine.cs
// Run them:      ./ex check L10
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class L10_NumbersOnOneLineTests
    {
        [Fact(DisplayName = "L10 example 1: PrintNumbers(4) prints \"1 2 3 4\"")]
        public void Example1() => Expect.Prints("1 2 3 4", () => L10_NumbersOnOneLine.PrintNumbers(4));

        [Fact(DisplayName = "L10 example 2: PrintNumbers(1) prints \"1\"")]
        public void Example2() => Expect.Prints("1", () => L10_NumbersOnOneLine.PrintNumbers(1));

        [Fact(DisplayName = "L10 example 3: PrintNumbers(0) prints nothing but a line break")]
        public void Example3() => Expect.Prints("", () => L10_NumbersOnOneLine.PrintNumbers(0));
    }
}
