// Tests for A32 · Product of odd numbers
// Exercise page: exercises/A32-product-of-odd-numbers.md
// Your code:     practice/A32_ProductOfOddNumbers.cs
// Run them:      ./ex check A32
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class A32_ProductOfOddNumbersTests
    {
        [Fact(DisplayName = "A32 example 1: ProductOfOdds(5) returns 15")]
        public void Example1() => Expect.Returns(15L, () => A32_ProductOfOddNumbers.ProductOfOdds(5));

        [Fact(DisplayName = "A32 example 2: ProductOfOdds(6) returns 15")]
        public void Example2() => Expect.Returns(15L, () => A32_ProductOfOddNumbers.ProductOfOdds(6));

        [Fact(DisplayName = "A32 example 3: ProductOfOdds(1) returns 1")]
        public void Example3() => Expect.Returns(1L, () => A32_ProductOfOddNumbers.ProductOfOdds(1));

        [Fact(DisplayName = "A32 example 4: ProductOfOdds(0) returns 1")]
        public void Example4() => Expect.Returns(1L, () => A32_ProductOfOddNumbers.ProductOfOdds(0));
    }
}
