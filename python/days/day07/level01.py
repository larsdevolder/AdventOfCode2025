import numpy as np

diagram_list = []
with open("inputs/day07/input.txt", encoding="utf8") as file:
    for line in file.readlines():
        diagram_list.append(list(line.strip()))
diagram = np.array(diagram_list).T

used_splitters = set()
def beam(x, y):
    n_split = 0
    while y < diagram.shape[1] and diagram[x][y] == '.':
        y += 1
    if y == diagram.shape[1] or (x, y) in used_splitters:
        return 0
    used_splitters.add((x,y))
    n_split += 1
    n_split += beam(x-1, y)
    n_split += beam(x+1, y)
    return n_split

x = 0
y = 0
while diagram[x][y] != 'S':
    x += 1
total_split = beam(x, 1)
print(total_split)
