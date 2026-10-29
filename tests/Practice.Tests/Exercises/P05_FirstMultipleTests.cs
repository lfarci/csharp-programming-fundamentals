// Tests for P05 · First multiple
// Exercise page: exercises/P05-first-multiple.md
// Your code:     practice/P05_FirstMultiple.cs
// Run them:      ./ex check P05
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class P05_FirstMultipleTests
    {
        [Fact(DisplayName = "P05 example 1: FirstMultiple(10, 20, 7) returns 14")]
        public void Example1() => Expect.Returns(14, () => P05_FirstMultiple.FirstMultiple(10, 20, 7));

        [Fact(DisplayName = "P05 example 2: FirstMultiple(1, 5, 6) returns -1")]
        public void Example2() => Expect.Returns(-1, () => P05_FirstMultiple.FirstMultiple(1, 5, 6));

        [Fact(DisplayName = "P05 example 3: FirstMultiple(6, 9, 3) returns 6")]
        public void Example3() => Expect.Returns(6, () => P05_FirstMultiple.FirstMultiple(6, 9, 3));

        [Fact(DisplayName = "P05 example 4: FirstMultiple(1, 30, 10) returns 10")]
        public void Example4() => Expect.Returns(10, () => P05_FirstMultiple.FirstMultiple(1, 30, 10));
    }
}
