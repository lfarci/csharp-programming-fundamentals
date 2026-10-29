// Tests for E01 · Safe number reader
// Exercise page: exercises/E01-safe-number-reader.md
// Your code:     practice/E01_SafeNumberReader.cs
// Run them:      ./ex check E01
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class E01_SafeNumberReaderTests
    {
        [Fact(DisplayName = "E01 example 1: input abc, 12x, 42 prints \"Thanks: 42\"")]
        public void Example1() => Expect.Output(
            input: ["abc", "12x", "42"],
            lines: ["That is not a number.", "That is not a number.", "Thanks: 42"],
            run: () => E01_SafeNumberReader.Run());
    }
}
