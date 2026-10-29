// Tests for F01 · Save numbers to a file
// Exercise page: exercises/F01-numbers-file.md
// Your code:     practice/F01_NumbersFile.cs
// Run them:      ./ex check F01
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class F01_NumbersFileTests
    {
        [Fact(DisplayName = "F01 example 1: input 4, 7, 1, 0 prints \"Sum: 12\"")]
        public void Example1() => Expect.Output(
            input: ["4", "7", "1", "0"],
            lines: ["Lines: 3", "Sum: 12"],
            run: () => F01_NumbersFile.Run());

        [Fact(DisplayName = "F01 example 2: input 0 prints \"Sum: 0\"")]
        public void Example2() => Expect.Output(
            input: ["0"],
            lines: ["Lines: 0", "Sum: 0"],
            run: () => F01_NumbersFile.Run());
    }
}
