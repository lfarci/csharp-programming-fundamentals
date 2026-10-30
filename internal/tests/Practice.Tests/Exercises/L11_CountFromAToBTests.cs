// Tests for L11 · Count from a to b
// Exercise page: exercises/L11-count-from-a-to-b.md
// Your code:     practice/L11_CountFromAToB.cs
// Run them:      ./ex check L11
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class L11_CountFromAToBTests
    {
        [Fact(DisplayName = "L11 example 1: PrintFromTo(3, 6) prints 4 lines")]
        public void Example1() => Expect.Prints(
            """
            3
            4
            5
            6
            """, () => L11_CountFromAToB.PrintFromTo(3, 6));

        [Fact(DisplayName = "L11 example 2: PrintFromTo(5, 5) prints \"5\"")]
        public void Example2() => Expect.Prints("5", () => L11_CountFromAToB.PrintFromTo(5, 5));

        [Fact(DisplayName = "L11 example 3: PrintFromTo(-2, 1) prints 4 lines")]
        public void Example3() => Expect.Prints(
            """
            -2
            -1
            0
            1
            """, () => L11_CountFromAToB.PrintFromTo(-2, 1));

        [Fact(DisplayName = "L11 example 4: edge case, PrintFromTo(6, 3) prints nothing")]
        public void Edge1() => Expect.Prints("", () => L11_CountFromAToB.PrintFromTo(6, 3), hint: "when a is bigger than b the loop test is false from the start: the loop runs 0 times.");
    }
}
