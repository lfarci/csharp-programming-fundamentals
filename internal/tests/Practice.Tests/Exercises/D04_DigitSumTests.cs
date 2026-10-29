// Tests for D04 · Sum of the digits
// Exercise page: exercises/D04-digit-sum.md
// Your code:     practice/D04_DigitSum.cs
// Run them:      ./ex check D04
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class D04_DigitSumTests
    {
        [Fact(DisplayName = "D04 example 1: DigitSum(352) returns 10")]
        public void Example1() => Expect.Returns(10, () => D04_DigitSum.DigitSum(352));

        [Fact(DisplayName = "D04 example 2: DigitSum(0) returns 0")]
        public void Example2() => Expect.Returns(0, () => D04_DigitSum.DigitSum(0));

        [Fact(DisplayName = "D04 example 3: DigitSum(9999) returns 36")]
        public void Example3() => Expect.Returns(36, () => D04_DigitSum.DigitSum(9999));

        [Fact(DisplayName = "D04 example 4: DigitSum(7) returns 7")]
        public void Example4() => Expect.Returns(7, () => D04_DigitSum.DigitSum(7));
    }
}
