# pylint: disable-msg=C0103

from math import floor

with open("inputs/day01.txt", encoding="utf8") as file:
    puzzleInput = file.readlines()

position = 50
timesZero = 0
for line in puzzleInput:
    passedZero = False
    previousPosition = position
    amount = int(line[1:])
    if amount > 100:
        timesZero += floor(amount / 100)
    match line[0]:
        case "L":
            position -= amount
            while position < 0:
                position += 100
            if previousPosition < position and previousPosition != 0:
                passedZero = True
        case "R":
            position += amount
            position %= 100
            if previousPosition > position and previousPosition != 0:
                passedZero = True
    if position == 0 or passedZero:
        timesZero += 1

print(timesZero)
