namespace Practice
{
    // S04 · Doubling
    // Exercise page: exercises/S04-doubling.md
    public static class S04_Doubling
    {
        public static void PrintDoubling(int start, int count)
        {
            int value = start;
            for (int i = 1; i <= count; i++)
            {
                Console.WriteLine(value);
                value = value * 2;
            }
        }
    }
}
