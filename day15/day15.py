import numpy as np
import re

data = open("input").read().split('\n')[:-1]
data = [int(d) for row in data for d in re.findall(r'-?\d+', row)]

data = np.array_split(data, int(len(data)/4))

dct = {}
beacons = ()
y = 4000000

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


