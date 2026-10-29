// Tests for D07 · Fix: digit sum
// Exercise page: exercises/D07-fix-digit-sum.md
// Your code:     practice/D07_FixDigitSum.cs
// Run them:      ./ex check D07
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class D07_FixDigitSumTests
    {
        const string Hint = "the code has 2 bugs. Trace DigitSum(123) with a table. Which operator gives the last digit (%) and which removes it (/)? Does the loop run for 10?";

        [Fact(DisplayName = "D07 example 1: DigitSum(123) returns 6")]
        public void Example1() => Expect.Returns(6, () => D07_FixDigitSum.DigitSum(123), hint: Hint);

        [Fact(DisplayName = "D07 example 2: DigitSum(10) returns 1")]
        public void Example2() => Expect.Returns(1, () => D07_FixDigitSum.DigitSum(10), hint: Hint);

        [Fact(DisplayName = "D07 example 3: DigitSum(7) returns 7")]
        public void Example3() => Expect.Returns(7, () => D07_FixDigitSum.DigitSum(7), hint: Hint);

        [Fact(DisplayName = "D07 example 4: DigitSum(0) returns 0")]
        public void Example4() => Expect.Returns(0, () => D07_FixDigitSum.DigitSum(0), hint: Hint);

        [Fact(DisplayName = "D07 example 5: DigitSum(9045) returns 18")]
        public void Example5() => Expect.Returns(18, () => D07_FixDigitSum.DigitSum(9045), hint: Hint);
    }
}
