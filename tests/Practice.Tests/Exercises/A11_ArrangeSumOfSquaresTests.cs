// Tests for A11 · Arrange the lines: sum of squares
// Exercise page: exercises/A11-arrange-sum-of-squares.md
// Your code:     practice/A11_ArrangeSumOfSquares.cs
// Run them:      ./ex check A11
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class A11_ArrangeSumOfSquaresTests
    {
        const string Hint = "every line you need is already in the file. Check the order: the box line before the loop, the update between { and }, the return after the loop. Did you remove every // and the line return -1; ?";

        [Fact(DisplayName = "A11 example 1: SumOfSquares(3) returns 14")]
        public void Example1() => Expect.Returns(14, () => A11_ArrangeSumOfSquares.SumOfSquares(3), hint: Hint);

        [Fact(DisplayName = "A11 example 2: SumOfSquares(1) returns 1")]
        public void Example2() => Expect.Returns(1, () => A11_ArrangeSumOfSquares.SumOfSquares(1), hint: Hint);

        [Fact(DisplayName = "A11 example 3: SumOfSquares(0) returns 0")]
        public void Example3() => Expect.Returns(0, () => A11_ArrangeSumOfSquares.SumOfSquares(0), hint: Hint);

        [Fact(DisplayName = "A11 example 4: SumOfSquares(10) returns 385")]
        public void Example4() => Expect.Returns(385, () => A11_ArrangeSumOfSquares.SumOfSquares(10), hint: Hint);
    }
}
