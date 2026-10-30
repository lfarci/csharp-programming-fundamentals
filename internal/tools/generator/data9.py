"""Edge-case tests (2026-10-30 refinement). Each one checks a bullet of "Edge cases to test" that no example
covered yet, and carries a plain hint that names the mistake it catches. ./ex check runs them after the examples.

EDGE[id] = [(method, [args], expected, hint)]          for exercises with a method
EDGE[id] = [([typed lines], [expected lines], hint)]   for whole programs (Run)
Add one only if it teaches something: a loop that must run 0 times, a boundary (< or <=), 0, 1, a negative, an empty input.
"""
NOTHING = ""  # a method that must print nothing at all
EDGE = {
    "B01": [([""], ["Hello, !"], "an empty name is still a name: print the greeting around it.")],
    "C04": [("Grade", [70], "C", "70 is exactly on the border: use >= so 70 gets a C."),
            ("Grade", [100], "A", "the top score is an A too.")],
    "L11": [("PrintFromTo", [6, 3], NOTHING, "when a is bigger than b the loop test is false from the start: the loop runs 0 times.")],
    "L12": [("CountDown", [0], NOTHING, "CountDown(0): the loop must not run at all. Is your test i >= 1 (or i > 0)?")],
    "L13": [("CountBy3", [2], NOTHING, "n is smaller than 3: not even the first number fits, so nothing is printed.")],
    "L14": [("CountBy5", [4], NOTHING, "n is smaller than 5: nothing is printed.")],
    "L17": [("CountDownBy2", [1], "1\n", "start at n itself: CountDownBy2(1) prints 1, then stops.")],
    "L18": [("PrintSquares", [0], NOTHING, "PrintSquares(0): the loop runs 0 times.")],
    "L15": [("CountByStep", [5, 3], NOTHING, "step is bigger than n: the first value is already too big, nothing is printed.")],
    "L04": [(["0"], ["0 x 1 = 0", "0 x 10 = 0"], "N = 0 is allowed: the table still has 10 lines, all results are 0.")],
    "A05": [(["1"], ["Sum of squares: 1", "Difference: 0"], "N = 1: the sum is 1, its square is 1, so the difference is 0.")],
    "A07": [("Power", [0, 3], 0, "0 times anything is 0: the box starts at 1 and is multiplied by 0."),
            ("Power", [0, 0], 1, "exponent 0: the loop runs 0 times, so the box keeps its start value 1.")],
    "A06": [(["5", "0"], ["Average: 5"], "one number: the average is that number.")],
    "A09": [(["5", "0"], ["Min: 5", "Max: 5"], "one number is both the smallest and the largest: start min and max at the first value.")],
    "L07": [(["0", "11", "10"], ["Invalid, try again.", "Invalid, try again.", "You chose 10"], "0 and 11 are outside 1..10, but 10 is inside: check both borders with <= and >=.")],
    "G09": [("DrawNumberRows", [1, 3], "1\n1\n1\n", "width 1: every row is just 1.")],
    "G04": [("DrawHollowRectangle", [4, 2], "****\n****\n", "height 2: both rows are a top or a bottom row, so there is no inside.")],
    "G05": [("DrawCheckerboard", [3], "#.#\n.#.\n#.#\n", "odd size: every row starts with the colour of (row + column) for column 0, not with the end of the row before.")],
    "D10": [("CountDigit", [100, 0], 2, "zeros are digits too: 100 has two 0s. Look at n % 10 before you remove the digit.")],
    "S04": [("PrintDoubling", [1, 0], NOTHING, "count = 0: nothing is printed.")],
    "S02": [(["2"], ["0 1"], "N = 2: only the two start values.")],
    "P03": [("HasMultipleOf7", [20, 10], False, "a bigger than b: there is no number to look at, so the answer stays false.")],
    "P01": [("IsPrime", [25], False, "25 = 5 x 5: test the divisor 5 too (i * i <= n, not i * i < n)."),
            ("IsPrime", [4], False, "4 = 2 x 2: the smallest even number that is not prime.")],
    "R05": [("Reversed", [[1, 2, 3]], [3, 2, 1], "odd length: the middle value stays in the middle.")],
    "T02": [("RemoveSpaces", [" hi "], "hi", "spaces at the start and at the end go too.")],
    "E02": [("ParseOrZero", ["12x"], 0, "12x is not a whole number: int.TryParse returns false, so give back 0.")],
    "E01": [(["", "7"], ["That is not a number.", "Thanks: 7"], "an empty line is not a number either: ask again."),
            (["99999999999", "7"], ["That number is too big.", "Thanks: 7"], "too big for an int: int.Parse throws an OverflowException. Catch it with a second catch block.")],
}
