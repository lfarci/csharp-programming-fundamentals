// Tests for A34 · Sum of a times table
// Exercise page: exercises/A34-sum-of-a-times-table.md
// Your code:     practice/A34_SumOfATimesTable.cs
// Run them:      ./ex check A34
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class A34_SumOfATimesTableTests
    {
        [Fact(DisplayName = "A34 example 1: SumOfTable(3, 10) returns 165")]
        public void Example1() => Expect.Returns(165, () => A34_SumOfATimesTable.SumOfTable(3, 10));

        [Fact(DisplayName = "A34 example 2: SumOfTable(10, 3) returns 60")]
        public void Example2() => Expect.Returns(60, () => A34_SumOfATimesTable.SumOfTable(10, 3));

        [Fact(DisplayName = "A34 example 3: SumOfTable(4, 1) returns 4")]
        public void Example3() => Expect.Returns(4, () => A34_SumOfATimesTable.SumOfTable(4, 1));

        [Fact(DisplayName = "A34 example 4: SumOfTable(5, 0) returns 0")]
        public void Example4() => Expect.Returns(0, () => A34_SumOfATimesTable.SumOfTable(5, 0));
    }
}
