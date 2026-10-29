// Tests for D03 · Count the digits
// Exercise page: exercises/D03-count-digits.md
// Your code:     practice/D03_CountDigits.cs
// Run them:      ./ex check D03
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class D03_CountDigitsTests
    {
        [Fact(DisplayName = "D03 example 1: CountDigits(352) returns 3")]
        public void Example1() => Expect.Returns(3, () => D03_CountDigits.CountDigits(352));

        [Fact(DisplayName = "D03 example 2: CountDigits(0) returns 1")]
        public void Example2() => Expect.Returns(1, () => D03_CountDigits.CountDigits(0));

        [Fact(DisplayName = "D03 example 3: CountDigits(1000) returns 4")]
        public void Example3() => Expect.Returns(4, () => D03_CountDigits.CountDigits(1000));

        [Fact(DisplayName = "D03 example 4: CountDigits(7) returns 1")]
        public void Example4() => Expect.Returns(1, () => D03_CountDigits.CountDigits(7));
    }
}
