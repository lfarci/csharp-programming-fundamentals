namespace Practice
{
    // A23 · FizzBuzz
    // Exercise page: exercises/A23-fizzbuzz.md
    public static class A23_Fizzbuzz
    {
        public static void PrintFizzBuzz(int n)
        {
            for (int i = 1; i <= n; i++)
            {
                if (i % 15 == 0)
                {
                    Console.WriteLine("FizzBuzz");
                }
                else if (i % 3 == 0)
                {
                    Console.WriteLine("Fizz");
                }
                else if (i % 5 == 0)
                {
                    Console.WriteLine("Buzz");
                }
                else
                {
                    Console.WriteLine(i);
                }
            }
        }
    }
}
