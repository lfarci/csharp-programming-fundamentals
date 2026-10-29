namespace Practice
{
    // B03 · Seconds to hours, minutes, seconds
    // Exercise page: exercises/B03-seconds-to-hms.md
    public static class B03_SecondsToHms
    {
        public static string Format(int totalSeconds)
        {
            int hours = totalSeconds / 3600;
            int rest = totalSeconds % 3600;
            int minutes = rest / 60;
            int seconds = rest % 60;
            return $"{hours} h {minutes} min {seconds} s";
        }
    }
}
