namespace Practice
{
    // R02 · Position of the largest
    // Exercise page: exercises/R02-largest-in-an-array.md
    public static class R02_LargestInAnArray
    {
        public static int IndexOfLargest(int[] values)
        {
            int maxIndex = 0;
            for (int i = 1; i < values.Length; i++)
            {
                if (values[i] > values[maxIndex])
                {
                    maxIndex = i;
                }
            }
            return maxIndex;
        }
    }
}
