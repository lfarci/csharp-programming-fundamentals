// Tests for A02 · Count multiples of 3
// Exercise page: exercises/A02-count-multiples-of-3.md
// Your code:     practice/A02_CountMultiplesOf3.cs
// Run them:      ./ex check A02
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class A02_CountMultiplesOf3Tests
    {
        [Fact(DisplayName = "A02 example 1: CountMultiplesOf3(10) returns 3")]
        public void Example1() => Expect.Returns(3, () => A02_CountMultiplesOf3.CountMultiplesOf3(10));

        [Fact(DisplayName = "A02 example 2: CountMultiplesOf3(2) returns 0")]
        public void Example2() => Expect.Returns(0, () => A02_CountMultiplesOf3.CountMultiplesOf3(2));

        [Fact(DisplayName = "A02 example 3: CountMultiplesOf3(9) returns 3")]
        public void Example3() => Expect.Returns(3, () => A02_CountMultiplesOf3.CountMultiplesOf3(9));

        [Fact(DisplayName = "A02 example 4: CountMultiplesOf3(0) returns 0")]
        public void Example4() => Expect.Returns(0, () => A02_CountMultiplesOf3.CountMultiplesOf3(0));
    }
}
