// Tests for R04 · Find the position
// Exercise page: exercises/R04-find-the-position.md
// Your code:     practice/R04_FindThePosition.cs
// Run them:      ./ex check R04
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class R04_FindThePositionTests
    {
        [Fact(DisplayName = "R04 example 1: IndexOf([7, 3, 9, 3], 3) returns 1")]
        public void Example1() => Expect.Returns(1, () => R04_FindThePosition.IndexOf(new[] { 7, 3, 9, 3 }, 3));

        [Fact(DisplayName = "R04 example 2: IndexOf([7, 3, 9, 3], 8) returns -1")]
        public void Example2() => Expect.Returns(-1, () => R04_FindThePosition.IndexOf(new[] { 7, 3, 9, 3 }, 8));

        [Fact(DisplayName = "R04 example 3: IndexOf([5], 5) returns 0")]
        public void Example3() => Expect.Returns(0, () => R04_FindThePosition.IndexOf(new[] { 5 }, 5));

        [Fact(DisplayName = "R04 example 4: IndexOf([], 1) returns -1")]
        public void Example4() => Expect.Returns(-1, () => R04_FindThePosition.IndexOf(new int[0], 1));
    }
}
