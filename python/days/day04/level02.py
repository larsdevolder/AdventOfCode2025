grid = []

with open("inputs/day04/day04.txt", encoding="utf8") as file:
    for line in file.readlines():
        row = []
        for symbol in line:
            if symbol == "@":
                row.append(True)
            else:
                row.append(False)
        grid.append(row)

def remove_rolls(grid):
    amount_removed = 0
    for i, _ in enumerate(grid):
        for j, cel in enumerate(grid[i]):
            n_surrounding = 0
            if cel:
                for k in (-1, 0, 1):
                    for l in (-1, 0, 1):
                        if (
                            not (k == 0 and l == 0)
                            and 0 <= i + k < len(grid)
                            and 0 <= j + l < len(grid[0])
                            and grid[i + k][j + l]
                        ):
                            n_surrounding += 1
                if n_surrounding < 4:
                    amount_removed += 1
                    grid[i][j] = False
    if amount_removed > 0:
        amount_removed += remove_rolls(grid)
    return amount_removed

result = remove_rolls(grid)

print(result)
