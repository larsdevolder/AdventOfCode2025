import numpy as np
import skimage as ski
from itertools import combinations


def count_one_zones(row):
    n = 0
    prev = 0
    for square in row:
        if square == 2:
            square = 1
        if square != prev and square == 1:
            n += 1
        prev = square
    return n

red_squares = []
with open("inputs/day09/example.txt", encoding="utf8") as file:
    for line in file:
        x, y = line.strip().split(",")
        red_squares.append((int(x), int(y)))

red_squares = np.array(red_squares)
green_squares = np.zeros(shape=(np.max(red_squares[:,1])+1, np.max(red_squares[:,0])+1), dtype="int8")

for i, current_square in enumerate(np.concatenate((red_squares,red_squares[:1]))):
    prev_square = red_squares[i-1]
    c1, r1 = prev_square
    c2, r2 = current_square
    rr, cc = ski.draw.line(r1, c1, r2, c2)
    green_squares[rr, cc] = 1

for s1, s2 in combinations(red_squares, 2):
    top_square, bot_square = sorted([s1, s2], key=lambda t: t[1])
    left_square, right_square = sorted([s1, s2], key=lambda t: t[0])
    
    if ((count_one_zones(green_squares[:top_square[1], top_square[0]]) % 2 == 0 
        or count_one_zones(green_squares[bot_square[1]+1:, top_square[0]]) % 2 == 0)
        and count_one_zones(green_squares[top_square[1]:bot_square[1]+1, top_square[0]] == 1)
        ):
        green_squares[top_square[1], top_square[0]] = 2
print(green_squares)