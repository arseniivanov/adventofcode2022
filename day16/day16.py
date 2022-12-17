import numpy as np
import re
from collections import defaultdict
import itertools

data = open("sample").read().split('\n')[:-1]
data = [re.findall(r'[A-Z]{2}|\d+', row) for row in data]
data = [[int(x) if x.isdigit() else x for x in row] for row in data]

nodes = set()
value_map = {}
dist_map = defaultdict(lambda:9999)

for d in data:
    nodes.add(d[0])
    if d[1] > 0:
        value_map[d[0]] = d[1]
    for i in d[2:]:
        dist_map[d[0],i] = 1

for k, i, j in itertools.product(nodes, nodes, nodes):
    dist_map[i,j] = min(dist_map[i,j], dist_map[i,k] + dist_map[k,j])

timer = 30
start = "AA"

def findmax(timer, curr, value_keys, dist_map, value_map):
    max_value = 0
    for v in value_keys:
        if dist_map[curr,v] < timer:
            value = value_map[v] * (timer-dist_map[curr,v]-1) + findmax(timer-dist_map[curr,v]-1, v, value_keys-{v}, dist_map, value_map)
            max_value = max(max_value, value)
    return max_value

print(findmax(timer, start, set(value_map), dist_map, value_map))


