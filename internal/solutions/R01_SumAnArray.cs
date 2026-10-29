namespace Practice
{
    // R01 · Sum of an array
    // Exercise page: exercises/R01-sum-an-array.md
    public static class R01_SumAnArray
    {
        public static int Sum(int[] values)
        {
            int sum = 0;
            foreach (int value in values)
            {
                sum += value;
            }
            return sum;
        }
    }
}
