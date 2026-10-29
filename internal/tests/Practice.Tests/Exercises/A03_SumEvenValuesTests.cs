// Tests for A03 · Sum of the even numbers
// Exercise page: exercises/A03-sum-even-values.md
// Your code:     practice/A03_SumEvenValues.cs
// Run them:      ./ex check A03
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class A03_SumEvenValuesTests
    {
        [Fact(DisplayName = "A03 example 1: SumOfEvens(6) returns 12")]
        public void Example1() => Expect.Returns(12, () => A03_SumEvenValues.SumOfEvens(6));

        [Fact(DisplayName = "A03 example 2: SumOfEvens(7) returns 12")]
        public void Example2() => Expect.Returns(12, () => A03_SumEvenValues.SumOfEvens(7));

        [Fact(DisplayName = "A03 example 3: SumOfEvens(1) returns 0")]
        public void Example3() => Expect.Returns(0, () => A03_SumEvenValues.SumOfEvens(1));

        [Fact(DisplayName = "A03 example 4: SumOfEvens(10) returns 30")]
        public void Example4() => Expect.Returns(30, () => A03_SumEvenValues.SumOfEvens(10));
    }
}
