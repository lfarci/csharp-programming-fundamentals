// Tests for A28 · Sum of i × (i + 1)
// Exercise page: exercises/A28-sum-of-pairs.md
// Your code:     practice/A28_SumOfPairs.cs
// Run them:      ./ex check A28
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class A28_SumOfPairsTests
    {
        [Fact(DisplayName = "A28 example 1: SumOfPairs(3) returns 20")]
        public void Example1() => Expect.Returns(20, () => A28_SumOfPairs.SumOfPairs(3));

        [Fact(DisplayName = "A28 example 2: SumOfPairs(1) returns 2")]
        public void Example2() => Expect.Returns(2, () => A28_SumOfPairs.SumOfPairs(1));

        [Fact(DisplayName = "A28 example 3: SumOfPairs(0) returns 0")]
        public void Example3() => Expect.Returns(0, () => A28_SumOfPairs.SumOfPairs(0));

        [Fact(DisplayName = "A28 example 4: SumOfPairs(4) returns 40")]
        public void Example4() => Expect.Returns(40, () => A28_SumOfPairs.SumOfPairs(4));
    }
}
