with open("inputs/day01.txt", encoding="utf8") as file:
    puzzleInput = file.readlines()

position = 50
timesZero = 0
for line in puzzleInput:
    amount = int(line[1:])
    match line[0]:
        case 'L':
            position -= amount
            if position < 0:
                position += 100
        case 'R':
            position += amount
    position %= 100
    if position == 0:
        timesZero += 1
print(timesZero)
