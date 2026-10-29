// Tests for E02 · Parse or zero
// Exercise page: exercises/E02-parse-or-zero.md
// Your code:     practice/E02_ParseOrZero.cs
// Run them:      ./ex check E02
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class E02_ParseOrZeroTests
    {
        [Fact(DisplayName = "E02 example 1: ParseOrZero(\"42\") returns 42")]
        public void Example1() => Expect.Returns(42, () => E02_ParseOrZero.ParseOrZero("42"));

        [Fact(DisplayName = "E02 example 2: ParseOrZero(\"abc\") returns 0")]
        public void Example2() => Expect.Returns(0, () => E02_ParseOrZero.ParseOrZero("abc"));

        [Fact(DisplayName = "E02 example 3: ParseOrZero(\"\") returns 0")]
        public void Example3() => Expect.Returns(0, () => E02_ParseOrZero.ParseOrZero(""));

        [Fact(DisplayName = "E02 example 4: ParseOrZero(\"-7\") returns -7")]
        public void Example4() => Expect.Returns(-7, () => E02_ParseOrZero.ParseOrZero("-7"));
    }
}
