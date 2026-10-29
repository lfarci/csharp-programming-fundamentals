// Tests for P07 · All digits odd
// Exercise page: exercises/P07-all-digits-odd.md
// Your code:     practice/P07_AllDigitsOdd.cs
// Run them:      ./ex check P07
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class P07_AllDigitsOddTests
    {
        [Fact(DisplayName = "P07 example 1: AllDigitsOdd(1357) returns true")]
        public void Example1() => Expect.Returns(true, () => P07_AllDigitsOdd.AllDigitsOdd(1357));

        [Fact(DisplayName = "P07 example 2: AllDigitsOdd(1352) returns false")]
        public void Example2() => Expect.Returns(false, () => P07_AllDigitsOdd.AllDigitsOdd(1352));

        [Fact(DisplayName = "P07 example 3: AllDigitsOdd(7) returns true")]
        public void Example3() => Expect.Returns(true, () => P07_AllDigitsOdd.AllDigitsOdd(7));

        [Fact(DisplayName = "P07 example 4: AllDigitsOdd(20) returns false")]
        public void Example4() => Expect.Returns(false, () => P07_AllDigitsOdd.AllDigitsOdd(20));
    }
}
