// Tests for A30 · Power of 10
// Exercise page: exercises/A30-power-of-10.md
// Your code:     practice/A30_PowerOf10.cs
// Run them:      ./ex check A30
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class A30_PowerOf10Tests
    {
        [Fact(DisplayName = "A30 example 1: PowerOf10(3) returns 1000")]
        public void Example1() => Expect.Returns(1000L, () => A30_PowerOf10.PowerOf10(3));

        [Fact(DisplayName = "A30 example 2: PowerOf10(0) returns 1")]
        public void Example2() => Expect.Returns(1L, () => A30_PowerOf10.PowerOf10(0));

        [Fact(DisplayName = "A30 example 3: PowerOf10(1) returns 10")]
        public void Example3() => Expect.Returns(10L, () => A30_PowerOf10.PowerOf10(1));

        [Fact(DisplayName = "A30 example 4: PowerOf10(9) returns 1000000000")]
        public void Example4() => Expect.Returns(1000000000L, () => A30_PowerOf10.PowerOf10(9));

        [Fact(DisplayName = "A30 example 5: edge case, PowerOf10(12) returns 1000000000000")]
        public void Edge1() => Expect.Returns(1000000000000L, () => A30_PowerOf10.PowerOf10(12), hint: "the result is too big for an int (about 2.1 billion at most): use a long for the running result, like the return type.");
    }
}
