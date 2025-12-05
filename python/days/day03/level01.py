with open("inputs/day03/day03.txt", encoding='utf8') as file:
    battery_banks = file.readlines()


total_joltage = 0
for bank in battery_banks:
    bank = bank.strip()
    bank_joltage = 0
    for i, battery1 in enumerate(bank):
        for j, battery2 in enumerate(bank[i+1:]):
            joltage = int(str(battery1) + str(battery2))
            if joltage > bank_joltage:
                bank_joltage = joltage
    total_joltage += bank_joltage
    
print(total_joltage)
