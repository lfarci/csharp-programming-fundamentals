namespace Practice
{
    // A08 · Multiples of 3 or 5
    // Exercise page: exercises/A08-multiples-of-3-or-5.md
    public static class A08_MultiplesOf3Or5
    {
        public static int SumOfMultiples(int n)
        {
            int sum = 0;
            for (int i = 1; i < n; i++)
            {
                if (i % 3 == 0 || i % 5 == 0)
                {
                    sum += i;
                }
            }
            return sum;
        }
    }
}
