// Tests for L09 · Draw one row
// Exercise page: exercises/L09-draw-a-row.md
// Your code:     practice/L09_DrawARow.cs
// Run them:      ./ex check L09
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class L09_DrawARowTests
    {
        [Fact(DisplayName = "L09 example 1: DrawRow(5) prints \"*****\"")]
        public void Example1() => Expect.Prints("*****", () => L09_DrawARow.DrawRow(5));

        [Fact(DisplayName = "L09 example 2: DrawRow(1) prints \"*\"")]
        public void Example2() => Expect.Prints("*", () => L09_DrawARow.DrawRow(1));

        [Fact(DisplayName = "L09 example 3: DrawRow(0) prints nothing but a line break")]
        public void Example3() => Expect.Prints("", () => L09_DrawARow.DrawRow(0));
    }
}
