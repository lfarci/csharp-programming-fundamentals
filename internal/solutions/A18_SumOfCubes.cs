namespace Practice
{
    // A18 · Sum of cubes
    // Exercise page: exercises/A18-sum-of-cubes.md
    public static class A18_SumOfCubes
    {
        public static int SumOfCubes(int n)
        {
            int sum = 0;
            for (int i = 1; i <= n; i++)
            {
                sum += i * i * i;
            }
            return sum;
        }
    }
}
