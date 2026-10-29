namespace Practice
{
    // B01 · Hello you
    // Exercise page: exercises/B01-hello-you.md
    public static class B01_HelloYou
    {
        public static void Run()
        {
            Console.Write("What is your name? ");
            string name = Console.ReadLine()!;
            Console.WriteLine($"Hello, {name}!");
        }
    }
}
