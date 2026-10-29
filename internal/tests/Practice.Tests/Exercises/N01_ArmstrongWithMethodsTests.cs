// Tests for N01 · Armstrong with methods
// Exercise page: exercises/N01-armstrong-with-methods.md
// Your code:     practice/N01_ArmstrongWithMethods.cs
// Run them:      ./ex check N01
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class N01_ArmstrongWithMethodsTests
    {
        [Fact(DisplayName = "N01 example 1: CountDigits(352) returns 3")]
        public void Example1() => Expect.Returns(3, () => N01_ArmstrongWithMethods.CountDigits(352));

        [Fact(DisplayName = "N01 example 2: CountDigits(0) returns 1")]
        public void Example2() => Expect.Returns(1, () => N01_ArmstrongWithMethods.CountDigits(0));

        [Fact(DisplayName = "N01 example 3: Power(3, 4) returns 81")]
        public void Example3() => Expect.Returns(81, () => N01_ArmstrongWithMethods.Power(3, 4));

        [Fact(DisplayName = "N01 example 4: Power(5, 0) returns 1")]
        public void Example4() => Expect.Returns(1, () => N01_ArmstrongWithMethods.Power(5, 0));

        [Fact(DisplayName = "N01 example 5: IsArmstrong(153) returns true")]
        public void Example5() => Expect.Returns(true, () => N01_ArmstrongWithMethods.IsArmstrong(153));

        [Fact(DisplayName = "N01 example 6: IsArmstrong(154) returns false")]
        public void Example6() => Expect.Returns(false, () => N01_ArmstrongWithMethods.IsArmstrong(154));

        [Fact(DisplayName = "N01 example 7: IsArmstrong(9474) returns true")]
        public void Example7() => Expect.Returns(true, () => N01_ArmstrongWithMethods.IsArmstrong(9474));
    }
}
