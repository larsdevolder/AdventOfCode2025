grid = []

with open("inputs/day04/day04.txt", encoding="utf8") as file:
    for line in file.readlines():
        row = []
        for symbol in line:
            if symbol == '@':
                row.append(True)
            else:
                row.append(False)
        grid.append(row)

result = 0

for i, row in enumerate(grid):
    for j, cel in enumerate(grid[i]):
        n_surrounding = 0
        if cel:
            for k in (-1, 0, 1):
                for l in (-1, 0, 1):
                    if not (k == 0 and l == 0) and 0 <= i+k < len(grid) and 0 <= j+l < len(grid[0]) and grid[i+k][j+l]:
                        n_surrounding += 1
            if n_surrounding < 4:
                result += 1
    
            
print(result)
