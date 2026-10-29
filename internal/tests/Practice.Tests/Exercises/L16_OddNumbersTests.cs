// Tests for L16 · Odd numbers
// Exercise page: exercises/L16-odd-numbers.md
// Your code:     practice/L16_OddNumbers.cs
// Run them:      ./ex check L16
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class L16_OddNumbersTests
    {
        [Fact(DisplayName = "L16 example 1: PrintOdds(7) prints 4 lines")]
        public void Example1() => Expect.Prints(
            """
            1
            3
            5
            7
            """, () => L16_OddNumbers.PrintOdds(7));

        [Fact(DisplayName = "L16 example 2: PrintOdds(8) prints 4 lines")]
        public void Example2() => Expect.Prints(
            """
            1
            3
            5
            7
            """, () => L16_OddNumbers.PrintOdds(8));

        [Fact(DisplayName = "L16 example 3: PrintOdds(1) prints \"1\"")]
        public void Example3() => Expect.Prints("1", () => L16_OddNumbers.PrintOdds(1));
    }
}
