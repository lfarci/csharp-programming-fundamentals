namespace Practice
{
    // A31 · Double k times
    // Exercise page: exercises/A31-double-k-times.md
    public static class A31_DoubleKTimes
    {
        public static long DoubleTimes(int start, int times)
        {
            long result = start;
            for (int i = 1; i <= times; i++)
            {
                result *= 2;
            }
            return result;
        }
    }
}
