namespace Practice
{
    // L04 · Multiplication table
    // Exercise page: exercises/L04-multiplication-table.md
    public static class L04_MultiplicationTable
    {
        public static void Run()
        {
            Console.Write("N: ");
            int n = int.Parse(Console.ReadLine()!);

            for (int i = 1; i <= 10; i++)
            {
                Console.WriteLine($"{n} x {i} = {n * i}");
            }
        }
    }
}
