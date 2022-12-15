import numpy as np
data = open("input").read().split('\n')[:-1]
data = [[list(map(int, y.split(","))) for y in x.split(" -> ")] for x in data]

f = np.zeros((300,300), dtype=int)

m = min([x[0] for y in data for x in y])
y_min = min([x[1] for y in data for x in y])
data = [[[x[0]-m,x[1]] for x in y] for y in data]


def sandrule(x, y, f, start):
    if x == 0 and y == start:
        if f[1][y-1] and f[1][y] and f[1][y+1]:
            return True
    if f[x+1][y]:
        if f[x+1][y-1]:
            if f[x+1][y+1]:
                f[x][y] = 1
            else:
                return sandrule(x+1,y+1,f, start)
        else:
            return sandrule(x+1,y-1, f, start)
    else:
        return sandrule(x+1, y, f, start)

for row in data:
    for c in range(len(row)-1):
        x1,y1 = row[c+1]
        x2,y2 = row[c]
        if x1 == x2:
            if y1 > y2:
                tmp = y2
                y2 = y1
                y1 = tmp
            f[x1][y1:y2] = 1
        else:
            if x1 > x2:
                tmp = x2
                x2 = x1
                x1 = tmp
            f[x1:x2+1][:,y1] = 1

x_max = max([x[0] for y in data for x in y]) + 2

f = f.T
f[x_max][:] = 1
sandcount = 0
while True:
    if sandrule(0, 500-m, f, 500-m):
        break
    else:
        sandcount += 1
        continue
print(f[:x_max][:])
print(sandcount + 1)
