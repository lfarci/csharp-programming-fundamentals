// Tests for A07 · Integer power
// Exercise page: exercises/A07-integer-power.md
// Your code:     practice/A07_IntegerPower.cs
// Run them:      ./ex check A07
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class A07_IntegerPowerTests
    {
        [Fact(DisplayName = "A07 example 1: Power(3, 4) returns 81")]
        public void Example1() => Expect.Returns(81L, () => A07_IntegerPower.Power(3, 4));

        [Fact(DisplayName = "A07 example 2: Power(2, 10) returns 1024")]
        public void Example2() => Expect.Returns(1024L, () => A07_IntegerPower.Power(2, 10));

        [Fact(DisplayName = "A07 example 3: Power(5, 0) returns 1")]
        public void Example3() => Expect.Returns(1L, () => A07_IntegerPower.Power(5, 0));

        [Fact(DisplayName = "A07 example 4: Power(-2, 3) returns -8")]
        public void Example4() => Expect.Returns(-8L, () => A07_IntegerPower.Power(-2, 3));

        [Fact(DisplayName = "A07 example 5: edge case, Power(0, 3) returns 0")]
        public void Edge1() => Expect.Returns(0L, () => A07_IntegerPower.Power(0, 3), hint: "0 times anything is 0: the box starts at 1 and is multiplied by 0.");

        [Fact(DisplayName = "A07 example 6: edge case, Power(0, 0) returns 1")]
        public void Edge2() => Expect.Returns(1L, () => A07_IntegerPower.Power(0, 0), hint: "exponent 0: the loop runs 0 times, so the box keeps its start value 1.");
    }
}
