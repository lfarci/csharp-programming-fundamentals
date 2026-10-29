namespace Practice
{
    // L15 · Count by any step
    // Exercise page: exercises/L15-count-by-step.md
    public static class L15_CountByStep
    {
        public static void CountByStep(int step, int n)
        {
            for (int i = step; i <= n; i += step)
            {
                Console.WriteLine(i);
            }
        }
    }
}
