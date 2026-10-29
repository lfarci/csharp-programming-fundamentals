// Tests for L07 · Ask until valid
// Exercise page: exercises/L07-ask-until-valid.md
// Your code:     practice/L07_AskUntilValid.cs
// Run them:      ./ex check L07
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class L07_AskUntilValidTests
    {
        [Fact(DisplayName = "L07 example 1: input abc, 42, 7 prints \"You chose 7\"")]
        public void Example1() => Expect.Output(
            input: ["abc", "42", "7"],
            lines: ["Invalid, try again.", "Invalid, try again.", "You chose 7"],
            run: () => L07_AskUntilValid.Run());

        [Fact(DisplayName = "L07 example 2: input 1 prints \"You chose 1\"")]
        public void Example2() => Expect.Output(
            input: ["1"],
            lines: ["You chose 1"],
            run: () => L07_AskUntilValid.Run());
    }
}
