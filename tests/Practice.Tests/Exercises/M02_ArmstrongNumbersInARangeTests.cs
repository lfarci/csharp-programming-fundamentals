// Tests for M02 · All Armstrong numbers in a range
// Exercise page: exercises/M02-armstrong-numbers-in-a-range.md
// Your code:     practice/M02_ArmstrongNumbersInARange.cs
// Run them:      ./ex check M02
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class M02_ArmstrongNumbersInARangeTests
    {
        [Fact(DisplayName = "M02 example 1: input 100, 999 prints \"153 370 371 407\"")]
        public void Example1() => Expect.Output(
            input: ["100", "999"],
            lines: ["153 370 371 407"],
            run: () => M02_ArmstrongNumbersInARange.Run());

        [Fact(DisplayName = "M02 example 2: input 1, 9 prints \"1 2 3 4 5 6 7 8 9\"")]
        public void Example2() => Expect.Output(
            input: ["1", "9"],
            lines: ["1 2 3 4 5 6 7 8 9"],
            run: () => M02_ArmstrongNumbersInARange.Run());

        [Fact(DisplayName = "M02 example 3: input 1000, 9999 prints \"1634 8208 9474\"")]
        public void Example3() => Expect.Output(
            input: ["1000", "9999"],
            lines: ["1634 8208 9474"],
            run: () => M02_ArmstrongNumbersInARange.Run());
    }
}
