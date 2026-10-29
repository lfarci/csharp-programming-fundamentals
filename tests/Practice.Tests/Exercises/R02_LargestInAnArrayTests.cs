// Tests for R02 · Position of the largest
// Exercise page: exercises/R02-largest-in-an-array.md
// Your code:     practice/R02_LargestInAnArray.cs
// Run them:      ./ex check R02
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class R02_LargestInAnArrayTests
    {
        [Fact(DisplayName = "R02 example 1: IndexOfLargest([-5, -2, -9]) returns 1")]
        public void Example1() => Expect.Returns(1, () => R02_LargestInAnArray.IndexOfLargest(new[] { -5, -2, -9 }));

        [Fact(DisplayName = "R02 example 2: IndexOfLargest([3, 7, 2, 7, 1]) returns 1")]
        public void Example2() => Expect.Returns(1, () => R02_LargestInAnArray.IndexOfLargest(new[] { 3, 7, 2, 7, 1 }));

        [Fact(DisplayName = "R02 example 3: IndexOfLargest([4]) returns 0")]
        public void Example3() => Expect.Returns(0, () => R02_LargestInAnArray.IndexOfLargest(new[] { 4 }));

        [Fact(DisplayName = "R02 example 4: IndexOfLargest([1, 2, 9]) returns 2")]
        public void Example4() => Expect.Returns(2, () => R02_LargestInAnArray.IndexOfLargest(new[] { 1, 2, 9 }));
    }
}
