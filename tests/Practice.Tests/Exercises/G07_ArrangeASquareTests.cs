// Tests for G07 · Arrange: a square
// Exercise page: exercises/G07-arrange-a-square.md
// Your code:     practice/G07_ArrangeASquare.cs
// Run them:      ./ex check G07
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class G07_ArrangeASquareTests
    {
        const string Hint = "every line is already in the file. The inner for (col) goes inside the outer for (row). Console.WriteLine(); goes after the inner loop's }, still inside the outer loop. Did you remove every // ?";

        [Fact(DisplayName = "G07 example 1: DrawSquare(3) prints 3 lines")]
        public void Example1() => Expect.Prints(
            """
            ###
            ###
            ###
            """, () => G07_ArrangeASquare.DrawSquare(3), hint: Hint);

        [Fact(DisplayName = "G07 example 2: DrawSquare(1) prints \"#\"")]
        public void Example2() => Expect.Prints("#", () => G07_ArrangeASquare.DrawSquare(1), hint: Hint);
    }
}
