// Tests for C04 · Grade from a score
// Exercise page: exercises/C04-grade-from-a-score.md
// Your code:     practice/C04_GradeFromAScore.cs
// Run them:      ./ex check C04
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class C04_GradeFromAScoreTests
    {
        [Fact(DisplayName = "C04 example 1: Grade(95) returns \"A\"")]
        public void Example1() => Expect.Returns("A", () => C04_GradeFromAScore.Grade(95));

        [Fact(DisplayName = "C04 example 2: Grade(90) returns \"A\"")]
        public void Example2() => Expect.Returns("A", () => C04_GradeFromAScore.Grade(90));

        [Fact(DisplayName = "C04 example 3: Grade(89) returns \"B\"")]
        public void Example3() => Expect.Returns("B", () => C04_GradeFromAScore.Grade(89));

        [Fact(DisplayName = "C04 example 4: Grade(80) returns \"B\"")]
        public void Example4() => Expect.Returns("B", () => C04_GradeFromAScore.Grade(80));

        [Fact(DisplayName = "C04 example 5: Grade(75) returns \"C\"")]
        public void Example5() => Expect.Returns("C", () => C04_GradeFromAScore.Grade(75));

        [Fact(DisplayName = "C04 example 6: Grade(50) returns \"D\"")]
        public void Example6() => Expect.Returns("D", () => C04_GradeFromAScore.Grade(50));

        [Fact(DisplayName = "C04 example 7: Grade(49) returns \"F\"")]
        public void Example7() => Expect.Returns("F", () => C04_GradeFromAScore.Grade(49));

        [Fact(DisplayName = "C04 example 8: Grade(0) returns \"F\"")]
        public void Example8() => Expect.Returns("F", () => C04_GradeFromAScore.Grade(0));
    }
}
