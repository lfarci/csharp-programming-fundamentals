// Tests for G02 · Draw a right triangle
// Exercise page: exercises/G02-right-triangle.md
// Your code:     practice/G02_RightTriangle.cs
// Run them:      ./ex check G02
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class G02_RightTriangleTests
    {
        [Fact(DisplayName = "G02 example 1: DrawTriangle(4) prints 4 lines")]
        public void Example1() => Expect.Prints(
            """
            *
            **
            ***
            ****
            """, () => G02_RightTriangle.DrawTriangle(4));

        [Fact(DisplayName = "G02 example 2: DrawTriangle(1) prints \"*\"")]
        public void Example2() => Expect.Prints("*", () => G02_RightTriangle.DrawTriangle(1));
    }
}
