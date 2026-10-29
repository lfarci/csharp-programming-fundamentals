// Tests for A16 · Count multiples of 5
// Exercise page: exercises/A16-count-multiples-of-5.md
// Your code:     practice/A16_CountMultiplesOf5.cs
// Run them:      ./ex check A16
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class A16_CountMultiplesOf5Tests
    {
        [Fact(DisplayName = "A16 example 1: CountMultiplesOf5(20) returns 4")]
        public void Example1() => Expect.Returns(4, () => A16_CountMultiplesOf5.CountMultiplesOf5(20));

        [Fact(DisplayName = "A16 example 2: CountMultiplesOf5(4) returns 0")]
        public void Example2() => Expect.Returns(0, () => A16_CountMultiplesOf5.CountMultiplesOf5(4));

        [Fact(DisplayName = "A16 example 3: CountMultiplesOf5(26) returns 5")]
        public void Example3() => Expect.Returns(5, () => A16_CountMultiplesOf5.CountMultiplesOf5(26));
    }
}
