// Tests for A33 · Product of squares
// Exercise page: exercises/A33-product-of-squares.md
// Your code:     practice/A33_ProductOfSquares.cs
// Run them:      ./ex check A33
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class A33_ProductOfSquaresTests
    {
        [Fact(DisplayName = "A33 example 1: ProductOfSquares(3) returns 36")]
        public void Example1() => Expect.Returns(36L, () => A33_ProductOfSquares.ProductOfSquares(3));

        [Fact(DisplayName = "A33 example 2: ProductOfSquares(1) returns 1")]
        public void Example2() => Expect.Returns(1L, () => A33_ProductOfSquares.ProductOfSquares(1));

        [Fact(DisplayName = "A33 example 3: ProductOfSquares(0) returns 1")]
        public void Example3() => Expect.Returns(1L, () => A33_ProductOfSquares.ProductOfSquares(0));

        [Fact(DisplayName = "A33 example 4: ProductOfSquares(4) returns 576")]
        public void Example4() => Expect.Returns(576L, () => A33_ProductOfSquares.ProductOfSquares(4));
    }
}
