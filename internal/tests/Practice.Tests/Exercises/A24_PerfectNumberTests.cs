// Tests for A24 · Perfect number
// Exercise page: exercises/A24-perfect-number.md
// Your code:     practice/A24_PerfectNumber.cs
// Run them:      ./ex check A24
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class A24_PerfectNumberTests
    {
        [Fact(DisplayName = "A24 example 1: IsPerfect(6) returns true")]
        public void Example1() => Expect.Returns(true, () => A24_PerfectNumber.IsPerfect(6));

        [Fact(DisplayName = "A24 example 2: IsPerfect(28) returns true")]
        public void Example2() => Expect.Returns(true, () => A24_PerfectNumber.IsPerfect(28));

        [Fact(DisplayName = "A24 example 3: IsPerfect(12) returns false")]
        public void Example3() => Expect.Returns(false, () => A24_PerfectNumber.IsPerfect(12));

        [Fact(DisplayName = "A24 example 4: IsPerfect(1) returns false")]
        public void Example4() => Expect.Returns(false, () => A24_PerfectNumber.IsPerfect(1));

        [Fact(DisplayName = "A24 example 5: IsPerfect(496) returns true")]
        public void Example5() => Expect.Returns(true, () => A24_PerfectNumber.IsPerfect(496));
    }
}
