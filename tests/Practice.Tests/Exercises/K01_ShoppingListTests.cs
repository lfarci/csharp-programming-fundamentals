// Tests for K01 · Shopping list
// Exercise page: exercises/K01-shopping-list.md
// Your code:     practice/K01_ShoppingList.cs
// Run them:      ./ex check K01
//
// Generated from tools/generator (edit the exercise there, not here).
namespace Practice.Tests
{
    public class K01_ShoppingListTests
    {
        [Fact(DisplayName = "K01 example 1: input milk, eggs, bread, done prints \"Total: 3 items\"")]
        public void Example1() => Expect.Output(
            input: ["milk", "eggs", "bread", "done"],
            lines: ["1. milk", "2. eggs", "3. bread", "Total: 3 items"],
            run: () => K01_ShoppingList.Run());

        [Fact(DisplayName = "K01 example 2: input done prints \"Total: 0 items\"")]
        public void Example2() => Expect.Output(
            input: ["done"],
            lines: ["Total: 0 items"],
            run: () => K01_ShoppingList.Run());
    }
}
