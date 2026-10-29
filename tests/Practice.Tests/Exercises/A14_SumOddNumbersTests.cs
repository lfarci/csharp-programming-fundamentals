// Tests for A14 · Sum the odd numbers
// Exercise page: exercises/A14-sum-odd-numbers.md
// Your code:     practice/A14_SumOddNumbers.cs
// Run them:      ./ex check A14
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class A14_SumOddNumbersTests
    {
        [Fact(DisplayName = "A14 example 1: SumOfOdds(5) returns 9")]
        public void Example1() => Expect.Returns(9, () => A14_SumOddNumbers.SumOfOdds(5));

        [Fact(DisplayName = "A14 example 2: SumOfOdds(6) returns 9")]
        public void Example2() => Expect.Returns(9, () => A14_SumOddNumbers.SumOfOdds(6));

        [Fact(DisplayName = "A14 example 3: SumOfOdds(1) returns 1")]
        public void Example3() => Expect.Returns(1, () => A14_SumOddNumbers.SumOfOdds(1));

        [Fact(DisplayName = "A14 example 4: SumOfOdds(0) returns 0")]
        public void Example4() => Expect.Returns(0, () => A14_SumOddNumbers.SumOfOdds(0));
    }
}
