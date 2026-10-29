namespace Practice
{
    // L06 · Even numbers
    // Exercise page: exercises/L06-even-numbers.md
    public static class L06_EvenNumbers
    {
        public static void Run()
        {
            Console.Write("N: ");
            int n = int.Parse(Console.ReadLine()!);

            // Way 1: jump by 2
            for (int i = 2; i <= n; i += 2)
            {
                Console.Write(i + " ");
            }
            Console.WriteLine();

            // Way 2 (same output): visit every number, keep the even ones
            // for (int i = 1; i <= n; i++)
            // {
            //     if (i % 2 == 0) Console.Write(i + " ");
            // }
        }
    }
}
