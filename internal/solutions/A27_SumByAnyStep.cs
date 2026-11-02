namespace Practice
{
    // A27 · Sum by any step
    // Exercise page: exercises/A27-sum-by-any-step.md
    public static class A27_SumByAnyStep
    {
        public static int SumByStep(int a, int b, int step)
        {
            int sum = 0;
            for (int i = a; i <= b; i += step)
            {
                sum += i;
            }
            return sum;
        }
    }
}
