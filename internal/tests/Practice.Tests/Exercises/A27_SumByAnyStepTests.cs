// Tests for A27 · Sum by any step
// Exercise page: exercises/A27-sum-by-any-step.md
// Your code:     practice/A27_SumByAnyStep.cs
// Run them:      ./ex check A27
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class A27_SumByAnyStepTests
    {
        [Fact(DisplayName = "A27 example 1: SumByStep(1, 10, 3) returns 22")]
        public void Example1() => Expect.Returns(22, () => A27_SumByAnyStep.SumByStep(1, 10, 3));

        [Fact(DisplayName = "A27 example 2: SumByStep(2, 10, 4) returns 18")]
        public void Example2() => Expect.Returns(18, () => A27_SumByAnyStep.SumByStep(2, 10, 4));

        [Fact(DisplayName = "A27 example 3: SumByStep(5, 5, 2) returns 5")]
        public void Example3() => Expect.Returns(5, () => A27_SumByAnyStep.SumByStep(5, 5, 2));

        [Fact(DisplayName = "A27 example 4: SumByStep(6, 5, 1) returns 0")]
        public void Example4() => Expect.Returns(0, () => A27_SumByAnyStep.SumByStep(6, 5, 1));
    }
}
