namespace Practice
{
    // L03 · Count up and down
    // Exercise page: exercises/L03-count-up-and-down.md
    public static class L03_CountUpAndDown
    {
        public static void Run()
        {
            Console.Write("N: ");
            int n = int.Parse(Console.ReadLine()!);

            for (int i = 1; i <= n; i++)
            {
                Console.Write(i + " ");
            }
            Console.WriteLine();

            for (int i = n; i >= 1; i--)
            {
                Console.Write(i + " ");
            }
            Console.WriteLine();
        }
    }
}
