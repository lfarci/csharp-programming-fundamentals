// Tests for L22 · Words until stop
// Exercise page: exercises/L22-words-until-stop.md
// Your code:     practice/L22_WordsUntilStop.cs
// Run them:      ./ex check L22
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class L22_WordsUntilStopTests
    {
        [Fact(DisplayName = "L22 example 1: input cat, dog, stop prints \"You typed 2 words.\"")]
        public void Example1() => Expect.Output(
            input: ["cat", "dog", "stop"],
            lines: ["You typed 2 words."],
            run: () => L22_WordsUntilStop.Run());

        [Fact(DisplayName = "L22 example 2: input red, green, blue, stop prints \"You typed 3 words.\"")]
        public void Example2() => Expect.Output(
            input: ["red", "green", "blue", "stop"],
            lines: ["You typed 3 words."],
            run: () => L22_WordsUntilStop.Run());

        [Fact(DisplayName = "L22 example 3: input stop prints \"You typed 0 words.\"")]
        public void Example3() => Expect.Output(
            input: ["stop"],
            lines: ["You typed 0 words."],
            run: () => L22_WordsUntilStop.Run());
    }
}
