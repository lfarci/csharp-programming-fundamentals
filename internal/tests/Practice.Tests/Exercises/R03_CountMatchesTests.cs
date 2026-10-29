// Tests for R03 · Count matches
// Exercise page: exercises/R03-count-matches.md
// Your code:     practice/R03_CountMatches.cs
// Run them:      ./ex check R03
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class R03_CountMatchesTests
    {
        [Fact(DisplayName = "R03 example 1: CountMatches([2, 4, 2, 5, 2], 2) returns 3")]
        public void Example1() => Expect.Returns(3, () => R03_CountMatches.CountMatches(new[] { 2, 4, 2, 5, 2 }, 2));

        [Fact(DisplayName = "R03 example 2: CountMatches([1, 1], 9) returns 0")]
        public void Example2() => Expect.Returns(0, () => R03_CountMatches.CountMatches(new[] { 1, 1 }, 9));

        [Fact(DisplayName = "R03 example 3: CountMatches([], 3) returns 0")]
        public void Example3() => Expect.Returns(0, () => R03_CountMatches.CountMatches(new int[0], 3));
    }
}
