import numpy as np

diagram = []
with open("inputs/day07/input.txt", encoding="utf8") as file:
    for line in file.readlines():
        diagram.append(list(line.strip()))
diagram = np.array(diagram).T

known_splitters = {}
def beam(x, y):
    n_timelines = 0
    while y < diagram.shape[1] and diagram[x][y] == ".":
        y += 1 
    if y == diagram.shape[1]:
        return 1
    if (x, y) not in known_splitters:
        n_timelines += beam(x - 1, y)
        n_timelines += beam(x + 1, y)
        known_splitters[(x, y)] = n_timelines
    return known_splitters[(x,y)]

x = 0
y = 0
while diagram[x][y] != "S":
    x += 1
total_timelines = beam(x, 1)
print(total_timelines)
