// Tests for D13 · Digital root
// Exercise page: exercises/D13-digital-root.md
// Your code:     practice/D13_DigitalRoot.cs
// Run them:      ./ex check D13
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class D13_DigitalRootTests
    {
        [Fact(DisplayName = "D13 example 1: DigitalRoot(7) returns 7")]
        public void Example1() => Expect.Returns(7, () => D13_DigitalRoot.DigitalRoot(7));

        [Fact(DisplayName = "D13 example 2: DigitalRoot(38) returns 2")]
        public void Example2() => Expect.Returns(2, () => D13_DigitalRoot.DigitalRoot(38));

        [Fact(DisplayName = "D13 example 3: DigitalRoot(9875) returns 2")]
        public void Example3() => Expect.Returns(2, () => D13_DigitalRoot.DigitalRoot(9875));

        [Fact(DisplayName = "D13 example 4: DigitalRoot(10) returns 1")]
        public void Example4() => Expect.Returns(1, () => D13_DigitalRoot.DigitalRoot(10));

        [Fact(DisplayName = "D13 example 5: DigitalRoot(999) returns 9")]
        public void Example5() => Expect.Returns(9, () => D13_DigitalRoot.DigitalRoot(999));
    }
}
