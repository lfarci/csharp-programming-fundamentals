// Tests for A17 · Sum the multiples of k
// Exercise page: exercises/A17-sum-multiples-of-k.md
// Your code:     practice/A17_SumMultiplesOfK.cs
// Run them:      ./ex check A17
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class A17_SumMultiplesOfKTests
    {
        [Fact(DisplayName = "A17 example 1: SumMultiplesOf(3, 10) returns 18")]
        public void Example1() => Expect.Returns(18, () => A17_SumMultiplesOfK.SumMultiplesOf(3, 10));

        [Fact(DisplayName = "A17 example 2: SumMultiplesOf(5, 20) returns 50")]
        public void Example2() => Expect.Returns(50, () => A17_SumMultiplesOfK.SumMultiplesOf(5, 20));

        [Fact(DisplayName = "A17 example 3: SumMultiplesOf(4, 3) returns 0")]
        public void Example3() => Expect.Returns(0, () => A17_SumMultiplesOfK.SumMultiplesOf(4, 3));
    }
}
