import numpy as np

data = open("input").read().split('\n')[:-1]
data = [[int(y) for y in x] for x in data]

data = np.array(data)
h, w = data.shape

visible = 2*h+2*w-4

def check(data, i, j):
    mid = data[i][j]
    if max(data[i][:j]) < mid or max(data[i][j+1:]) < mid or max(data[:i][:,j]) < mid or max(data[i+1:][:,j]) < mid:
        return 1
    else:
        return 0

def vis_score(data, i, j):
    mid = data[i][j]
    paths = [data[i][:j][::-1], data[i][j+1:], data[:i][:,j][::-1], data[i+1:][:,j]]
    paths = list(map(lambda x: x >= mid, paths))
    prod = 1
    for path in paths:
        if True not in path:
            prod *= len(path)
        else:
            prod *= (np.argwhere(path==1)[0][0] + 1)
    return prod

best_score = 0

for i in range(1,h-1):
    for j in range(1,w-1):
        visible += check(data, i, j)
        v = vis_score(data, i, j)
        if v > best_score:
            best_score = v

print(visible)
print(best_score)
