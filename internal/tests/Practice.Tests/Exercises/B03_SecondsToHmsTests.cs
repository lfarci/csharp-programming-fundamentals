// Tests for B03 · Seconds to h, min, s
// Exercise page: exercises/B03-seconds-to-hms.md
// Your code:     practice/B03_SecondsToHms.cs
// Run them:      ./ex check B03
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class B03_SecondsToHmsTests
    {
        [Fact(DisplayName = "B03 example 1: Format(3725) returns \"1 h 2 min 5 s\"")]
        public void Example1() => Expect.Returns("1 h 2 min 5 s", () => B03_SecondsToHms.Format(3725));

        [Fact(DisplayName = "B03 example 2: Format(59) returns \"0 h 0 min 59 s\"")]
        public void Example2() => Expect.Returns("0 h 0 min 59 s", () => B03_SecondsToHms.Format(59));

        [Fact(DisplayName = "B03 example 3: Format(7200) returns \"2 h 0 min 0 s\"")]
        public void Example3() => Expect.Returns("2 h 0 min 0 s", () => B03_SecondsToHms.Format(7200));

        [Fact(DisplayName = "B03 example 4: Format(0) returns \"0 h 0 min 0 s\"")]
        public void Example4() => Expect.Returns("0 h 0 min 0 s", () => B03_SecondsToHms.Format(0));
    }
}
