// Tests for B01 · Hello you
// Exercise page: exercises/B01-hello-you.md
// Your code:     practice/B01_HelloYou.cs
// Run them:      ./ex check B01
//
// Generated from internal/tools/generator (edit the exercise there, not here).
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

        [Fact(DisplayName = "B01 example 3: edge case, input (empty) prints \"Hello, !\"")]
        public void Edge1() => Expect.Output(
            input: [""],
            lines: ["Hello, !"],
            run: () => B01_HelloYou.Run(), hint: "an empty name is still a name: print the greeting around it.");
    }
}
