// Tests for R01 · Sum of an array
// Exercise page: exercises/R01-sum-an-array.md
// Your code:     practice/R01_SumAnArray.cs
// Run them:      ./ex check R01
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class R01_SumAnArrayTests
    {
        [Fact(DisplayName = "R01 example 1: Sum([4, 9, 2]) returns 15")]
        public void Example1() => Expect.Returns(15, () => R01_SumAnArray.Sum(new[] { 4, 9, 2 }));

        [Fact(DisplayName = "R01 example 2: Sum([-5]) returns -5")]
        public void Example2() => Expect.Returns(-5, () => R01_SumAnArray.Sum(new[] { -5 }));

        [Fact(DisplayName = "R01 example 3: Sum([]) returns 0")]
        public void Example3() => Expect.Returns(0, () => R01_SumAnArray.Sum(new int[0]));
    }
}
