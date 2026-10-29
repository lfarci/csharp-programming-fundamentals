// Tests for G09 · Rows of numbers
// Exercise page: exercises/G09-number-rows.md
// Your code:     practice/G09_NumberRows.cs
// Run them:      ./ex check G09
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class G09_NumberRowsTests
    {
        [Fact(DisplayName = "G09 example 1: DrawNumberRows(4, 2) prints 2 lines")]
        public void Example1() => Expect.Prints(
            """
            1234
            1234
            """, () => G09_NumberRows.DrawNumberRows(4, 2));

        [Fact(DisplayName = "G09 example 2: DrawNumberRows(3, 3) prints 3 lines")]
        public void Example2() => Expect.Prints(
            """
            123
            123
            123
            """, () => G09_NumberRows.DrawNumberRows(3, 3));
    }
}
