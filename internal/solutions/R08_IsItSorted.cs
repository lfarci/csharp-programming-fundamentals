namespace Practice
{
    // R08 · Is it sorted?
    // Exercise page: exercises/R08-is-it-sorted.md
    public static class R08_IsItSorted
    {
        public static bool IsSorted(int[] values)
        {
            for (int i = 1; i < values.Length; i++)
            {
                if (values[i] < values[i - 1])
                {
                    return false;
                }
            }
            return true;
        }
    }
}
