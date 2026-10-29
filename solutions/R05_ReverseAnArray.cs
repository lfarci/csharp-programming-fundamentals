namespace Practice
{
    // R05 · Reverse an array
    // Exercise page: exercises/R05-reverse-an-array.md
    public static class R05_ReverseAnArray
    {
        public static int[] Reversed(int[] values)
        {
            int[] reversed = new int[values.Length];
            for (int i = 0; i < values.Length; i++)
            {
                reversed[values.Length - 1 - i] = values[i];
            }
            return reversed;
        }
    }
}
