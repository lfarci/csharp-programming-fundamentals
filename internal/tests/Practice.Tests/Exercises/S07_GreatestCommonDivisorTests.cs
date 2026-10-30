// Tests for S07 · Greatest common divisor
// Exercise page: exercises/S07-greatest-common-divisor.md
// Your code:     practice/S07_GreatestCommonDivisor.cs
// Run them:      ./ex check S07
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class S07_GreatestCommonDivisorTests
    {
        [Fact(DisplayName = "S07 example 1: Gcd(12, 18) returns 6")]
        public void Example1() => Expect.Returns(6, () => S07_GreatestCommonDivisor.Gcd(12, 18));

        [Fact(DisplayName = "S07 example 2: Gcd(18, 12) returns 6")]
        public void Example2() => Expect.Returns(6, () => S07_GreatestCommonDivisor.Gcd(18, 12));

        [Fact(DisplayName = "S07 example 3: Gcd(7, 5) returns 1")]
        public void Example3() => Expect.Returns(1, () => S07_GreatestCommonDivisor.Gcd(7, 5));

        [Fact(DisplayName = "S07 example 4: Gcd(10, 10) returns 10")]
        public void Example4() => Expect.Returns(10, () => S07_GreatestCommonDivisor.Gcd(10, 10));

        [Fact(DisplayName = "S07 example 5: Gcd(9, 0) returns 9")]
        public void Example5() => Expect.Returns(9, () => S07_GreatestCommonDivisor.Gcd(9, 0));
    }
}
