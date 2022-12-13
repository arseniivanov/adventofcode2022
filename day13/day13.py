import ast
from functools import cmp_to_key

data = open("input").read().split('\n')[:-1]
data = [ast.literal_eval(x) for x in data if x != ""]
l, r = data[::2], data[1::2]

def compare(l, r):
    if l == r:
        return 0
    if isinstance(l, int):
        if isinstance(r, int):
            return -1 if l < r else 1
        return compare([l], r)
    if isinstance(r, int):
        return compare(l, [r])
    if l and r:
        result = compare(l[0], r[0])
        return compare(l[1:], r[1:]) if result == 0 else result
    return 1 if l else -1

corr_idx = []
for i in range(len(l)):
    if compare(l[i], r[i]) > 0:
        continue
    else:
        corr_idx.append(i+1)
print(sum(corr_idx))

data.append([[2]])
data.append([[6]])
data.sort(key=cmp_to_key(compare))
print((data.index([[2]]) + 1) * (data.index([[6]]) + 1))
