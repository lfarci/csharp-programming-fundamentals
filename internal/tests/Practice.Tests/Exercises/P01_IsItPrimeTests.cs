// Tests for P01 · Is it prime?
// Exercise page: exercises/P01-is-it-prime.md
// Your code:     practice/P01_IsItPrime.cs
// Run them:      ./ex check P01
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class P01_IsItPrimeTests
    {
        [Fact(DisplayName = "P01 example 1: IsPrime(7) returns true")]
        public void Example1() => Expect.Returns(true, () => P01_IsItPrime.IsPrime(7));

        [Fact(DisplayName = "P01 example 2: IsPrime(9) returns false")]
        public void Example2() => Expect.Returns(false, () => P01_IsItPrime.IsPrime(9));

        [Fact(DisplayName = "P01 example 3: IsPrime(1) returns false")]
        public void Example3() => Expect.Returns(false, () => P01_IsItPrime.IsPrime(1));

        [Fact(DisplayName = "P01 example 4: IsPrime(2) returns true")]
        public void Example4() => Expect.Returns(true, () => P01_IsItPrime.IsPrime(2));

        [Fact(DisplayName = "P01 example 5: IsPrime(97) returns true")]
        public void Example5() => Expect.Returns(true, () => P01_IsItPrime.IsPrime(97));

        [Fact(DisplayName = "P01 example 6: IsPrime(0) returns false")]
        public void Example6() => Expect.Returns(false, () => P01_IsItPrime.IsPrime(0));

        [Fact(DisplayName = "P01 example 7: edge case, IsPrime(25) returns false")]
        public void Edge1() => Expect.Returns(false, () => P01_IsItPrime.IsPrime(25), hint: "25 = 5 x 5: test the divisor 5 too (i * i <= n, not i * i < n).");

        [Fact(DisplayName = "P01 example 8: edge case, IsPrime(4) returns false")]
        public void Edge2() => Expect.Returns(false, () => P01_IsItPrime.IsPrime(4), hint: "4 = 2 x 2: the smallest even number that is not prime.");
    }
}
