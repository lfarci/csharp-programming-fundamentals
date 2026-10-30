namespace Practice
{
    // D13 · Digital root
    // Exercise page: exercises/D13-digital-root.md
    public static class D13_DigitalRoot
    {
        public static int DigitalRoot(int n)
        {
            while (n >= 10)
            {
                int sum = 0;
                while (n > 0)
                {
                    sum += n % 10;
                    n /= 10;
                }
                n = sum;
            }
            return n;
        }
    }
}
