// Tests for D12 · Product of the digits
// Exercise page: exercises/D12-product-of-digits.md
// Your code:     practice/D12_ProductOfDigits.cs
// Run them:      ./ex check D12
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class D12_ProductOfDigitsTests
    {
        [Fact(DisplayName = "D12 example 1: ProductOfDigits(234) returns 24")]
        public void Example1() => Expect.Returns(24, () => D12_ProductOfDigits.ProductOfDigits(234));

        [Fact(DisplayName = "D12 example 2: ProductOfDigits(5) returns 5")]
        public void Example2() => Expect.Returns(5, () => D12_ProductOfDigits.ProductOfDigits(5));

        [Fact(DisplayName = "D12 example 3: ProductOfDigits(105) returns 0")]
        public void Example3() => Expect.Returns(0, () => D12_ProductOfDigits.ProductOfDigits(105));

        [Fact(DisplayName = "D12 example 4: ProductOfDigits(1111) returns 1")]
        public void Example4() => Expect.Returns(1, () => D12_ProductOfDigits.ProductOfDigits(1111));
    }
}
