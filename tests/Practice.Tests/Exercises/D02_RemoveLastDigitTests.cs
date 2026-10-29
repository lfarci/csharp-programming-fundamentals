// Tests for D02 · Remove the last digit
// Exercise page: exercises/D02-remove-last-digit.md
// Your code:     practice/D02_RemoveLastDigit.cs
// Run them:      ./ex check D02
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class D02_RemoveLastDigitTests
    {
        [Fact(DisplayName = "D02 example 1: RemoveLastDigit(352) returns 35")]
        public void Example1() => Expect.Returns(35, () => D02_RemoveLastDigit.RemoveLastDigit(352));

        [Fact(DisplayName = "D02 example 2: RemoveLastDigit(7) returns 0")]
        public void Example2() => Expect.Returns(0, () => D02_RemoveLastDigit.RemoveLastDigit(7));

        [Fact(DisplayName = "D02 example 3: RemoveLastDigit(0) returns 0")]
        public void Example3() => Expect.Returns(0, () => D02_RemoveLastDigit.RemoveLastDigit(0));

        [Fact(DisplayName = "D02 example 4: RemoveLastDigit(1000) returns 100")]
        public void Example4() => Expect.Returns(100, () => D02_RemoveLastDigit.RemoveLastDigit(1000));
    }
}
