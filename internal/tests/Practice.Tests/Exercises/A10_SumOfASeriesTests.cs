// Tests for A10 · Sum of a series
// Exercise page: exercises/A10-sum-of-a-series.md
// Your code:     practice/A10_SumOfASeries.cs
// Run them:      ./ex check A10
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class A10_SumOfASeriesTests
    {
        [Fact(DisplayName = "A10 example 1: SeriesSum(1) returns 1.0")]
        public void Example1() => Expect.Returns(1.0, () => A10_SumOfASeries.SeriesSum(1));

        [Fact(DisplayName = "A10 example 2: SeriesSum(2) returns 1.5")]
        public void Example2() => Expect.Returns(1.5, () => A10_SumOfASeries.SeriesSum(2));

        [Fact(DisplayName = "A10 example 3: SeriesSum(4) returns 2.0833333333")]
        public void Example3() => Expect.Returns(2.0833333333, () => A10_SumOfASeries.SeriesSum(4));
    }
}
