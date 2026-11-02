// Tests for A26 · Sum of tens
// Exercise page: exercises/A26-sum-of-tens.md
// Your code:     practice/A26_SumOfTens.cs
// Run them:      ./ex check A26
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class A26_SumOfTensTests
    {
        [Fact(DisplayName = "A26 example 1: SumOfTens(3) returns 60")]
        public void Example1() => Expect.Returns(60, () => A26_SumOfTens.SumOfTens(3));

        [Fact(DisplayName = "A26 example 2: SumOfTens(1) returns 10")]
        public void Example2() => Expect.Returns(10, () => A26_SumOfTens.SumOfTens(1));

        [Fact(DisplayName = "A26 example 3: SumOfTens(0) returns 0")]
        public void Example3() => Expect.Returns(0, () => A26_SumOfTens.SumOfTens(0));

        [Fact(DisplayName = "A26 example 4: SumOfTens(5) returns 150")]
        public void Example4() => Expect.Returns(150, () => A26_SumOfTens.SumOfTens(5));
    }
}
