// Tests for G10 · Triangle of row numbers
// Exercise page: exercises/G10-row-number-triangle.md
// Your code:     practice/G10_RowNumberTriangle.cs
// Run them:      ./ex check G10
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class G10_RowNumberTriangleTests
    {
        [Fact(DisplayName = "G10 example 1: DrawRowTriangle(3) prints 3 lines")]
        public void Example1() => Expect.Prints(
            """
            1
            22
            333
            """, () => G10_RowNumberTriangle.DrawRowTriangle(3));

        [Fact(DisplayName = "G10 example 2: DrawRowTriangle(1) prints \"1\"")]
        public void Example2() => Expect.Prints("1", () => G10_RowNumberTriangle.DrawRowTriangle(1));
    }
}
