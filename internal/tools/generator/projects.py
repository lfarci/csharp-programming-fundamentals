"""Projects: small programs of your own, no tests, no answer key. Original text, written for this course.
Ideas are classic beginner console programs (folk games and everyday problems); for more inspiration the
overview links the official dotnet/dotnet-console-games repo. Never copy from the C# Player's Guide.

Each project: (slug, title, group, level, effort, themes, pitch, intro, sample, learn, prep, milestones, stretch, hints).
Everything in the milestones uses only course concepts (console I/O, if, loops, arrays, lists, methods, Random);
anything else is a stretch goal with a Microsoft Learn link.
"""
import glob, os
ML = "https://learn.microsoft.com/en-us/dotnet"
DOC = {"color": f"[`Console.ForegroundColor`]({ML}/api/system.console.foregroundcolor)",
       "clear": f"[`Console.Clear()`]({ML}/api/system.console.clear)",
       "sleep": f"[`Thread.Sleep`]({ML}/api/system.threading.thread.sleep)",
       "readkey": f"[`Console.ReadKey`]({ML}/api/system.console.readkey)",
       "file": f"[`File.WriteAllLines`]({ML}/api/system.io.file.writealllines)",
       "random": f"[`Random`]({ML}/api/system.random)",
       "array2d": f"[2D arrays]({ML}/csharp/language-reference/builtin-types/arrays#multidimensional-arrays)",
       "switch": f"[`switch`]({ML}/csharp/language-reference/statements/selection-statements#the-switch-statement)",
       "datetime": f"[`DateTime`]({ML}/api/system.datetime)",
       "format": f"[number formats]({ML}/standard/base-types/standard-numeric-format-strings)"}
GROUPS = [("games", "Terminal games", "Play them, beat your friends, then make them harder."),
          ("real", "Learn something real", "Small tools that teach you a real-world idea while you code."),
          ("fun", "Just for fun", "Stories, quizzes and surprises: the program talks back.")]
THEMES = {"basics": "Basics", "loops": "Loops", "arrays": "Arrays, text and lists", "methods": "Methods and errors"}

P = [
("guessing-game", "Guessing game", "games", "Easy", "1 to 2 hours", ["basics", "loops", "methods"],
 "The computer hides a number. Hot or cold? Find it in as few tries as you can.",
 "The computer thinks of a number from 1 to 100 and dares you to find it. Every guess gets an answer: higher, lower, and with the stretch goals, *hot* or *freezing*. Then you turn the tables and make the computer guess **your** number.",
 """=== GUESS MY NUMBER ===
I picked a number from 1 to 100. You have 7 tries.
Try 1: 50
Too high! (warm)
Try 2: banana
That is not a number. Bananas do not count.
Try 2: 25
Too low! (hot!)
Try 3: 31
*** YOU GOT IT in 3 tries! New best score! ***
Play again? (y/n) n
Best this session: 3 tries. Bye!""",
 ["repeat until something happens with a `while` loop", "count tries and keep a best score", "read numbers safely with `int.TryParse`", "pick random numbers with `Random.Shared.Next`"],
 ["L07", "L08", "E01"],
 ["**Fixed secret.** The secret is 42. Read one guess and print `Too high!`, `Too low!` or `You got it!`.",
  "**Loop.** Keep asking until the guess is right. Count the tries and print them.",
  "**Random secret.** `Random.Shared.Next(1, 101)` gives 1 to 100 (the 101 is not included).",
  "**Safe input.** Text or an empty line does not crash and does not count as a try.",
  "**Limited tries.** 7 tries at most. When they run out, reveal the number.",
  "**Play again.** Ask `Play again? (y/n)` and keep the best score of the session."],
 ["**Hot or cold:** print `hot!` when the guess is within 5 of the secret, `warm` within 15, `freezing` otherwise.",
  "**Difficulty levels:** easy (1 to 50, 10 tries), normal, hard (1 to 1000, 10 tries).",
  "**Reverse mode:** you think of a number and the computer guesses it by halving the range. Can it always win in 10 tries for 1 to 1000? Why?",
  "**Colours:** green for a win, red for too high, blue for too low, with " + DOC["color"] + ".",
  "**High score file:** save the best score in `best.txt` so it survives a restart (" + DOC["file"] + ")."],
 [("Which loop?", "You do not know how many guesses are needed: a `while` loop whose test is \"not found yet and tries left\". See the [sentinel loop](../cookbook/10-sentinel-loop.md) recipe."),
  ("Not counting bad input", "`if (!int.TryParse(text, out int guess)) { ...; continue; }` jumps back to the top before `tries++`."),
  ("The best score", "Start it at `int.MaxValue`; after a win, `if (tries < best) best = tries;`. That is the [min/max](../cookbook/04-min-max.md) recipe."),
  ("Reverse mode", "Keep `low` and `high`. The computer guesses `(low + high) / 2`; on `higher` set `low = guess + 1`, on `lower` set `high = guess - 1`.")]),

("hangman", "Hangman", "games", "Medium", "3 to 4 hours", ["loops", "arrays", "methods"],
 "Guess the secret word letter by letter before the little man is drawn.",
 "A secret word, a row of underscores and a gallows that grows with every wrong letter. Hangman is the perfect game for working on text letter by letter, and the ASCII drawing is half the fun.",
 """  +---+
  |   |
  O   |
 /|   |
      |
=========
Word:   _ O _ _ _ A M
Missed: E, I, U  (3 of 6)
Your letter: r
Yes! R is in the word.
Word:   _ R O _ R A M
Your letter: p
Word:   P R O _ R A M
Your letter: g
Word:   P R O G R A M
*** You saved him! The word was PROGRAM. ***""",
 ["walk through a string letter by letter", "keep the found letters in a `bool[]` or a `char[]`", "use a list for the letters already tried", "split a game into small methods"],
 ["T01", "R03", "R04", "K01"],
 ["**One word, one letter.** The word is `PROGRAM`. Read one letter and say if it is in the word.",
  "**Show the progress.** Print the word with `_` for the letters not found yet, like `_ R O _ R A M`.",
  "**The game loop.** Repeat until every letter is found or 6 wrong letters were given.",
  "**Already tried.** Keep a `List<char>` of tried letters; refuse the same letter twice and ignore upper/lower case.",
  "**Random word.** Pick the word from an array of at least 10 words with `Random.Shared.Next`.",
  "**The drawing.** Print the gallows with one more body part for each mistake: 7 small drawings in a `string[]`."],
 ["**Categories:** animals, countries, programming words. The player picks one, the hint shows it.",
  "**Two players:** player 1 types the word (then " + DOC["clear"] + " hides it), player 2 guesses.",
  "**Words from a file:** read `words.txt` with `File.ReadAllLines` so anyone can add words.",
  "**Score:** points for each found letter, a bonus for each unused life; keep a high score.",
  "**Colours:** found letters in green, missed ones in red (" + DOC["color"] + ")."],
 [("Showing the word", "Loop over the word: for each letter, print it if it was found, `_` otherwise. A `bool[] found` with the same length as the word remembers which positions are found."),
  ("Is the game won?", "A flag: `bool allFound = true;` then one loop, `if (!found[i]) allFound = false;`. That is the [flag/search](../cookbook/05-flag-search.md) recipe."),
  ("Upper and lower case", "`char.ToUpper(letter)` before comparing, and keep the words in capitals."),
  ("The drawing", "`string[] stages = { \"...\", \"...\" };` with 7 multi-line strings (use `\\n` or a raw string `\"\"\"`). Print `stages[mistakes]`.")]),

("rock-paper-scissors-lizard-spock", "Rock paper scissors+", "games", "Easy", "2 to 3 hours", ["basics", "loops", "methods"],
 "The classic game, then the 5-weapon version where Spock vaporizes rock.",
 "Start with rock, paper, scissors against the computer, best of 5. Then add two more weapons, lizard and Spock: now there are 25 possible duels and a big `if` chain gets messy. Time to think about a better way to decide who wins.",
 """ROCK PAPER SCISSORS LIZARD SPOCK - best of 5
Your move (r, p, s, l, k): k
You: SPOCK   Computer: ROCK
Spock vaporizes rock. You win this round!
Score: you 1 - 0 computer
Your move (r, p, s, l, k): l
You: LIZARD  Computer: SCISSORS
Scissors decapitate lizard. Computer wins this round.
Score: you 1 - 1 computer
...
*** You win the match 3 - 2! ***""",
 ["turn the user's choice into a number and back into a name", "decide a winner with conditions, then with a table", "count rounds and scores", "write methods that give back a value"],
 ["C02", "C03", "N02"],
 ["**One round.** Read `r`, `p` or `s`; the computer picks at random; print both moves and who wins.",
  "**Refuse bad input.** Anything else: `Please type r, p or s.` and ask again.",
  "**Best of 5.** Keep the score; stop when someone reaches 3 wins (draws do not count).",
  "**Methods.** `string Name(int move)` and `int Winner(int a, int b)` (1, 2 or 0 for a draw).",
  "**Lizard and Spock.** Add the two weapons: scissors cut paper, paper covers rock, rock crushes lizard, lizard poisons Spock, Spock smashes scissors, scissors decapitate lizard, lizard eats paper, paper disproves Spock, Spock vaporizes rock, rock crushes scissors.",
  "**The funny line.** Print the right sentence for each win: `Paper disproves Spock.`"],
 ["**The clever trick:** number the weapons 0 to 4 in the order rock, Spock, paper, lizard, scissors. Then `(5 + a - b) % 5` is 1 or 2 when `a` wins, 3 or 4 when `b` wins. Why does it work?",
  "**A computer that learns:** count which move the player uses most, and play what beats it.",
  "**Statistics:** at the end, print how often the player used each weapon, as an ASCII bar chart.",
  "**Suspense:** print `Rock... paper... scissors...` with a pause (" + DOC["sleep"] + ").",
  "**Colours:** the winner of each round in green (" + DOC["color"] + ")."],
 [("Moves as numbers", "Store the move as an `int` (0 = rock, 1 = paper, 2 = scissors). A `string[] names = { \"ROCK\", \"PAPER\", \"SCISSORS\" };` turns it back into text."),
  ("Who wins with 3 weapons", "With 0, 1, 2 in that order, each move beats the one before it: `a` wins when `(a - b + 3) % 3 == 1`."),
  ("Who wins with 5 weapons", "A table: `bool[,] beats` or, simpler, a `string[]` of 10 lines like `\"PAPER DISPROVES SPOCK\"`. Look for the line that starts with your move and ends with the computer's."),
  ("Best of 5", "`while (you < 3 && computer < 3)`: two counters, an `if` after each round.")]),

("pig-dice", "Pig dice duel", "games", "Medium", "2 to 3 hours", ["loops", "methods"],
 "Roll again or bank your points? One 1 and you lose the whole turn.",
 "Pig is an old folk dice game with a single cruel rule: roll as often as you like and add up the dice, but if you roll a 1 your turn's points are gone. First to 100 wins. It is a game about greed, chance and, later, strategy.",
 """=== PIG === first to 100 wins
You: 0   Computer: 0
You roll... 5   (turn: 5)   Roll again? (y/n) y
You roll... 6   (turn: 11)  Roll again? (y/n) y
You roll... 4   (turn: 15)  Roll again? (y/n) n
You bank 15. You: 15
Computer rolls... 3, 6, 2, 1  -> PIG! It loses 11 points.
You roll... 1  -> PIG! Turn over.
Computer rolls... 6, 5, 4, 6  and banks 21. Computer: 21
...
*** You win 102 to 87! ***""",
 ["simulate dice with `Random`", "nest a turn loop inside a game loop", "update several variables in the right order", "write a simple computer strategy"],
 ["S04", "A06", "L08"],
 ["**One roll.** Print a random number from 1 to 6, many times, to check that 1 and 6 both appear.",
  "**One turn.** Roll, add to the turn total, ask `Roll again?`. A 1 ends the turn with 0 points.",
  "**Bank.** Saying `n` adds the turn total to your score.",
  "**The game.** Repeat turns until someone reaches 100. Print both scores after each turn.",
  "**The computer.** Its strategy: keep rolling until its turn total is 20 or more, then bank.",
  "**Polish.** Show every die of the computer's turn on one line, and announce the winner in style."],
 ["**Two dice:** a 1 loses the turn; double 1 loses the **whole score**.",
  "**Smarter computer:** if it is far behind, it takes more risks (banks at 30).",
  "**Simulation:** make two computer players with different limits (15, 20, 25) play 10 000 games without printing. Which limit wins most? You just did science.",
  "**ASCII dice:** draw each die as a 3x3 box of dots.",
  "**More players:** 2 to 4 humans, names in a `List<string>`, scores in a `List<int>`."],
 [("A die", "`int die = Random.Shared.Next(1, 7);` gives 1 to 6."),
  ("Two loops", "The outer loop runs while nobody has 100. Inside, one turn is another loop that runs until the player stops or rolls a 1."),
  ("Two players, one code", "Write `int PlayHumanTurn()` and `int PlayComputerTurn()`; both give back the points to bank (0 after a 1)."),
  ("The simulation", "Turn the computer turn into a method with the limit as a parameter, then call it in a `for` loop 10 000 times and count wins.")]),

("tic-tac-toe", "Tic-tac-toe", "games", "Hard", "4 to 6 hours", ["loops", "arrays", "methods"],
 "X against O on a 3x3 grid, then against a computer that never loses.",
 "Everyone knows the game, and that is exactly why it is a great project: you know what *correct* looks like. Draw the grid, take turns, detect a win or a draw, then teach the computer to block you.",
 """ X | 2 | 3
---+---+---
 4 | X | 6
---+---+---
 O | 8 | 9
X, your square (1-9): 5
Square 5 is taken. Try again.
X, your square (1-9): 9
 X | 2 | 3
---+---+---
 4 | X | 6
---+---+---
 O | 8 | X
*** X WINS (1, 5, 9)! *** Score: X 1 - O 0 - draws 0""",
 ["keep a board in an array of 9 cells", "draw a grid with loops", "check 8 winning lines with a loop over a table", "write a computer move from simple rules"],
 ["G01", "R04", "P03", "N01"],
 ["**The board.** A `char[] board` of 9 cells with `'1'` to `'9'`. Print it as a 3x3 grid.",
  "**One move.** Read a square from 1 to 9, put an `X` there. Refuse a number outside 1 to 9 or a square already taken.",
  "**Take turns.** Switch between `X` and `O` after each move, for two human players.",
  "**Winner.** After each move, check the 8 lines (3 rows, 3 columns, 2 diagonals). Stop on a win.",
  "**Draw.** 9 moves and no winner: it is a draw.",
  "**The computer.** O plays a random free square.",
  "**A smarter computer.** O wins if it can, otherwise blocks X if X could win, otherwise takes the centre, otherwise random."],
 ["**Score across games:** wins, losses and draws, and who starts alternates.",
  "**A real grid:** use a " + DOC["array2d"] + " `char[3, 3]` instead of 9 cells.",
  "**Bigger board:** 4x4, 4 in a row. What has to change in your code?",
  "**Colours:** X in blue, O in red (" + DOC["color"] + "), and " + DOC["clear"] + " before each new board.",
  "**Unbeatable:** look up the *minimax* idea and make a computer that never loses (this one is hard: recursion)."],
 [("The 8 lines", "Write them once: `int[] lines = { 0,1,2, 3,4,5, 6,7,8, 0,3,6, 1,4,7, 2,5,8, 0,4,8, 2,4,6 };`. Line `k` is `lines[3*k]`, `lines[3*k+1]`, `lines[3*k+2]`."),
  ("Who won?", "`char Winner(char[] board)`: for each line, if the 3 cells are equal, give back that cell; after the loop give back `' '`. That is the [flag/search](../cookbook/05-flag-search.md) recipe."),
  ("Win or block", "Try each free square: put `O` there, ask `Winner`, then put the number back. If `O` wins, play it. Do the same with `X` to find the square to block."),
  ("Drawing the grid", "A loop over the 3 rows; inside, the 3 cells of the row joined by ` | `; between rows, `---+---+---`.")]),

("weather-station", "Weather station", "real", "Medium", "3 to 4 hours", ["loops", "arrays", "methods"],
 "Turn a week of temperatures into stats, trends and an ASCII chart, like a meteorologist.",
 "Meteorologists do not just read a thermometer: they look for the minimum, the maximum, the average, the warmest day and the trend. Type a week of temperatures (or read them from a file) and your program writes the weather report.",
 """Temperature for Monday (°C): 12
Temperature for Tuesday (°C): 15
...
Temperature for Sunday (°C): 8

        WEEKLY WEATHER REPORT
Mon  12 °C | ############
Tue  15 °C | ###############
Wed  17 °C | ################# <- warmest
Thu  14 °C | ##############
Fri   9 °C | #########
Sat   7 °C | ####### <- coldest
Sun   8 °C | ########
Average 11.7 °C, range 10 degrees.
Biggest change: Thu -> Fri, 5 degrees colder.
Trend: getting colder. Take a coat this weekend!""",
 ["min, max and average: the core of statistics", "the range and the biggest day-to-day change", "a bar chart made of characters", "what an average hides (and why weather reports give min and max too)"],
 ["A06", "A09", "R01", "R02", "G09"],
 ["**Read the week.** 7 temperatures (whole degrees) into an `int[]`, with the day names in a `string[]`.",
  "**Min, max, average.** One loop for each, or one loop for all three. Print the average with 1 decimal.",
  "**Which day?** Not only the coldest temperature but the **day** it was: keep the index.",
  "**The chart.** One line per day with one `#` per degree. Mark the warmest and coldest days.",
  "**Change.** Find the biggest change between two days in a row and say if it got warmer or colder.",
  "**Trend.** Compare the average of the first 3 days with the last 3 days: getting warmer, colder or stable. Finish with an advice line."],
 ["**Negative degrees:** the chart cannot draw `-3` hashes. Shift the chart so the coldest day starts at 0, or draw `-` signs to the left of a middle line.",
  "**A month from a file:** read `temperatures.txt` (one number per line) with `File.ReadAllLines` and handle any number of days.",
  "**Celsius and Fahrenheit:** add a switch: F = C × 9 / 5 + 32. Print both in the report.",
  "**Heat wave alert:** 3 days or more in a row above 25 °C. Count the longest run.",
  "**Colours:** cold bars in blue, warm bars in red (" + DOC["color"] + ")."],
 [("The average with decimals", "Add up in an `int`, then divide as a `double`: `double average = (double)sum / days.Length;`, printed with `{average:0.0}`."),
  ("The warmest day", "Keep the index, not the value: `int warmest = 0;` and in the loop `if (t[i] > t[warmest]) warmest = i;`. Same as [R02](../exercises/R02-largest-in-an-array.md)."),
  ("Biggest change", "Compare neighbours: loop from `i = 1` and look at `t[i] - t[i - 1]`. Keep the biggest absolute value (`Math.Abs`)."),
  ("The bars", "`new string('#', t[i])` makes a row of `#`, or write an inner loop like in [G09](../exercises/G09-number-rows.md).")]),

("dress-for-the-weather", "What should I wear?", "real", "Easy", "1 to 2 hours", ["basics", "loops", "methods"],
 "Convert temperatures, feel the wind chill and get outfit advice from your own program.",
 "Is 50 °F warm? What does 5 °C *feel* like with a strong wind? Build a little assistant that converts temperatures, computes the wind chill the way weather services do, and tells you what to wear.",
 """=== WHAT SHOULD I WEAR? ===
Temperature: 41
Unit (C or F): F
41 °F is 5.0 °C.
Wind speed (km/h): 30
With the wind it feels like 0.1 °C. Brrr.
Rain? (y/n) y

Your outfit:
 - winter coat and scarf
 - gloves (it feels like 0!)
 - umbrella or rain jacket
Convert another? (y/n) n""",
 ["the Celsius and Fahrenheit scales and the formula between them", "the wind chill: why wind makes cold feel colder", "choosing among ranges with `if` / `else if`", "methods that compute a `double`"],
 ["B02", "C03", "C04", "L07"],
 ["**C to F.** Read a temperature in °C and print it in °F: F = C × 9 / 5 + 32.",
  "**Both ways.** Ask for the unit (`C` or `F`) and convert in the right direction; refuse anything else.",
  "**Methods.** `double ToFahrenheit(double c)` and `double ToCelsius(double f)`. Check: 100 °C is 212 °F, -40 is the same in both.",
  "**Outfit.** From the temperature in °C: below 0, 0 to 10, 10 to 18, 18 to 25, above 25. One piece of advice per range.",
  "**Wind chill.** Ask the wind speed and compute the *feels like* temperature (formula in the hints). Base the outfit on it.",
  "**Rain and repeat.** Add the rain question, then a loop: `Convert another?`."],
 ["**Conversion table:** print -20 to 40 °C in steps of 5 next to °F, as a neat table (" + DOC["format"] + ").",
  "**Kelvin:** add the scale scientists use (K = C + 273.15) and refuse temperatures below absolute zero.",
  "**Heat index:** for hot days, humidity makes heat feel worse. Look up the simple heat index formula and add it.",
  "**A week of outfits:** read 7 days and plan the week, then count how many days need an umbrella.",
  "**Colours:** blue advice when cold, orange when hot (" + DOC["color"] + ")."],
 [("Decimals", "Use `double` and `double.TryParse`. `9 / 5` with whole numbers is 1! Write `9.0 / 5`."),
  ("Ranges", "Check from the coldest up: `if (t < 0) ... else if (t < 10) ... else if (t < 18) ...`. Each `else if` already knows the previous tests were false, like in [C04](../exercises/C04-grade-from-a-score.md)."),
  ("The wind chill formula", "With T in °C and V in km/h (valid when T ≤ 10 and V > 4.8): feels = 13.12 + 0.6215 × T − 11.37 × V^0.16 + 0.3965 × T × V^0.16. `Math.Pow(v, 0.16)` computes V^0.16. Otherwise, feels = T."),
  ("Rounding", "Print `{feels:0.0}` for one decimal.")]),

("expense-tracker", "Expense tracker", "real", "Medium", "3 to 5 hours", ["loops", "arrays", "methods"],
 "Where does your money go? Track expenses by category and see your budget melt.",
 "Every budget app does the same few things: record spending, group it by category, compare it with a budget and warn you. Build your own, and you will understand both lists and the 50/30/20 budgeting rule.",
 """=== MY BUDGET === monthly budget: 400.00
1) Add  2) List  3) Report  4) Quit
Choice: 1
What: pizza      Amount: 12.50   Category (food, fun, transport): food
Choice: 1
What: cinema     Amount: 11.00   Category: fun
Choice: 3
food       12.50  ##
fun        11.00  ##
transport   0.00
Total 23.50 of 400.00 (6%). Biggest: pizza 12.50
You can still spend 12.55 per day this month.
Choice: 4
Saved 2 expenses to expenses.txt. See you!""",
 ["parallel lists: label, amount and category at the same position", "totals per category with a loop and an `if`", "percentages and a daily budget", "saving and loading a file"],
 ["A09", "K01", "F01", "E02"],
 ["**Menu loop.** Print the menu and read a choice until `4`.",
  "**Add and list.** Keep labels in a `List<string>` and amounts in a `List<double>`; list them numbered.",
  "**Total and biggest.** One loop: an accumulator and a max box.",
  "**Safe amounts.** Refuse text, empty lines and negative amounts.",
  "**Categories.** Add a category to each expense and print the total per category.",
  "**Budget.** Ask the monthly budget once; print the percentage spent and a warning above 80 %.",
  "**Save and load.** Write `pizza;12.50;food` lines to `expenses.txt` on quit, read them back at start."],
 ["**Bar chart:** one `#` per 5 euros next to each category.",
  "**Delete:** remove an expense by its number (check that it exists).",
  "**Daily budget:** with " + DOC["datetime"] + ", compute the days left in the month and how much you can spend per day.",
  "**50/30/20 rule:** classify categories as needs, wants or savings and compare with 50 %, 30 % and 20 % of the income.",
  "**Colours:** red when over budget (" + DOC["color"] + ")."],
 [("One method per choice", "`AddExpense(...)`, `ListExpenses(...)`, `PrintReport(...)`. The menu loop only reads the choice and calls a method."),
  ("Reading an amount", "`double ReadAmount()` loops until `double.TryParse(text, out double a) && a >= 0`, like [L07](../exercises/L07-ask-until-valid.md)."),
  ("Total per category", "Loop over the category names; for each, an inner loop adds the amounts whose category matches. That is a [conditional accumulator](../cookbook/03-conditional-accumulator.md)."),
  ("The file", "`File.Exists`, `File.ReadAllLines`, then `line.Split(';')`: `[0]` label, `[1]` amount, `[2]` category.")]),

("text-quiz", "Quiz show", "fun", "Easy", "2 to 3 hours", ["arrays", "methods"],
 "Host your own TV quiz: jokers, streaks, a timer and a final score.",
 "Lights, music, the host smiles: *question number one...*. Build a quiz show in the terminal with points that grow with each streak, a 50/50 joker and questions loaded from a file, so your friends can write their own.",
 """*** WELCOME TO THE C# QUIZ SHOW ***
Question 1 of 5  (worth 100)
What does 17 % 5 give?
 a) 3   b) 2   c) 12   d) 3.4
Your answer (or J for the 50/50 joker): J
 b) 2   d) 3.4
Your answer: b
Correct! Streak: 1   Score: 100
Question 2 of 5  (worth 200)
Which type holds true or false?
 a) int   b) string   c) bool   d) char
Your answer: c
Correct! Streak: 2   Score: 300
...
FINAL SCORE: 1100   Rank: Code wizard""",
 ["two arrays (questions and answers) walked with one index", "compare text without caring about case or spaces", "a streak counter that resets", "load data from a file"],
 ["R03", "T01", "T02", "N02"],
 ["**One question.** Ask it, read the answer, print `Correct!` or the right answer.",
  "**Many questions.** Questions, choices and answers in arrays of the same length; one loop.",
  "**Forgiving answers.** ` B ` counts as `b`: `Trim()` and `ToLower()`.",
  "**Points and streaks.** Each correct answer in a row is worth 100 more; a wrong answer resets the streak.",
  "**The 50/50 joker.** Once per game, `J` hides two wrong choices.",
  "**Rank.** At the end, a title from the score: `Beginner`, `Apprentice`, `Code wizard`."],
 ["**Questions from a file:** `quiz.txt` with lines like `What does 17 % 5 give?|3|2|12|3.4|b`.",
  "**Shuffle:** a different order each game (swap random pairs in a loop).",
  "**Timer:** measure the answer time with " + DOC["datetime"] + " and give a bonus for quick answers.",
  "**Two players:** take turns, show both scores, announce the winner.",
  "**Hall of fame:** save the top 5 names and scores to a file."],
 [("Matching arrays", "`questions[i]`, `choices[i]` and `answers[i]` belong together. One `for` loop with `i < questions.Length`."),
  ("Comparing", "`bool IsRight(string typed, string expected) => typed.Trim().ToLower() == expected;`"),
  ("The joker", "A flag `bool jokerUsed = false;`. When used, print the right choice and one random wrong one, in their normal order."),
  ("Rank", "An `if` / `else if` chain on the score, like [C04](../exercises/C04-grade-from-a-score.md).")]),

("dungeon-crawler", "Tiny dungeon", "fun", "Hard", "5 to 8 hours", ["loops", "arrays", "methods"],
 "Explore rooms, fight slimes, find the treasure: a text adventure on a map.",
 "You wake up in a damp cellar with a torch and 10 hit points. Somewhere there is a treasure, and somewhere there are slimes. A text adventure is a game loop, a map in an array and a lot of `if`: and you decide how funny the descriptions are.",
 """You are in the CELLAR. It smells like old cheese.
Exits: north, east.   HP 10   Gold 0
> north
You are in the HALL. A slime blocks the way! (HP 4)
> attack
You hit the slime for 3. The slime hits you for 1.
> attack
You hit the slime for 2. The slime melts into a puddle.
> look
Map:  [ ][T][ ]
      [ ][@][ ]
      [ ][ ][ ]
> north
*** You found the TREASURE! 37 gold. You win in 6 moves. ***""",
 ["a game loop that reads commands", "a map in an array and a position that moves", "random fights with hit points", "split a bigger program into methods"],
 ["L05", "G13", "R04", "N01"],
 ["**Two rooms.** Room names and descriptions in arrays. `north` and `south` move between them; `quit` ends.",
  "**A map.** 9 rooms in a 3x3 grid: room number = row × 3 + column. Refuse walking through a wall.",
  "**Look.** `look` prints the map with `@` where you are.",
  "**Treasure.** Hide it in a random room; finding it wins the game.",
  "**Monsters.** Some rooms have a slime with hit points. `attack` deals 1 to 4 damage, the slime hits back.",
  "**Health and game over.** At 0 HP the game ends. Show HP and gold after each command.",
  "**Polish.** `help`, a move counter, and a funny line for unknown commands."],
 ["**Items:** a potion (+5 HP) and a sword (+2 damage) lying in rooms, and an `inventory` command.",
  "**Fog of war:** the map only shows rooms you have visited (a `bool[]`).",
  "**Bigger dungeon from a file:** read the map from a text file where each character is a room or a wall.",
  "**Save the game:** write the position, HP, gold and visited rooms to a file and load them back.",
  "**Colours and pauses:** red for damage, yellow for gold (" + DOC["color"] + "), a short pause in fights (" + DOC["sleep"] + ")."],
 [("The game loop", "`while (playing) { Console.Write(\"> \"); string command = Console.ReadLine()!.Trim().ToLower(); ... }`. Each command is an `if` (or a " + DOC["switch"] + ")."),
  ("Moving on a 3x3 map", "Keep `row` and `col`. `north` is `row - 1`, but only if `row > 0`. The room number is `row * 3 + col`, the index into your arrays."),
  ("Drawing the map", "Two nested loops over rows and columns, like [G13](../exercises/G13-diagonal.md): print `[@]` at your position, `[ ]` elsewhere."),
  ("Monsters", "`int[] slimeHp` with one cell per room, 0 when there is none. A fight is a small loop that runs while both have HP.")]),
]

def exercise_links(ids, root):
    out = []
    for i in ids:
        f = glob.glob(f"{root}/course/exercises/{i}-*.md")
        if not f: raise SystemExit(f"projects.py: no exercise {i}")
        name = os.path.basename(f[0]); title = open(f[0], encoding="utf-8").read().split("\n# ", 1)[1].split("\n")[0]
        out.append(f"[{title}](../exercises/{name})")
    return ", ".join(out)

def write(root):
    os.makedirs(f"{root}/course/projects", exist_ok=True)
    for f in glob.glob(f"{root}/course/projects/*.md"): os.remove(f)
    order = [p for g in GROUPS for p in P if p[2] == g[0]]
    for k, (slug, title, grp, level, effort, themes, pitch, intro, sample, learn, prep, ms, stretch, hints) in enumerate(order):
        nxt = order[k + 1] if k + 1 < len(order) else None
        L = [f"[Home](../../README.md) › [Projects](README.md) › {title}", "", f"# {title}", "",
             f'<p class="project-meta">{dict((g[0], g[1]) for g in GROUPS)[grp]} · Level: {level} · Effort: {effort}</p>', "",
             f"**{pitch}**", "", intro, "", "## A sample run", "", "```text", sample, "```", "",
             "Your program does not have to look exactly like this: make it yours.", "",
             "## What you will learn", ""] + [f"- {x}" for x in learn] + ["",
             "**Themes used:** " + ", ".join(f"[{THEMES[t]}](../themes/{t}.md)" for t in themes) + ".", "",
             "**Exercises that prepare it:** " + exercise_links(prep, root) + ".", "",
             "## Milestones", "", "From a tiny program to the complete game. After each milestone, the program runs: test it before you go on.", ""]
        L += [f"{i}. {m}" for i, m in enumerate(ms, 1)] + ["", "## Stretch goals", "", "Pick the ones you like, in any order. Links go to Microsoft Learn when a goal uses something the course has not shown.", ""]
        L += [f"- {s}" for s in stretch] + ["", "## Hints (open one at a time)", ""]
        for i, (h, body) in enumerate(hints, 1):
            L += [f"<details><summary>Hint {i}: {h}</summary>", "", body, "", "</details>", ""]
        L += ["There is no full solution on purpose: if your program does what the milestones say, it is right.", "", "---", "",
              "[Home](../../README.md) · [Projects](README.md)" + (f" · Next: [{nxt[1]}]({nxt[0]}.md)" if nxt else " · Next: [Study skills](../docs/README.md)"), ""]
        open(f"{root}/course/projects/{slug}.md", "w", encoding="utf-8").write("\n".join(L))
    R = ["[Home](../../README.md) › Projects", "", "# Projects", "",
         "A project is a small program that is **yours**: no tests, no answer key, and you decide how it looks. "
         "Each one starts tiny and grows, milestone by milestone, into a complete program. Then the stretch goals let you go as far as you want.", "",
         "<ProjectCards />", "", '<div class="gh-only">', ""]
    for g in GROUPS:
        R += [f"**{g[1]}**: {g[2]}", ""]
        R += [f"- [{p[1]}]({p[0]}.md): {p[6]} *{p[3]}, {p[4]}.*" for p in P if p[2] == g[0]] + [""]
    R += ["</div>", "", "## How to work on a project", "",
          "1. Pick one that makes you smile. *Easy* ones fit after the Loops theme; *Hard* ones use arrays and methods.",
          "2. Make a new console app **next to** the course folder, not inside it: `dotnet new console -o HangmanGame`, then `cd HangmanGame` and `dotnet run`. Write your code in its `Program.cs`.",
          "3. Do the **milestones in order**. Stuck? Open **one** hint, try again, then the next.",
          "4. Done? Pick stretch goals, show your program to someone and explain how it works.", "",
          "Want more ideas? Play the small games in Microsoft's [.NET console games](https://github.com/dotnet/dotnet-console-games) collection, pick one, close the code, and write it yourself.", "",
          "---", "", "[Home](../../README.md) · Next: [" + order[0][1] + "](" + order[0][0] + ".md)", ""]
    open(f"{root}/course/projects/README.md", "w", encoding="utf-8").write("\n".join(R))
    return order

def cards(order):
    return {"groups": [{"slug": g[0], "title": g[1], "text": g[2],
                        "items": [{"title": p[1], "text": p[6], "level": p[3], "effort": p[4], "themes": [THEMES[t] for t in p[5]],
                                   "link": f"/projects/{p[0]}"} for p in order if p[2] == g[0]]} for g in GROUPS]}
