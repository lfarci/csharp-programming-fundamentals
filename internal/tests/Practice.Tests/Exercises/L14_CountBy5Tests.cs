// Tests for L14 · Count by 5
// Exercise page: exercises/L14-count-by-5.md
// Your code:     practice/L14_CountBy5.cs
// Run them:      ./ex check L14
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class L14_CountBy5Tests
    {
        [Fact(DisplayName = "L14 example 1: CountBy5(22) prints 4 lines")]
        public void Example1() => Expect.Prints(
            """
            5
            10
            15
            20
            """, () => L14_CountBy5.CountBy5(22));

        [Fact(DisplayName = "L14 example 2: CountBy5(5) prints \"5\"")]
        public void Example2() => Expect.Prints("5", () => L14_CountBy5.CountBy5(5));
    }
}
