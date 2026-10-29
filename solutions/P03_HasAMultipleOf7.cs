namespace Practice
{
    // P03 · Has a multiple of 7
    // Exercise page: exercises/P03-has-a-multiple-of-7.md
    public static class P03_HasAMultipleOf7
    {
        public static bool HasMultipleOf7(int a, int b)
        {
            bool found = false;
            for (int i = a; i <= b; i++)
            {
                if (i % 7 == 0)
                {
                    found = true;
                }
            }
            return found;
        }
    }
}
