// Tests for L17 · Count down by 2
// Exercise page: exercises/L17-count-down-by-2.md
// Your code:     practice/L17_CountDownBy2.cs
// Run them:      ./ex check L17
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class L17_CountDownBy2Tests
    {
        [Fact(DisplayName = "L17 example 1: CountDownBy2(9) prints 5 lines")]
        public void Example1() => Expect.Prints(
            """
            9
            7
            5
            3
            1
            """, () => L17_CountDownBy2.CountDownBy2(9));

        [Fact(DisplayName = "L17 example 2: CountDownBy2(6) prints 3 lines")]
        public void Example2() => Expect.Prints(
            """
            6
            4
            2
            """, () => L17_CountDownBy2.CountDownBy2(6));
    }
}
