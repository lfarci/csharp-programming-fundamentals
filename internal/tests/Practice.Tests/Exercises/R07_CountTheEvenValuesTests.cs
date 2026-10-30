// Tests for R07 · Count the even values
// Exercise page: exercises/R07-count-the-even-values.md
// Your code:     practice/R07_CountTheEvenValues.cs
// Run them:      ./ex check R07
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class R07_CountTheEvenValuesTests
    {
        [Fact(DisplayName = "R07 example 1: CountEven([1, 2, 3, 4]) returns 2")]
        public void Example1() => Expect.Returns(2, () => R07_CountTheEvenValues.CountEven(new[] { 1, 2, 3, 4 }));

        [Fact(DisplayName = "R07 example 2: CountEven([2, 4, 6]) returns 3")]
        public void Example2() => Expect.Returns(3, () => R07_CountTheEvenValues.CountEven(new[] { 2, 4, 6 }));

        [Fact(DisplayName = "R07 example 3: CountEven([1, 3]) returns 0")]
        public void Example3() => Expect.Returns(0, () => R07_CountTheEvenValues.CountEven(new[] { 1, 3 }));

        [Fact(DisplayName = "R07 example 4: CountEven([]) returns 0")]
        public void Example4() => Expect.Returns(0, () => R07_CountTheEvenValues.CountEven(new int[0]));

        [Fact(DisplayName = "R07 example 5: CountEven([-2, 0, 5]) returns 2")]
        public void Example5() => Expect.Returns(2, () => R07_CountTheEvenValues.CountEven(new[] { -2, 0, 5 }));
    }
}
