// Tests for G03 · Multiplication grid
// Exercise page: exercises/G03-multiplication-grid.md
// Your code:     practice/G03_MultiplicationGrid.cs
// Run them:      ./ex check G03
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class G03_MultiplicationGridTests
    {
        [Fact(DisplayName = "G03 example 1: DrawGrid(4) prints 4 lines")]
        public void Example1() => Expect.Prints(
            """
               1   2   3   4
               2   4   6   8
               3   6   9  12
               4   8  12  16
            """, () => G03_MultiplicationGrid.DrawGrid(4));

        [Fact(DisplayName = "G03 example 2: DrawGrid(1) prints \"   1\"")]
        public void Example2() => Expect.Prints("   1", () => G03_MultiplicationGrid.DrawGrid(1));
    }
}
