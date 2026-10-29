namespace Practice
{
    // F01 · Save numbers to a file
    // Exercise page: exercises/F01-numbers-file.md
    public static class F01_NumbersFile
    {
        public static void Run()
        {
            string content = "";
            while (true)
            {
                Console.Write("Number (0 to stop): ");
                string text = Console.ReadLine()!;
                if (text == "0")
                {
                    break;
                }
                content += text + "\n";
            }
            File.WriteAllText("numbers.txt", content);

            string[] saved = File.ReadAllLines("numbers.txt");
            int sum = 0;
            foreach (string line in saved)
            {
                sum += int.Parse(line);
            }
            Console.WriteLine($"Lines: {saved.Length}");
            Console.WriteLine($"Sum: {sum}");
        }
    }
}
