// Tests for G13 · Diagonal
// Exercise page: exercises/G13-diagonal.md
// Your code:     practice/G13_Diagonal.cs
// Run them:      ./ex check G13
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class G13_DiagonalTests
    {
        [Fact(DisplayName = "G13 example 1: DrawDiagonal(3) prints 3 lines")]
        public void Example1() => Expect.Prints(
            """
            *..
            .*.
            ..*
            """, () => G13_Diagonal.DrawDiagonal(3));

        [Fact(DisplayName = "G13 example 2: DrawDiagonal(1) prints \"*\"")]
        public void Example2() => Expect.Prints("*", () => G13_Diagonal.DrawDiagonal(1));
    }
}
