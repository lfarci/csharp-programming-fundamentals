// Tests for G01 · Draw a rectangle
// Exercise page: exercises/G01-rectangle.md
// Your code:     practice/G01_Rectangle.cs
// Run them:      ./ex check G01
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class G01_RectangleTests
    {
        [Fact(DisplayName = "G01 example 1: DrawRectangle(4, 3) prints 3 lines")]
        public void Example1() => Expect.Prints(
            """
            ****
            ****
            ****
            """, () => G01_Rectangle.DrawRectangle(4, 3));

        [Fact(DisplayName = "G01 example 2: DrawRectangle(1, 2) prints 2 lines")]
        public void Example2() => Expect.Prints(
            """
            *
            *
            """, () => G01_Rectangle.DrawRectangle(1, 2));
    }
}
