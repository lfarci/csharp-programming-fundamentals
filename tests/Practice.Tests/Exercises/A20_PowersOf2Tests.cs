// Tests for A20 · Power of 2
// Exercise page: exercises/A20-powers-of-2.md
// Your code:     practice/A20_PowersOf2.cs
// Run them:      ./ex check A20
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class A20_PowersOf2Tests
    {
        [Fact(DisplayName = "A20 example 1: PowerOf2(3) returns 8")]
        public void Example1() => Expect.Returns(8L, () => A20_PowersOf2.PowerOf2(3));

        [Fact(DisplayName = "A20 example 2: PowerOf2(0) returns 1")]
        public void Example2() => Expect.Returns(1L, () => A20_PowersOf2.PowerOf2(0));

        [Fact(DisplayName = "A20 example 3: PowerOf2(10) returns 1024")]
        public void Example3() => Expect.Returns(1024L, () => A20_PowersOf2.PowerOf2(10));
    }
}
