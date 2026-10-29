// Tests for N02 · A method that calls one
// Exercise page: exercises/N02-is-multiple-and-count.md
// Your code:     practice/N02_IsMultipleAndCount.cs
// Run them:      ./ex check N02
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class N02_IsMultipleAndCountTests
    {
        [Fact(DisplayName = "N02 example 1: IsMultiple(12, 3) returns true")]
        public void Example1() => Expect.Returns(true, () => N02_IsMultipleAndCount.IsMultiple(12, 3));

        [Fact(DisplayName = "N02 example 2: IsMultiple(7, 2) returns false")]
        public void Example2() => Expect.Returns(false, () => N02_IsMultipleAndCount.IsMultiple(7, 2));

        [Fact(DisplayName = "N02 example 3: CountMultiples(20, 5) returns 4")]
        public void Example3() => Expect.Returns(4, () => N02_IsMultipleAndCount.CountMultiples(20, 5));

        [Fact(DisplayName = "N02 example 4: CountMultiples(10, 3) returns 3")]
        public void Example4() => Expect.Returns(3, () => N02_IsMultipleAndCount.CountMultiples(10, 3));

        [Fact(DisplayName = "N02 example 5: CountMultiples(4, 5) returns 0")]
        public void Example5() => Expect.Returns(0, () => N02_IsMultipleAndCount.CountMultiples(4, 5));
    }
}
