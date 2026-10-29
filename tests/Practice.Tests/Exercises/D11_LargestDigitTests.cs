// Tests for D11 · Largest digit
// Exercise page: exercises/D11-largest-digit.md
// Your code:     practice/D11_LargestDigit.cs
// Run them:      ./ex check D11
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class D11_LargestDigitTests
    {
        [Fact(DisplayName = "D11 example 1: LargestDigit(3829) returns 9")]
        public void Example1() => Expect.Returns(9, () => D11_LargestDigit.LargestDigit(3829));

        [Fact(DisplayName = "D11 example 2: LargestDigit(111) returns 1")]
        public void Example2() => Expect.Returns(1, () => D11_LargestDigit.LargestDigit(111));

        [Fact(DisplayName = "D11 example 3: LargestDigit(5) returns 5")]
        public void Example3() => Expect.Returns(5, () => D11_LargestDigit.LargestDigit(5));

        [Fact(DisplayName = "D11 example 4: LargestDigit(2061) returns 6")]
        public void Example4() => Expect.Returns(6, () => D11_LargestDigit.LargestDigit(2061));
    }
}
