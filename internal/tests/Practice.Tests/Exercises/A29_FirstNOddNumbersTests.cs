// Tests for A29 · First n odd numbers
// Exercise page: exercises/A29-first-n-odd-numbers.md
// Your code:     practice/A29_FirstNOddNumbers.cs
// Run them:      ./ex check A29
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class A29_FirstNOddNumbersTests
    {
        [Fact(DisplayName = "A29 example 1: SumFirstOdds(3) returns 9")]
        public void Example1() => Expect.Returns(9, () => A29_FirstNOddNumbers.SumFirstOdds(3));

        [Fact(DisplayName = "A29 example 2: SumFirstOdds(1) returns 1")]
        public void Example2() => Expect.Returns(1, () => A29_FirstNOddNumbers.SumFirstOdds(1));

        [Fact(DisplayName = "A29 example 3: SumFirstOdds(0) returns 0")]
        public void Example3() => Expect.Returns(0, () => A29_FirstNOddNumbers.SumFirstOdds(0));

        [Fact(DisplayName = "A29 example 4: SumFirstOdds(5) returns 25")]
        public void Example4() => Expect.Returns(25, () => A29_FirstNOddNumbers.SumFirstOdds(5));
    }
}
