// Tests for A04 · Factorial
// Exercise page: exercises/A04-factorial.md
// Your code:     practice/A04_Factorial.cs
// Run them:      ./ex check A04
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class A04_FactorialTests
    {
        [Fact(DisplayName = "A04 example 1: Factorial(5) returns 120")]
        public void Example1() => Expect.Returns(120L, () => A04_Factorial.Factorial(5));

        [Fact(DisplayName = "A04 example 2: Factorial(0) returns 1")]
        public void Example2() => Expect.Returns(1L, () => A04_Factorial.Factorial(0));

        [Fact(DisplayName = "A04 example 3: Factorial(1) returns 1")]
        public void Example3() => Expect.Returns(1L, () => A04_Factorial.Factorial(1));

        [Fact(DisplayName = "A04 example 4: Factorial(12) returns 479001600")]
        public void Example4() => Expect.Returns(479001600L, () => A04_Factorial.Factorial(12));

        [Fact(DisplayName = "A04 example 5: Factorial(20) returns 2432902008176640000")]
        public void Example5() => Expect.Returns(2432902008176640000L, () => A04_Factorial.Factorial(20));
    }
}
