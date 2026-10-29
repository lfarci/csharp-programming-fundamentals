// Tests for M01 · Armstrong number
// Exercise page: exercises/M01-armstrong-number.md
// Your code:     practice/M01_ArmstrongNumber.cs
// Run them:      ./ex check M01
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class M01_ArmstrongNumberTests
    {
        [Fact(DisplayName = "M01 example 1: IsArmstrong(153) returns true")]
        public void Example1() => Expect.Returns(true, () => M01_ArmstrongNumber.IsArmstrong(153));

        [Fact(DisplayName = "M01 example 2: IsArmstrong(154) returns false")]
        public void Example2() => Expect.Returns(false, () => M01_ArmstrongNumber.IsArmstrong(154));

        [Fact(DisplayName = "M01 example 3: IsArmstrong(9474) returns true")]
        public void Example3() => Expect.Returns(true, () => M01_ArmstrongNumber.IsArmstrong(9474));

        [Fact(DisplayName = "M01 example 4: IsArmstrong(0) returns true")]
        public void Example4() => Expect.Returns(true, () => M01_ArmstrongNumber.IsArmstrong(0));

        [Fact(DisplayName = "M01 example 5: IsArmstrong(10) returns false")]
        public void Example5() => Expect.Returns(false, () => M01_ArmstrongNumber.IsArmstrong(10));

        [Fact(DisplayName = "M01 example 6: IsArmstrong(370) returns true")]
        public void Example6() => Expect.Returns(true, () => M01_ArmstrongNumber.IsArmstrong(370));
    }
}
