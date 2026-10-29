// Tests for G04 · Hollow rectangle
// Exercise page: exercises/G04-hollow-rectangle.md
// Your code:     practice/G04_HollowRectangle.cs
// Run them:      ./ex check G04
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class G04_HollowRectangleTests
    {
        [Fact(DisplayName = "G04 example 1: DrawHollowRectangle(5, 4) prints 4 lines")]
        public void Example1() => Expect.Prints(
            """
            *****
            *   *
            *   *
            *****
            """, () => G04_HollowRectangle.DrawHollowRectangle(5, 4));

        [Fact(DisplayName = "G04 example 2: DrawHollowRectangle(3, 3) prints 3 lines")]
        public void Example2() => Expect.Prints(
            """
            ***
            * *
            ***
            """, () => G04_HollowRectangle.DrawHollowRectangle(3, 3));
    }
}
