namespace Practice
{
    // S06 · Collatz steps
    // Exercise page: exercises/S06-collatz-steps.md
    public static class S06_CollatzSteps
    {
        public static int CollatzSteps(int n)
        {
            int steps = 0;
            while (n != 1)
            {
                if (n % 2 == 0)
                {
                    n = n / 2;
                }
                else
                {
                    n = 3 * n + 1;
                }
                steps++;
            }
            return steps;
        }
    }
}
