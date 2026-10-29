// Tests for L06 · Even numbers
// Exercise page: exercises/L06-even-numbers.md
// Your code:     practice/L06_EvenNumbers.cs
// Run them:      ./ex check L06
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class L06_EvenNumbersTests
    {
        [Fact(DisplayName = "L06 example 1: input 9 prints \"2 4 6 8\"")]
        public void Example1() => Expect.Output(
            input: ["9"],
            lines: ["2 4 6 8"],
            run: () => L06_EvenNumbers.Run());

        [Fact(DisplayName = "L06 example 2: input 10 prints \"2 4 6 8 10\"")]
        public void Example2() => Expect.Output(
            input: ["10"],
            lines: ["2 4 6 8 10"],
            run: () => L06_EvenNumbers.Run());

        [Fact(DisplayName = "L06 example 3: input 1 prints nothing")]
        public void Example3() => Expect.Output(
            input: ["1"],
            lines: [],
            run: () => L06_EvenNumbers.Run());
    }
}
