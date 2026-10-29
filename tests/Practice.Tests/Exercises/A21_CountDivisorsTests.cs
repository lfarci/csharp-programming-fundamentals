// Tests for A21 · Count the divisors
// Exercise page: exercises/A21-count-divisors.md
// Your code:     practice/A21_CountDivisors.cs
// Run them:      ./ex check A21
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class A21_CountDivisorsTests
    {
        [Fact(DisplayName = "A21 example 1: CountDivisors(6) returns 4")]
        public void Example1() => Expect.Returns(4, () => A21_CountDivisors.CountDivisors(6));

        [Fact(DisplayName = "A21 example 2: CountDivisors(7) returns 2")]
        public void Example2() => Expect.Returns(2, () => A21_CountDivisors.CountDivisors(7));

        [Fact(DisplayName = "A21 example 3: CountDivisors(1) returns 1")]
        public void Example3() => Expect.Returns(1, () => A21_CountDivisors.CountDivisors(1));

        [Fact(DisplayName = "A21 example 4: CountDivisors(12) returns 6")]
        public void Example4() => Expect.Returns(6, () => A21_CountDivisors.CountDivisors(12));
    }
}
