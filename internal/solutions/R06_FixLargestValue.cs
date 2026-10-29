namespace Practice
{
    // R06 · Fix: largest value
    // Exercise page: exercises/R06-fix-largest-value.md
    public static class R06_FixLargestValue
    {
        public static int Largest(int[] values)
        {
            int max = values[0];
            for (int i = 1; i < values.Length; i++)
            {
                if (values[i] > max)
                {
                    max = values[i];
                }
            }
            return max;
        }
    }
}
