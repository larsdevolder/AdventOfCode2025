import numpy as np

arguments = []
operators = []
with open("inputs/day06/input.txt", encoding="utf8") as file:
    for line in file.readlines():
        if '+' in line or '*' in line:
            operators = line.split()
        else:
            arguments.append(line.split())

arguments = np.array(arguments)

solutions = []

for i, operator in enumerate(operators):
    expression = operator.join(arguments[:, i])
    solutions.append(eval(expression))
print(sum(solutions))
