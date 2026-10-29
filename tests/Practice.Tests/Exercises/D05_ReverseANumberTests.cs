// Tests for D05 · Reverse a number
// Exercise page: exercises/D05-reverse-a-number.md
// Your code:     practice/D05_ReverseANumber.cs
// Run them:      ./ex check D05
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class D05_ReverseANumberTests
    {
        [Fact(DisplayName = "D05 example 1: ReverseNumber(352) returns 253")]
        public void Example1() => Expect.Returns(253, () => D05_ReverseANumber.ReverseNumber(352));

        [Fact(DisplayName = "D05 example 2: ReverseNumber(1200) returns 21")]
        public void Example2() => Expect.Returns(21, () => D05_ReverseANumber.ReverseNumber(1200));

        [Fact(DisplayName = "D05 example 3: ReverseNumber(0) returns 0")]
        public void Example3() => Expect.Returns(0, () => D05_ReverseANumber.ReverseNumber(0));

        [Fact(DisplayName = "D05 example 4: ReverseNumber(7) returns 7")]
        public void Example4() => Expect.Returns(7, () => D05_ReverseANumber.ReverseNumber(7));
    }
}
