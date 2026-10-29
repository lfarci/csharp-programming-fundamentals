// Tests for A12 · Fix: multiples of 7
// Exercise page: exercises/A12-fix-count-multiples-of-7.md
// Your code:     practice/A12_FixCountMultiplesOf7.cs
// Run them:      ./ex check A12
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class A12_FixCountMultiplesOf7Tests
    {
        const string Hint = "the code has 2 bugs. Trace the failing call on paper. Look at the start value of the box, then at the loop test (< or <=).";

        [Fact(DisplayName = "A12 example 1: CountMultiplesOf7(7) returns 1")]
        public void Example1() => Expect.Returns(1, () => A12_FixCountMultiplesOf7.CountMultiplesOf7(7), hint: Hint);

        [Fact(DisplayName = "A12 example 2: CountMultiplesOf7(20) returns 2")]
        public void Example2() => Expect.Returns(2, () => A12_FixCountMultiplesOf7.CountMultiplesOf7(20), hint: Hint);

        [Fact(DisplayName = "A12 example 3: CountMultiplesOf7(6) returns 0")]
        public void Example3() => Expect.Returns(0, () => A12_FixCountMultiplesOf7.CountMultiplesOf7(6), hint: Hint);

        [Fact(DisplayName = "A12 example 4: CountMultiplesOf7(21) returns 3")]
        public void Example4() => Expect.Returns(3, () => A12_FixCountMultiplesOf7.CountMultiplesOf7(21), hint: Hint);
    }
}
