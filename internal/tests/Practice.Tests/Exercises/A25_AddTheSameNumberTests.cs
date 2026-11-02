// Tests for A25 · Add the same number
// Exercise page: exercises/A25-add-the-same-number.md
// Your code:     practice/A25_AddTheSameNumber.cs
// Run them:      ./ex check A25
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class A25_AddTheSameNumberTests
    {
        [Fact(DisplayName = "A25 example 1: AddRepeated(4, 3) returns 12")]
        public void Example1() => Expect.Returns(12, () => A25_AddTheSameNumber.AddRepeated(4, 3));

        [Fact(DisplayName = "A25 example 2: AddRepeated(7, 1) returns 7")]
        public void Example2() => Expect.Returns(7, () => A25_AddTheSameNumber.AddRepeated(7, 1));

        [Fact(DisplayName = "A25 example 3: AddRepeated(5, 0) returns 0")]
        public void Example3() => Expect.Returns(0, () => A25_AddTheSameNumber.AddRepeated(5, 0));

        [Fact(DisplayName = "A25 example 4: AddRepeated(2, 10) returns 20")]
        public void Example4() => Expect.Returns(20, () => A25_AddTheSameNumber.AddRepeated(2, 10));
    }
}
