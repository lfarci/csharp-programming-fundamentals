namespace Practice
{
    // P02 · All primes up to N
    // Exercise page: exercises/P02-primes-up-to-n.md
    public static class P02_PrimesUpToN
    {
        public static void Run()
        {
            Console.Write("N: ");
            int n = int.Parse(Console.ReadLine()!);

            int count = 0;
            for (int candidate = 2; candidate <= n; candidate++)
            {
                bool isPrime = true;               // reset for every candidate
                for (int d = 2; d * d <= candidate; d++)
                {
                    if (candidate % d == 0)
                    {
                        isPrime = false;
                        break;
                    }
                }
                if (isPrime)
                {
                    Console.Write(candidate + " ");
                    count++;
                }
            }
            Console.WriteLine();
            Console.WriteLine($"Count: {count}");
        }
    }
}
