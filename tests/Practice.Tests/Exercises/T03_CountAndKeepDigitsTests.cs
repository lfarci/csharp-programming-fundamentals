// Tests for T03 · Keep the digits
// Exercise page: exercises/T03-count-and-keep-digits.md
// Your code:     practice/T03_CountAndKeepDigits.cs
// Run them:      ./ex check T03
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class T03_CountAndKeepDigitsTests
    {
        [Fact(DisplayName = "T03 example 1: KeepDigits(\"a1 b2!\") returns \"12\"")]
        public void Example1() => Expect.Returns("12", () => T03_CountAndKeepDigits.KeepDigits("a1 b2!"));

        [Fact(DisplayName = "T03 example 2: KeepDigits(\"abc\") returns \"\"")]
        public void Example2() => Expect.Returns("", () => T03_CountAndKeepDigits.KeepDigits("abc"));

        [Fact(DisplayName = "T03 example 3: KeepDigits(\"2026\") returns \"2026\"")]
        public void Example3() => Expect.Returns("2026", () => T03_CountAndKeepDigits.KeepDigits("2026"));
    }
}
