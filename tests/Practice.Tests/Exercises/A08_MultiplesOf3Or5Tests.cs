// Tests for A08 · Multiples of 3 or 5
// Exercise page: exercises/A08-multiples-of-3-or-5.md
// Your code:     practice/A08_MultiplesOf3Or5.cs
// Run them:      ./ex check A08
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class A08_MultiplesOf3Or5Tests
    {
        [Fact(DisplayName = "A08 example 1: SumOfMultiples(10) returns 23")]
        public void Example1() => Expect.Returns(23, () => A08_MultiplesOf3Or5.SumOfMultiples(10));

        [Fact(DisplayName = "A08 example 2: SumOfMultiples(20) returns 78")]
        public void Example2() => Expect.Returns(78, () => A08_MultiplesOf3Or5.SumOfMultiples(20));

        [Fact(DisplayName = "A08 example 3: SumOfMultiples(1) returns 0")]
        public void Example3() => Expect.Returns(0, () => A08_MultiplesOf3Or5.SumOfMultiples(1));

        [Fact(DisplayName = "A08 example 4: SumOfMultiples(16) returns 60")]
        public void Example4() => Expect.Returns(60, () => A08_MultiplesOf3Or5.SumOfMultiples(16));
    }
}
