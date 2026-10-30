// Tests for L13 · Count by 3
// Exercise page: exercises/L13-count-by-3.md
// Your code:     practice/L13_CountBy3.cs
// Run them:      ./ex check L13
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class L13_CountBy3Tests
    {
        [Fact(DisplayName = "L13 example 1: CountBy3(10) prints 3 lines")]
        public void Example1() => Expect.Prints(
            """
            3
            6
            9
            """, () => L13_CountBy3.CountBy3(10));

        [Fact(DisplayName = "L13 example 2: CountBy3(3) prints \"3\"")]
        public void Example2() => Expect.Prints("3", () => L13_CountBy3.CountBy3(3));

        [Fact(DisplayName = "L13 example 3: CountBy3(12) prints 4 lines")]
        public void Example3() => Expect.Prints(
            """
            3
            6
            9
            12
            """, () => L13_CountBy3.CountBy3(12));

        [Fact(DisplayName = "L13 example 4: edge case, CountBy3(2) prints nothing")]
        public void Edge1() => Expect.Prints("", () => L13_CountBy3.CountBy3(2), hint: "n is smaller than 3: not even the first number fits, so nothing is printed.");
    }
}
