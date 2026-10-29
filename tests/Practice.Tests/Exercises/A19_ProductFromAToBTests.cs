// Tests for A19 · Product from a to b
// Exercise page: exercises/A19-product-from-a-to-b.md
// Your code:     practice/A19_ProductFromAToB.cs
// Run them:      ./ex check A19
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class A19_ProductFromAToBTests
    {
        [Fact(DisplayName = "A19 example 1: ProductFromTo(2, 4) returns 24")]
        public void Example1() => Expect.Returns(24L, () => A19_ProductFromAToB.ProductFromTo(2, 4));

        [Fact(DisplayName = "A19 example 2: ProductFromTo(3, 3) returns 3")]
        public void Example2() => Expect.Returns(3L, () => A19_ProductFromAToB.ProductFromTo(3, 3));

        [Fact(DisplayName = "A19 example 3: ProductFromTo(1, 5) returns 120")]
        public void Example3() => Expect.Returns(120L, () => A19_ProductFromAToB.ProductFromTo(1, 5));

        [Fact(DisplayName = "A19 example 4: ProductFromTo(5, 4) returns 1")]
        public void Example4() => Expect.Returns(1L, () => A19_ProductFromAToB.ProductFromTo(5, 4));
    }
}
