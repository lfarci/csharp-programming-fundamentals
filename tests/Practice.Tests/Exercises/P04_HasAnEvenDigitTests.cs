// Tests for P04 · Has an even digit
// Exercise page: exercises/P04-has-an-even-digit.md
// Your code:     practice/P04_HasAnEvenDigit.cs
// Run them:      ./ex check P04
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class P04_HasAnEvenDigitTests
    {
        [Fact(DisplayName = "P04 example 1: HasEvenDigit(135) returns false")]
        public void Example1() => Expect.Returns(false, () => P04_HasAnEvenDigit.HasEvenDigit(135));

        [Fact(DisplayName = "P04 example 2: HasEvenDigit(1352) returns true")]
        public void Example2() => Expect.Returns(true, () => P04_HasAnEvenDigit.HasEvenDigit(1352));

        [Fact(DisplayName = "P04 example 3: HasEvenDigit(8) returns true")]
        public void Example3() => Expect.Returns(true, () => P04_HasAnEvenDigit.HasEvenDigit(8));

        [Fact(DisplayName = "P04 example 4: HasEvenDigit(7) returns false")]
        public void Example4() => Expect.Returns(false, () => P04_HasAnEvenDigit.HasEvenDigit(7));
    }
}
