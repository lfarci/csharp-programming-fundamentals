// Tests for A13 · Sum from a to b
// Exercise page: exercises/A13-sum-from-a-to-b.md
// Your code:     practice/A13_SumFromAToB.cs
// Run them:      ./ex check A13
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class A13_SumFromAToBTests
    {
        [Fact(DisplayName = "A13 example 1: SumFromTo(3, 5) returns 12")]
        public void Example1() => Expect.Returns(12, () => A13_SumFromAToB.SumFromTo(3, 5));

        [Fact(DisplayName = "A13 example 2: SumFromTo(1, 4) returns 10")]
        public void Example2() => Expect.Returns(10, () => A13_SumFromAToB.SumFromTo(1, 4));

        [Fact(DisplayName = "A13 example 3: SumFromTo(7, 7) returns 7")]
        public void Example3() => Expect.Returns(7, () => A13_SumFromAToB.SumFromTo(7, 7));

        [Fact(DisplayName = "A13 example 4: SumFromTo(5, 4) returns 0")]
        public void Example4() => Expect.Returns(0, () => A13_SumFromAToB.SumFromTo(5, 4));
    }
}
