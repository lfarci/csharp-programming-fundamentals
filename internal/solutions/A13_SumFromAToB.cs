namespace Practice
{
    // A13 · Sum from a to b
    // Exercise page: exercises/A13-sum-from-a-to-b.md
    public static class A13_SumFromAToB
    {
        public static int SumFromTo(int a, int b)
        {
            int sum = 0;
            for (int i = a; i <= b; i++)
            {
                sum += i;
            }
            return sum;
        }
    }
}
