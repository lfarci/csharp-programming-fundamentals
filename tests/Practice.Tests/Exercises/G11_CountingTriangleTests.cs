// Tests for G11 · Counting triangle
// Exercise page: exercises/G11-counting-triangle.md
// Your code:     practice/G11_CountingTriangle.cs
// Run them:      ./ex check G11
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class G11_CountingTriangleTests
    {
        [Fact(DisplayName = "G11 example 1: DrawCountingTriangle(4) prints 4 lines")]
        public void Example1() => Expect.Prints(
            """
            1
            12
            123
            1234
            """, () => G11_CountingTriangle.DrawCountingTriangle(4));

        [Fact(DisplayName = "G11 example 2: DrawCountingTriangle(1) prints \"1\"")]
        public void Example2() => Expect.Prints("1", () => G11_CountingTriangle.DrawCountingTriangle(1));
    }
}
