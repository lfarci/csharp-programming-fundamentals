// Tests for S04 · Doubling
// Exercise page: exercises/S04-doubling.md
// Your code:     practice/S04_Doubling.cs
// Run them:      ./ex check S04
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class S04_DoublingTests
    {
        [Fact(DisplayName = "S04 example 1: PrintDoubling(1, 5) prints 5 lines")]
        public void Example1() => Expect.Prints(
            """
            1
            2
            4
            8
            16
            """, () => S04_Doubling.PrintDoubling(1, 5));

        [Fact(DisplayName = "S04 example 2: PrintDoubling(3, 3) prints 3 lines")]
        public void Example2() => Expect.Prints(
            """
            3
            6
            12
            """, () => S04_Doubling.PrintDoubling(3, 3));
    }
}
