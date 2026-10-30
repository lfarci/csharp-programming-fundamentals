// Tests for R08 · Is it sorted?
// Exercise page: exercises/R08-is-it-sorted.md
// Your code:     practice/R08_IsItSorted.cs
// Run them:      ./ex check R08
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class R08_IsItSortedTests
    {
        [Fact(DisplayName = "R08 example 1: IsSorted([1, 2, 2, 5]) returns true")]
        public void Example1() => Expect.Returns(true, () => R08_IsItSorted.IsSorted(new[] { 1, 2, 2, 5 }));

        [Fact(DisplayName = "R08 example 2: IsSorted([3, 1, 2]) returns false")]
        public void Example2() => Expect.Returns(false, () => R08_IsItSorted.IsSorted(new[] { 3, 1, 2 }));

        [Fact(DisplayName = "R08 example 3: IsSorted([1, 2, 4, 3]) returns false")]
        public void Example3() => Expect.Returns(false, () => R08_IsItSorted.IsSorted(new[] { 1, 2, 4, 3 }));

        [Fact(DisplayName = "R08 example 4: IsSorted([7]) returns true")]
        public void Example4() => Expect.Returns(true, () => R08_IsItSorted.IsSorted(new[] { 7 }));

        [Fact(DisplayName = "R08 example 5: IsSorted([]) returns true")]
        public void Example5() => Expect.Returns(true, () => R08_IsItSorted.IsSorted(new int[0]));
    }
}
