// Tests for G14 · Numbers in columns
// Exercise page: exercises/G14-numbers-in-columns.md
// Your code:     practice/G14_NumbersInColumns.cs
// Run them:      ./ex check G14
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class G14_NumbersInColumnsTests
    {
        [Fact(DisplayName = "G14 example 1: PrintInColumns(3) prints \"  10  20  30\"")]
        public void Example1() => Expect.Prints("  10  20  30", () => G14_NumbersInColumns.PrintInColumns(3));

        [Fact(DisplayName = "G14 example 2: PrintInColumns(1) prints \"  10\"")]
        public void Example2() => Expect.Prints("  10", () => G14_NumbersInColumns.PrintInColumns(1));

        [Fact(DisplayName = "G14 example 3: PrintInColumns(12) prints \"  10  20  30  40  50  60  70  80  90 100 110 120\"")]
        public void Example3() => Expect.Prints("  10  20  30  40  50  60  70  80  90 100 110 120", () => G14_NumbersInColumns.PrintInColumns(12));
    }
}
