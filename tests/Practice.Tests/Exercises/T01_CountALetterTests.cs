// Tests for T01 · Count a letter
// Exercise page: exercises/T01-count-a-letter.md
// Your code:     practice/T01_CountALetter.cs
// Run them:      ./ex check T01
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class T01_CountALetterTests
    {
        [Fact(DisplayName = "T01 example 1: CountLetter(\"banana\", 'a') returns 3")]
        public void Example1() => Expect.Returns(3, () => T01_CountALetter.CountLetter("banana", 'a'));

        [Fact(DisplayName = "T01 example 2: CountLetter(\"BANANA\", 'a') returns 0")]
        public void Example2() => Expect.Returns(0, () => T01_CountALetter.CountLetter("BANANA", 'a'));

        [Fact(DisplayName = "T01 example 3: CountLetter(\"\", 'a') returns 0")]
        public void Example3() => Expect.Returns(0, () => T01_CountALetter.CountLetter("", 'a'));
    }
}
