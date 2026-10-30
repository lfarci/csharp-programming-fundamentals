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

        [Fact(DisplayName = "E01 example 2: edge case, input (empty), 7 prints \"Thanks: 7\"")]
        public void Edge1() => Expect.Output(
            input: ["", "7"],
            lines: ["That is not a number.", "Thanks: 7"],
            run: () => E01_SafeNumberReader.Run(), hint: "an empty line is not a number either: ask again.");

        [Fact(DisplayName = "E01 example 3: edge case, input 99999999999, 7 prints \"Thanks: 7\"")]
        public void Edge2() => Expect.Output(
            input: ["99999999999", "7"],
            lines: ["That number is too big.", "Thanks: 7"],
            run: () => E01_SafeNumberReader.Run(), hint: "too big for an int: int.Parse throws an OverflowException. Catch it with a second catch block.");
    }
}
