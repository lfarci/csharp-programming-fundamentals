// Tests for B01 · Hello you
// Exercise page: exercises/B01-hello-you.md
// Your code:     practice/B01_HelloYou.cs
// Run them:      ./ex check B01
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class B01_HelloYouTests
    {
        [Fact(DisplayName = "B01 example 1: input Ada prints \"Hello, Ada!\"")]
        public void Example1() => Expect.Output(
            input: ["Ada"],
            lines: ["Hello, Ada!"],
            run: () => B01_HelloYou.Run());

        [Fact(DisplayName = "B01 example 2: input Sam prints \"Hello, Sam!\"")]
        public void Example2() => Expect.Output(
            input: ["Sam"],
            lines: ["Hello, Sam!"],
            run: () => B01_HelloYou.Run());
    }
}
