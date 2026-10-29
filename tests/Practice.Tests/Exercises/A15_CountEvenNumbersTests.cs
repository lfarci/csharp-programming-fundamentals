// Tests for A15 · Count the even numbers
// Exercise page: exercises/A15-count-even-numbers.md
// Your code:     practice/A15_CountEvenNumbers.cs
// Run them:      ./ex check A15
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class A15_CountEvenNumbersTests
    {
        [Fact(DisplayName = "A15 example 1: CountEvens(10) returns 5")]
        public void Example1() => Expect.Returns(5, () => A15_CountEvenNumbers.CountEvens(10));

        [Fact(DisplayName = "A15 example 2: CountEvens(7) returns 3")]
        public void Example2() => Expect.Returns(3, () => A15_CountEvenNumbers.CountEvens(7));

        [Fact(DisplayName = "A15 example 3: CountEvens(1) returns 0")]
        public void Example3() => Expect.Returns(0, () => A15_CountEvenNumbers.CountEvens(1));
    }
}
