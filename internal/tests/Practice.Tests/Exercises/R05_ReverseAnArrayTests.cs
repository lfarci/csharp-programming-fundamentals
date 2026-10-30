// Tests for R05 · Reverse an array
// Exercise page: exercises/R05-reverse-an-array.md
// Your code:     practice/R05_ReverseAnArray.cs
// Run them:      ./ex check R05
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class R05_ReverseAnArrayTests
    {
        [Fact(DisplayName = "R05 example 1: Reversed([1, 2, 3, 4]) returns [4, 3, 2, 1]")]
        public void Example1() => Expect.Returns(new[] { 4, 3, 2, 1 }, () => R05_ReverseAnArray.Reversed(new[] { 1, 2, 3, 4 }));

        [Fact(DisplayName = "R05 example 2: Reversed([8]) returns [8]")]
        public void Example2() => Expect.Returns(new[] { 8 }, () => R05_ReverseAnArray.Reversed(new[] { 8 }));

        [Fact(DisplayName = "R05 example 3: Reversed([]) returns []")]
        public void Example3() => Expect.Returns(new int[0], () => R05_ReverseAnArray.Reversed(new int[0]));

        [Fact(DisplayName = "R05 example 4: edge case, Reversed([1, 2, 3]) returns [3, 2, 1]")]
        public void Edge1() => Expect.Returns(new[] { 3, 2, 1 }, () => R05_ReverseAnArray.Reversed(new[] { 1, 2, 3 }), hint: "odd length: the middle value stays in the middle.");
    }
}
