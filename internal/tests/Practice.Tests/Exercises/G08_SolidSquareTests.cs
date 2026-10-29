// Tests for G08 · Solid square
// Exercise page: exercises/G08-solid-square.md
// Your code:     practice/G08_SolidSquare.cs
// Run them:      ./ex check G08
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class G08_SolidSquareTests
    {
        [Fact(DisplayName = "G08 example 1: DrawSquare(3) prints 3 lines")]
        public void Example1() => Expect.Prints(
            """
            ***
            ***
            ***
            """, () => G08_SolidSquare.DrawSquare(3));

        [Fact(DisplayName = "G08 example 2: DrawSquare(1) prints \"*\"")]
        public void Example2() => Expect.Prints("*", () => G08_SolidSquare.DrawSquare(1));
    }
}
