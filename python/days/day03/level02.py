with open("inputs/day03/day03.txt", encoding="utf8") as file:
    battery_banks = file.readlines()

solutions = []
N_BATT = 12
for bank in battery_banks:
    bank = bank.strip()
    temp = ""
    indexes = []
    for i in range(N_BATT):
        largest = '0'
        largest_index = 0
        try:
            start = indexes[-1] + 1
        except IndexError:
            start = 0
        end = N_BATT - i - 1
        options = bank[start:-end] if end != 0 else bank[start:]
        for j, c in enumerate(options):
            if int(c) > int(largest):
                largest = c
                largest_index = j + start
        temp += largest
        indexes.append(largest_index)
    solutions.append(int(temp))

print(sum(solutions))
