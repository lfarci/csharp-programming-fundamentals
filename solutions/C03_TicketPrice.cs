namespace Practice
{
    // C03 · Ticket price
    // Exercise page: exercises/C03-ticket-price.md
    public static class C03_TicketPrice
    {
        public static int Price(int age)
        {
            if (age < 12)
            {
                return 5;
            }
            else if (age >= 65)
            {
                return 7;
            }
            else
            {
                return 10;
            }
        }
    }
}
