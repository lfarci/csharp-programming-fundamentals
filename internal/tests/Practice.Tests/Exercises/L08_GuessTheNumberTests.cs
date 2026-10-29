// Tests for L08 · Guess the number
// Exercise page: exercises/L08-guess-the-number.md
// Your code:     practice/L08_GuessTheNumber.cs
// Run them:      ./ex check L08
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class L08_GuessTheNumberTests
    {
        [Fact(DisplayName = "L08 example 1: input 50, 30, 42 prints \"Correct! You needed 3 tries.\"")]
        public void Example1() => Expect.Output(
            input: ["50", "30", "42"],
            lines: ["Lower!", "Higher!", "Correct! You needed 3 tries."],
            run: () => L08_GuessTheNumber.Run());

        [Fact(DisplayName = "L08 example 2: input 42 prints \"Correct! You needed 1 tries.\"")]
        public void Example2() => Expect.Output(
            input: ["42"],
            lines: ["Correct! You needed 1 tries."],
            run: () => L08_GuessTheNumber.Run());
    }
}
