// Tests for A01 · Sum from 1 to N
// Exercise page: exercises/A01-sum-1-to-n.md
// Your code:     practice/A01_Sum1ToN.cs
// Run them:      ./ex check A01
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class A01_Sum1ToNTests
    {
        [Fact(DisplayName = "A01 example 1: SumTo(5) returns 15")]
        public void Example1() => Expect.Returns(15, () => A01_Sum1ToN.SumTo(5));

        [Fact(DisplayName = "A01 example 2: SumTo(1) returns 1")]
        public void Example2() => Expect.Returns(1, () => A01_Sum1ToN.SumTo(1));

        [Fact(DisplayName = "A01 example 3: SumTo(10) returns 55")]
        public void Example3() => Expect.Returns(55, () => A01_Sum1ToN.SumTo(10));

        [Fact(DisplayName = "A01 example 4: SumTo(0) returns 0")]
        public void Example4() => Expect.Returns(0, () => A01_Sum1ToN.SumTo(0));
    }
}
