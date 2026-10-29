namespace Practice
{
    // P05 · First multiple
    // Exercise page: exercises/P05-first-multiple.md
    public static class P05_FirstMultiple
    {
        public static int FirstMultiple(int a, int b, int k)
        {
            int position = -1;
            for (int i = a; i <= b; i++)
            {
                if (i % k == 0)
                {
                    position = i;
                    break;
                }
            }
            return position;
        }
    }
}
