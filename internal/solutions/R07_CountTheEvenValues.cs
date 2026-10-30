namespace Practice
{
    // R07 · Count the even values
    // Exercise page: exercises/R07-count-the-even-values.md
    public static class R07_CountTheEvenValues
    {
        public static int CountEven(int[] values)
        {
            int count = 0;
            for (int i = 0; i < values.Length; i++)
            {
                if (values[i] % 2 == 0)
                {
                    count++;
                }
            }
            return count;
        }
    }
}
