// Tests for R06 · Fix the bugs: largest value
// Exercise page: exercises/R06-fix-largest-value.md
// Your code:     practice/R06_FixLargestValue.cs
// Run them:      ./ex check R06
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class R06_FixLargestValueTests
    {
        const string Hint = "the code has 2 bugs. The last index is values.Length - 1. And try [-5, -2, -9]: why is 0 a bad start value for max?";

        [Fact(DisplayName = "R06 example 1: Largest([3, 7, 2]) returns 7")]
        public void Example1() => Expect.Returns(7, () => R06_FixLargestValue.Largest(new[] { 3, 7, 2 }), hint: Hint);

        [Fact(DisplayName = "R06 example 2: Largest([-5, -2, -9]) returns -2")]
        public void Example2() => Expect.Returns(-2, () => R06_FixLargestValue.Largest(new[] { -5, -2, -9 }), hint: Hint);

        [Fact(DisplayName = "R06 example 3: Largest([4]) returns 4")]
        public void Example3() => Expect.Returns(4, () => R06_FixLargestValue.Largest(new[] { 4 }), hint: Hint);

        [Fact(DisplayName = "R06 example 4: Largest([1, 2, 9]) returns 9")]
        public void Example4() => Expect.Returns(9, () => R06_FixLargestValue.Largest(new[] { 1, 2, 9 }), hint: Hint);
    }
}
