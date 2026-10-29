// Tests for C01 · Even or odd
// Exercise page: exercises/C01-even-or-odd.md
// Your code:     practice/C01_EvenOrOdd.cs
// Run them:      ./ex check C01
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class C01_EvenOrOddTests
    {
        [Fact(DisplayName = "C01 example 1: IsEven(7) returns false")]
        public void Example1() => Expect.Returns(false, () => C01_EvenOrOdd.IsEven(7));

        [Fact(DisplayName = "C01 example 2: IsEven(0) returns true")]
        public void Example2() => Expect.Returns(true, () => C01_EvenOrOdd.IsEven(0));

        [Fact(DisplayName = "C01 example 3: IsEven(-4) returns true")]
        public void Example3() => Expect.Returns(true, () => C01_EvenOrOdd.IsEven(-4));

        [Fact(DisplayName = "C01 example 4: IsEven(-3) returns false")]
        public void Example4() => Expect.Returns(false, () => C01_EvenOrOdd.IsEven(-3));
    }
}
