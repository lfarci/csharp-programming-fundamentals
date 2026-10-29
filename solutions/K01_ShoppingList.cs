namespace Practice
{
    // K01 · Shopping list
    // Exercise page: exercises/K01-shopping-list.md
    public static class K01_ShoppingList
    {
        public static void Run()
        {
            List<string> items = new List<string>();
            while (true)
            {
                Console.Write("Item (done to stop): ");
                string item = Console.ReadLine()!;
                if (item == "done")
                {
                    break;
                }
                items.Add(item);
            }

            for (int i = 0; i < items.Count; i++)
            {
                Console.WriteLine($"{i + 1}. {items[i]}");
            }
            Console.WriteLine($"Total: {items.Count} items");
        }
    }
}
