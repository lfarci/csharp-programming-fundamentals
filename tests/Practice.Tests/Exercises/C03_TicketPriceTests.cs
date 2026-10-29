// Tests for C03 · Ticket price
// Exercise page: exercises/C03-ticket-price.md
// Your code:     practice/C03_TicketPrice.cs
// Run them:      ./ex check C03
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class C03_TicketPriceTests
    {
        [Fact(DisplayName = "C03 example 1: Price(11) returns 5")]
        public void Example1() => Expect.Returns(5, () => C03_TicketPrice.Price(11));

        [Fact(DisplayName = "C03 example 2: Price(12) returns 10")]
        public void Example2() => Expect.Returns(10, () => C03_TicketPrice.Price(12));

        [Fact(DisplayName = "C03 example 3: Price(64) returns 10")]
        public void Example3() => Expect.Returns(10, () => C03_TicketPrice.Price(64));

        [Fact(DisplayName = "C03 example 4: Price(65) returns 7")]
        public void Example4() => Expect.Returns(7, () => C03_TicketPrice.Price(65));

        [Fact(DisplayName = "C03 example 5: Price(0) returns 5")]
        public void Example5() => Expect.Returns(5, () => C03_TicketPrice.Price(0));
    }
}
