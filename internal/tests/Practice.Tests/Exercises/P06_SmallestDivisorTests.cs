// Tests for P06 · Smallest divisor
// Exercise page: exercises/P06-smallest-divisor.md
// Your code:     practice/P06_SmallestDivisor.cs
// Run them:      ./ex check P06
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class P06_SmallestDivisorTests
    {
        [Fact(DisplayName = "P06 example 1: SmallestDivisor(15) returns 3")]
        public void Example1() => Expect.Returns(3, () => P06_SmallestDivisor.SmallestDivisor(15));

        [Fact(DisplayName = "P06 example 2: SmallestDivisor(7) returns 7")]
        public void Example2() => Expect.Returns(7, () => P06_SmallestDivisor.SmallestDivisor(7));

        [Fact(DisplayName = "P06 example 3: SmallestDivisor(2) returns 2")]
        public void Example3() => Expect.Returns(2, () => P06_SmallestDivisor.SmallestDivisor(2));

        [Fact(DisplayName = "P06 example 4: SmallestDivisor(49) returns 7")]
        public void Example4() => Expect.Returns(7, () => P06_SmallestDivisor.SmallestDivisor(49));
    }
}
