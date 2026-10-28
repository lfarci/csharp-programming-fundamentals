// ✏️ Your practice space.
// 1. Pick an exercise in exercises/README.md (for example A01).
// 2. Replace the code below with your solution.
// 3. Run it:  dotnet run --project practice
// Keep a copy of solutions you are proud of in practice/done/ (for example done/A01.cs.txt).

Console.Write("N: ");
int n = int.Parse(Console.ReadLine()!);

int sum = 0;
for (int i = 1; i <= n; i++)
{
    sum += i;
}

Console.WriteLine($"Sum: {sum}");
