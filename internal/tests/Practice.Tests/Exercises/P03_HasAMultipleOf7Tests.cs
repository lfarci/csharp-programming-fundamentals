// Tests for P03 · Has a multiple of 7
// Exercise page: exercises/P03-has-a-multiple-of-7.md
// Your code:     practice/P03_HasAMultipleOf7.cs
// Run them:      ./ex check P03
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class P03_HasAMultipleOf7Tests
    {
        [Fact(DisplayName = "P03 example 1: HasMultipleOf7(1, 6) returns false")]
        public void Example1() => Expect.Returns(false, () => P03_HasAMultipleOf7.HasMultipleOf7(1, 6));

        [Fact(DisplayName = "P03 example 2: HasMultipleOf7(1, 7) returns true")]
        public void Example2() => Expect.Returns(true, () => P03_HasAMultipleOf7.HasMultipleOf7(1, 7));

        [Fact(DisplayName = "P03 example 3: HasMultipleOf7(10, 20) returns true")]
        public void Example3() => Expect.Returns(true, () => P03_HasAMultipleOf7.HasMultipleOf7(10, 20));

        [Fact(DisplayName = "P03 example 4: HasMultipleOf7(15, 20) returns false")]
        public void Example4() => Expect.Returns(false, () => P03_HasAMultipleOf7.HasMultipleOf7(15, 20));
    }
}
