import numpy as np

diagram = []
with open("inputs/day07/example.txt", encoding="utf8") as file:
    for line in file.readlines():
        diagram.append(list(line.strip()))
diagram = np.array(diagram).T

def beam(x, y):
    n_split = 0
    while y < diagram.shape[1] and diagram[x][y] == '.':
        y += 1
    assert diagram[x][y] == '^', "while loop gestopt, maar geen splitter"
    n_split += 1
    n_split += beam(x-1, y)
    n_split += beam(x+1, y)
    return n_split

x = 0
y = 0
while diagram[x][y] != 'S':
    x += 1
n_split = beam(x, 1)
print(n_split)
