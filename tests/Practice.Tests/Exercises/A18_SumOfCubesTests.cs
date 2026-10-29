// Tests for A18 · Sum of cubes
// Exercise page: exercises/A18-sum-of-cubes.md
// Your code:     practice/A18_SumOfCubes.cs
// Run them:      ./ex check A18
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class A18_SumOfCubesTests
    {
        [Fact(DisplayName = "A18 example 1: SumOfCubes(3) returns 36")]
        public void Example1() => Expect.Returns(36, () => A18_SumOfCubes.SumOfCubes(3));

        [Fact(DisplayName = "A18 example 2: SumOfCubes(1) returns 1")]
        public void Example2() => Expect.Returns(1, () => A18_SumOfCubes.SumOfCubes(1));

        [Fact(DisplayName = "A18 example 3: SumOfCubes(4) returns 100")]
        public void Example3() => Expect.Returns(100, () => A18_SumOfCubes.SumOfCubes(4));

        [Fact(DisplayName = "A18 example 4: SumOfCubes(0) returns 0")]
        public void Example4() => Expect.Returns(0, () => A18_SumOfCubes.SumOfCubes(0));
    }
}
