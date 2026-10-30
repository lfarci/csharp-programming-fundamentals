// Tests for S06 · Collatz steps
// Exercise page: exercises/S06-collatz-steps.md
// Your code:     practice/S06_CollatzSteps.cs
// Run them:      ./ex check S06
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class S06_CollatzStepsTests
    {
        [Fact(DisplayName = "S06 example 1: CollatzSteps(1) returns 0")]
        public void Example1() => Expect.Returns(0, () => S06_CollatzSteps.CollatzSteps(1));

        [Fact(DisplayName = "S06 example 2: CollatzSteps(2) returns 1")]
        public void Example2() => Expect.Returns(1, () => S06_CollatzSteps.CollatzSteps(2));

        [Fact(DisplayName = "S06 example 3: CollatzSteps(6) returns 8")]
        public void Example3() => Expect.Returns(8, () => S06_CollatzSteps.CollatzSteps(6));

        [Fact(DisplayName = "S06 example 4: CollatzSteps(7) returns 16")]
        public void Example4() => Expect.Returns(16, () => S06_CollatzSteps.CollatzSteps(7));

        [Fact(DisplayName = "S06 example 5: CollatzSteps(27) returns 111")]
        public void Example5() => Expect.Returns(111, () => S06_CollatzSteps.CollatzSteps(27));
    }
}
