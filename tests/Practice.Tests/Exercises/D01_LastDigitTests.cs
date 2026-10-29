// Tests for D01 · Last digit
// Exercise page: exercises/D01-last-digit.md
// Your code:     practice/D01_LastDigit.cs
// Run them:      ./ex check D01
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class D01_LastDigitTests
    {
        [Fact(DisplayName = "D01 example 1: LastDigit(352) returns 2")]
        public void Example1() => Expect.Returns(2, () => D01_LastDigit.LastDigit(352));

        [Fact(DisplayName = "D01 example 2: LastDigit(7) returns 7")]
        public void Example2() => Expect.Returns(7, () => D01_LastDigit.LastDigit(7));

        [Fact(DisplayName = "D01 example 3: LastDigit(0) returns 0")]
        public void Example3() => Expect.Returns(0, () => D01_LastDigit.LastDigit(0));

        [Fact(DisplayName = "D01 example 4: LastDigit(90) returns 0")]
        public void Example4() => Expect.Returns(0, () => D01_LastDigit.LastDigit(90));
    }
}
