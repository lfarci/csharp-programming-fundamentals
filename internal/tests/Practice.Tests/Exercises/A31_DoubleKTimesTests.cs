// Tests for A31 · Double k times
// Exercise page: exercises/A31-double-k-times.md
// Your code:     practice/A31_DoubleKTimes.cs
// Run them:      ./ex check A31
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class A31_DoubleKTimesTests
    {
        [Fact(DisplayName = "A31 example 1: DoubleTimes(5, 3) returns 40")]
        public void Example1() => Expect.Returns(40L, () => A31_DoubleKTimes.DoubleTimes(5, 3));

        [Fact(DisplayName = "A31 example 2: DoubleTimes(7, 0) returns 7")]
        public void Example2() => Expect.Returns(7L, () => A31_DoubleKTimes.DoubleTimes(7, 0));

        [Fact(DisplayName = "A31 example 3: DoubleTimes(1, 10) returns 1024")]
        public void Example3() => Expect.Returns(1024L, () => A31_DoubleKTimes.DoubleTimes(1, 10));

        [Fact(DisplayName = "A31 example 4: DoubleTimes(3, 1) returns 6")]
        public void Example4() => Expect.Returns(6L, () => A31_DoubleKTimes.DoubleTimes(3, 1));
    }
}
