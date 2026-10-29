// Tests for D10 · Count one digit
// Exercise page: exercises/D10-count-a-digit.md
// Your code:     practice/D10_CountADigit.cs
// Run them:      ./ex check D10
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class D10_CountADigitTests
    {
        [Fact(DisplayName = "D10 example 1: CountDigit(1717, 7) returns 2")]
        public void Example1() => Expect.Returns(2, () => D10_CountADigit.CountDigit(1717, 7));

        [Fact(DisplayName = "D10 example 2: CountDigit(123, 9) returns 0")]
        public void Example2() => Expect.Returns(0, () => D10_CountADigit.CountDigit(123, 9));

        [Fact(DisplayName = "D10 example 3: CountDigit(555, 5) returns 3")]
        public void Example3() => Expect.Returns(3, () => D10_CountADigit.CountDigit(555, 5));
    }
}
