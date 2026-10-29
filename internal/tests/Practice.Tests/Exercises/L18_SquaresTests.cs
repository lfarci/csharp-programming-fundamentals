// Tests for L18 · Square numbers
// Exercise page: exercises/L18-squares.md
// Your code:     practice/L18_Squares.cs
// Run them:      ./ex check L18
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class L18_SquaresTests
    {
        [Fact(DisplayName = "L18 example 1: PrintSquares(4) prints 4 lines")]
        public void Example1() => Expect.Prints(
            """
            1
            4
            9
            16
            """, () => L18_Squares.PrintSquares(4));

        [Fact(DisplayName = "L18 example 2: PrintSquares(1) prints \"1\"")]
        public void Example2() => Expect.Prints("1", () => L18_Squares.PrintSquares(1));
    }
}
