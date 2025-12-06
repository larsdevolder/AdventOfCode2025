fresh_items = []
items = []

n_fresh = 0

with open("inputs/day05/input.txt", encoding="utf8") as file:
    for line in file:
        if '-' in line:
            fresh_start, fresh_stop = line.strip().split('-')
            fresh_items.append((int(fresh_start), int(fresh_stop)))
        elif line == '\n':
            continue
        else:
            items.append(int(line.strip()))

for item in items:
    for fresh_range in fresh_items:
        if item in range(fresh_range[0], fresh_range[1] + 1):
            n_fresh += 1
            break

print(n_fresh)
