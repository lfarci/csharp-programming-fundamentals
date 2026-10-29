// Tests for G12 · Upside-down triangle
// Exercise page: exercises/G12-upside-down-triangle.md
// Your code:     practice/G12_UpsideDownTriangle.cs
// Run them:      ./ex check G12
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class G12_UpsideDownTriangleTests
    {
        [Fact(DisplayName = "G12 example 1: DrawUpsideDown(3) prints 3 lines")]
        public void Example1() => Expect.Prints(
            """
            ***
            **
            *
            """, () => G12_UpsideDownTriangle.DrawUpsideDown(3));

        [Fact(DisplayName = "G12 example 2: DrawUpsideDown(1) prints \"*\"")]
        public void Example2() => Expect.Prints("*", () => G12_UpsideDownTriangle.DrawUpsideDown(1));
    }
}
