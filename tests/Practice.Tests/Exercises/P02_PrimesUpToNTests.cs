// Tests for P02 · All primes up to N
// Exercise page: exercises/P02-primes-up-to-n.md
// Your code:     practice/P02_PrimesUpToN.cs
// Run them:      ./ex check P02
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class P02_PrimesUpToNTests
    {
        [Fact(DisplayName = "P02 example 1: input 20 prints \"Count: 8\"")]
        public void Example1() => Expect.Output(
            input: ["20"],
            lines: ["2 3 5 7 11 13 17 19", "Count: 8"],
            run: () => P02_PrimesUpToN.Run());

        [Fact(DisplayName = "P02 example 2: input 2 prints \"Count: 1\"")]
        public void Example2() => Expect.Output(
            input: ["2"],
            lines: ["2", "Count: 1"],
            run: () => P02_PrimesUpToN.Run());

        [Fact(DisplayName = "P02 example 3: input 1 prints \"Count: 0\"")]
        public void Example3() => Expect.Output(
            input: ["1"],
            lines: ["Count: 0"],
            run: () => P02_PrimesUpToN.Run());
    }
}
