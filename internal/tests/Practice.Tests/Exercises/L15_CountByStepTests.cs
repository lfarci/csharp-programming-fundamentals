// Tests for L15 · Count by any step
// Exercise page: exercises/L15-count-by-step.md
// Your code:     practice/L15_CountByStep.cs
// Run them:      ./ex check L15
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class L15_CountByStepTests
    {
        [Fact(DisplayName = "L15 example 1: CountByStep(2, 7) prints 3 lines")]
        public void Example1() => Expect.Prints(
            """
            2
            4
            6
            """, () => L15_CountByStep.CountByStep(2, 7));

        [Fact(DisplayName = "L15 example 2: CountByStep(4, 12) prints 3 lines")]
        public void Example2() => Expect.Prints(
            """
            4
            8
            12
            """, () => L15_CountByStep.CountByStep(4, 12));

        [Fact(DisplayName = "L15 example 3: CountByStep(1, 3) prints 3 lines")]
        public void Example3() => Expect.Prints(
            """
            1
            2
            3
            """, () => L15_CountByStep.CountByStep(1, 3));

        [Fact(DisplayName = "L15 example 4: edge case, CountByStep(5, 3) prints nothing")]
        public void Edge1() => Expect.Prints("", () => L15_CountByStep.CountByStep(5, 3), hint: "step is bigger than n: the first value is already too big, nothing is printed.");
    }
}
