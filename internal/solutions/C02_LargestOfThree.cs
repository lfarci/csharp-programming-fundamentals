namespace Practice
{
    // C02 · Largest of three
    // Exercise page: exercises/C02-largest-of-three.md
    public static class C02_LargestOfThree
    {
        public static int Largest(int a, int b, int c)
        {
            int largest = a;
            if (b > largest)
            {
                largest = b;
            }
            if (c > largest)
            {
                largest = c;
            }
            return largest;
        }
    }
}
