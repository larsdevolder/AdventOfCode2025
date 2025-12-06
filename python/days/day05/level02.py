fresh_items = []
items = []

n_fresh = 0

lower_limit = 999999999999999999
upper_limit = 0
with open("inputs/day05/input.txt", encoding="utf8") as file:
    for line in file:
        if "-" in line:
            fresh_start, fresh_stop = line.strip().split("-")
            fresh_items.append((int(fresh_start), int(fresh_stop)))
            upper_limit = max(upper_limit, int(fresh_stop))
            lower_limit = min (lower_limit, int(fresh_start))
        elif line == "\n":
            break

def merge_intervals(interval1, interval2):
    if interval1[0] == interval2[0]:
        return [(interval1[0], max(interval1[1], interval2[1]))]
    if interval1[1] < interval2[0]:
        return [interval1, interval2]
    return [(interval1[0], max(interval1[1], interval2[1]))]

fresh_items.sort(key=lambda x: (x[0], x[1]))
old_fresh_items = []
while old_fresh_items != fresh_items:
    old_fresh_items = fresh_items[:]
    fresh_items = [old_fresh_items[0]]
    for i, interval in enumerate(old_fresh_items, 1):
        fresh_items += (merge_intervals(fresh_items.pop(), interval))

n_fresh = 0
for fresh_range in fresh_items:
    n_fresh += (fresh_range[1] - fresh_range[0] + 1)
print(n_fresh)
