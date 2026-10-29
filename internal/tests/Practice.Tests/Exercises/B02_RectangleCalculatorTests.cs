// Tests for B02 · Rectangle calculator
// Exercise page: exercises/B02-rectangle-calculator.md
// Your code:     practice/B02_RectangleCalculator.cs
// Run them:      ./ex check B02
//
// Generated from internal/tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class B02_RectangleCalculatorTests
    {
        [Fact(DisplayName = "B02 example 1: Area(4, 3) returns 12")]
        public void Example1() => Expect.Returns(12, () => B02_RectangleCalculator.Area(4, 3));

        [Fact(DisplayName = "B02 example 2: Perimeter(4, 3) returns 14")]
        public void Example2() => Expect.Returns(14, () => B02_RectangleCalculator.Perimeter(4, 3));

        [Fact(DisplayName = "B02 example 3: Area(5, 5) returns 25")]
        public void Example3() => Expect.Returns(25, () => B02_RectangleCalculator.Area(5, 5));

        [Fact(DisplayName = "B02 example 4: Perimeter(5, 5) returns 20")]
        public void Example4() => Expect.Returns(20, () => B02_RectangleCalculator.Perimeter(5, 5));

        [Fact(DisplayName = "B02 example 5: Area(0, 7) returns 0")]
        public void Example5() => Expect.Returns(0, () => B02_RectangleCalculator.Area(0, 7));
    }
}
