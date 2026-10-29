namespace Practice
{
    // L07 · Ask until valid
    // Exercise page: exercises/L07-ask-until-valid.md
    public static class L07_AskUntilValid
    {
        public static void Run()
        {
            int number;
            bool valid;
            do
            {
                Console.Write("Number between 1 and 10: ");
                string? text = Console.ReadLine();
                valid = int.TryParse(text, out number) && number >= 1 && number <= 10;
                if (!valid)
                {
                    Console.WriteLine("Invalid, try again.");
                }
            }
            while (!valid);

            Console.WriteLine($"You chose {number}");
        }
    }
}
