// Tests for T02 · Remove spaces
// Exercise page: exercises/T02-remove-spaces.md
// Your code:     practice/T02_RemoveSpaces.cs
// Run them:      ./ex check T02
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class T02_RemoveSpacesTests
    {
        [Fact(DisplayName = "T02 example 1: RemoveSpaces(\"a b c\") returns \"abc\"")]
        public void Example1() => Expect.Returns("abc", () => T02_RemoveSpaces.RemoveSpaces("a b c"));

        [Fact(DisplayName = "T02 example 2: RemoveSpaces(\"   \") returns \"\"")]
        public void Example2() => Expect.Returns("", () => T02_RemoveSpaces.RemoveSpaces("   "));

        [Fact(DisplayName = "T02 example 3: RemoveSpaces(\"no-space\") returns \"no-space\"")]
        public void Example3() => Expect.Returns("no-space", () => T02_RemoveSpaces.RemoveSpaces("no-space"));
    }
}
