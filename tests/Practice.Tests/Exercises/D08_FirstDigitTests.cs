// Tests for D08 · First digit
// Exercise page: exercises/D08-first-digit.md
// Your code:     practice/D08_FirstDigit.cs
// Run them:      ./ex check D08
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class D08_FirstDigitTests
    {
        [Fact(DisplayName = "D08 example 1: FirstDigit(352) returns 3")]
        public void Example1() => Expect.Returns(3, () => D08_FirstDigit.FirstDigit(352));

        [Fact(DisplayName = "D08 example 2: FirstDigit(7) returns 7")]
        public void Example2() => Expect.Returns(7, () => D08_FirstDigit.FirstDigit(7));

        [Fact(DisplayName = "D08 example 3: FirstDigit(1000) returns 1")]
        public void Example3() => Expect.Returns(1, () => D08_FirstDigit.FirstDigit(1000));

        [Fact(DisplayName = "D08 example 4: FirstDigit(90) returns 9")]
        public void Example4() => Expect.Returns(9, () => D08_FirstDigit.FirstDigit(90));
    }
}
