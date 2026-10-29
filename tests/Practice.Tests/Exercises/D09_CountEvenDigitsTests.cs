// Tests for D09 · Count the even digits
// Exercise page: exercises/D09-count-even-digits.md
// Your code:     practice/D09_CountEvenDigits.cs
// Run them:      ./ex check D09
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class D09_CountEvenDigitsTests
    {
        [Fact(DisplayName = "D09 example 1: CountEvenDigits(2468) returns 4")]
        public void Example1() => Expect.Returns(4, () => D09_CountEvenDigits.CountEvenDigits(2468));

        [Fact(DisplayName = "D09 example 2: CountEvenDigits(135) returns 0")]
        public void Example2() => Expect.Returns(0, () => D09_CountEvenDigits.CountEvenDigits(135));

        [Fact(DisplayName = "D09 example 3: CountEvenDigits(1234) returns 2")]
        public void Example3() => Expect.Returns(2, () => D09_CountEvenDigits.CountEvenDigits(1234));
    }
}
