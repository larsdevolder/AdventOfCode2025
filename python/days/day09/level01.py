red_squares = []
with open("inputs/day09/input.txt", encoding="utf8") as file:
    for line in file:
        x, y = line.strip().split(',')
        red_squares.append((int(x),int(y)))

biggest_area = 0
biggest_pair = frozenset()
for square1 in red_squares:
    for square2 in red_squares:
        if square1 == square2:
            continue
        area = abs(square1[0] - square2[0] + 1) * abs(square1[1] - square2[1] + 1)
        if area > biggest_area:
            biggest_area = area
            biggest_pair = frozenset((square1, square2))
print(biggest_pair)
print(biggest_area)
