// Tests for A22 · Sum of the divisors
// Exercise page: exercises/A22-sum-of-divisors.md
// Your code:     practice/A22_SumOfDivisors.cs
// Run them:      ./ex check A22
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class A22_SumOfDivisorsTests
    {
        [Fact(DisplayName = "A22 example 1: SumOfDivisors(6) returns 12")]
        public void Example1() => Expect.Returns(12, () => A22_SumOfDivisors.SumOfDivisors(6));

        [Fact(DisplayName = "A22 example 2: SumOfDivisors(7) returns 8")]
        public void Example2() => Expect.Returns(8, () => A22_SumOfDivisors.SumOfDivisors(7));

        [Fact(DisplayName = "A22 example 3: SumOfDivisors(1) returns 1")]
        public void Example3() => Expect.Returns(1, () => A22_SumOfDivisors.SumOfDivisors(1));
    }
}
