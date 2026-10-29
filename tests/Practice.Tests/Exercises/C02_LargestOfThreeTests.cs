// Tests for C02 · Largest of three
// Exercise page: exercises/C02-largest-of-three.md
// Your code:     practice/C02_LargestOfThree.cs
// Run them:      ./ex check C02
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class C02_LargestOfThreeTests
    {
        [Fact(DisplayName = "C02 example 1: Largest(3, 9, 5) returns 9")]
        public void Example1() => Expect.Returns(9, () => C02_LargestOfThree.Largest(3, 9, 5));

        [Fact(DisplayName = "C02 example 2: Largest(-1, -7, -3) returns -1")]
        public void Example2() => Expect.Returns(-1, () => C02_LargestOfThree.Largest(-1, -7, -3));

        [Fact(DisplayName = "C02 example 3: Largest(4, 4, 2) returns 4")]
        public void Example3() => Expect.Returns(4, () => C02_LargestOfThree.Largest(4, 4, 2));

        [Fact(DisplayName = "C02 example 4: Largest(1, 2, 8) returns 8")]
        public void Example4() => Expect.Returns(8, () => C02_LargestOfThree.Largest(1, 2, 8));
    }
}
