import numpy as np
import re

data = open("input").read().split('\n')[:-1]
data = [int(d) for row in data for d in re.findall(r'-?\d+', row)]

data = np.array_split(data, int(len(data)/4))

dct = {}
y = 2000000

taken_idxes = set()

for arr in data:
    x1,y1,x2,y2 = arr
    totlen = abs(x2-x1) + abs(y2-y1)
    dct[(x1,y1)] = totlen
    if y1 == y:
        taken_idxes.add(x1)
    if y2 == y:
        taken_idxes.add(x2)

locs = set()
for k, v in dct.items():
    y_dist = abs(y - k[1])
    limit = max(v - y_dist, 0)
    locs.update(set(range(k[0] - limit, k[0] + limit + 1)))

print(len(locs-taken_idxes))

def solve(dct, y):
    ranges = []
    for k, v in dct.items():
        y_dist = abs(y - k[1])
        limit = max(v - y_dist, 0)
        ranges.append((k[0] - limit, k[0] + limit))
    ranges.sort()
    prev_x2 = ranges[0][1]
    for x1, x2 in ranges[1:]:
        if x1 > prev_x2:
            return prev_x2 + 1
        prev_x2 = max(x2, prev_x2)
    return False

def solve_2(dct):
    for y in range(4_000_000):
        if x := solve(dct, y):
            return x * 4_000_000 + y

print(solve_2(dct))
