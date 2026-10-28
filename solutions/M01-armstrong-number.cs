// M01 · Armstrong number
// Exercise: exercises/M01-armstrong-number.md
// Run: dotnet run solutions/M01-armstrong-number.cs   (.NET 10+), or paste into practice/Program.cs

Console.Write("N: ");
int n = int.Parse(Console.ReadLine()!);

// 1. count the digits
int digits = 0;
int remaining = n;
do
{
    digits++;
    remaining /= 10;
}
while (remaining > 0);

// 2-4. add digit^digits for every digit
int sum = 0;
remaining = n;
while (remaining > 0)
{
    int digit = remaining % 10;
    int power = 1;
    for (int i = 0; i < digits; i++)
    {
        power *= digit;
    }
    sum += power;
    remaining /= 10;
}

// 5. compare
if (sum == n)
{
    Console.WriteLine($"{n} is an Armstrong number");
}
else
{
    Console.WriteLine($"{n} is not an Armstrong number");
}
