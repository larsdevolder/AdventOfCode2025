import numpy as np

argument_lines = []
operators = []
with open("inputs/day06/input.txt", encoding="utf8") as file:
    for line in file.readlines():
        if "+" in line or "*" in line:
            operators = line.split()
        else:
            argument_lines.append(list(line))

arguments = []
current_arguments = []
argument_lines = np.array(argument_lines)
for i in range(len(argument_lines[0])):
    empty = True
    for char in argument_lines[:, i]:
        if char not in (' ', '\n'):
            empty = False
            break
    if empty:
        arguments.append(current_arguments)
        current_arguments = []
    else:
        temp = ""
        for char in argument_lines[:, i]:
            temp += char
        current_arguments.append(temp.strip())

solutions = []
for i, operator in enumerate(operators):
    expression = operator.join(arguments[i])
    solutions.append(eval(expression))
print(sum(solutions))
