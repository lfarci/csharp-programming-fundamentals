// Tests for L19 · Count the turns
// Exercise page: exercises/L19-count-the-turns.md
// Your code:     practice/L19_CountTheTurns.cs
// Run them:      ./ex check L19
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class L19_CountTheTurnsTests
    {
        [Fact(DisplayName = "L19 example 1: CountTurns(1, 5) returns 5")]
        public void Example1() => Expect.Returns(5, () => L19_CountTheTurns.CountTurns(1, 5));

        [Fact(DisplayName = "L19 example 2: CountTurns(3, 3) returns 1")]
        public void Example2() => Expect.Returns(1, () => L19_CountTheTurns.CountTurns(3, 3));

        [Fact(DisplayName = "L19 example 3: CountTurns(4, 10) returns 7")]
        public void Example3() => Expect.Returns(7, () => L19_CountTheTurns.CountTurns(4, 10));

        [Fact(DisplayName = "L19 example 4: CountTurns(5, 4) returns 0")]
        public void Example4() => Expect.Returns(0, () => L19_CountTheTurns.CountTurns(5, 4));
    }
}
