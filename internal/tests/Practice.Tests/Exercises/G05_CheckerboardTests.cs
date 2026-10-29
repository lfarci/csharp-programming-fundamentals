// Tests for G05 · Checkerboard
// Exercise page: exercises/G05-checkerboard.md
// Your code:     practice/G05_Checkerboard.cs
// Run them:      ./ex check G05
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class G05_CheckerboardTests
    {
        [Fact(DisplayName = "G05 example 1: DrawCheckerboard(4) prints 4 lines")]
        public void Example1() => Expect.Prints(
            """
            #.#.
            .#.#
            #.#.
            .#.#
            """, () => G05_Checkerboard.DrawCheckerboard(4));

        [Fact(DisplayName = "G05 example 2: DrawCheckerboard(1) prints \"#\"")]
        public void Example2() => Expect.Prints("#", () => G05_Checkerboard.DrawCheckerboard(1));
    }
}
