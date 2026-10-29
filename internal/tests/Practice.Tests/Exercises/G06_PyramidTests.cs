// Tests for G06 · Pyramid
// Exercise page: exercises/G06-pyramid.md
// Your code:     practice/G06_Pyramid.cs
// Run them:      ./ex check G06
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class G06_PyramidTests
    {
        [Fact(DisplayName = "G06 example 1: DrawPyramid(3) prints 3 lines")]
        public void Example1() => Expect.Prints(
            """
              *
             ***
            *****
            """, () => G06_Pyramid.DrawPyramid(3));

        [Fact(DisplayName = "G06 example 2: DrawPyramid(1) prints \"*\"")]
        public void Example2() => Expect.Prints("*", () => G06_Pyramid.DrawPyramid(1));
    }
}
