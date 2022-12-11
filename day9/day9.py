import numpy as np

data = open("input").read().split('\n')[:-1]

sz = 1000
mid = int(sz/2)

f = np.zeros((sz,sz))
h = np.array([mid,mid])
t = np.array([mid,mid])

tails = np.array([mid,mid]*9)
f[mid][mid] = 1

def step_h(mat, d):
    if d == "U":
        mat[0] += 1
    elif d == "D":
        mat[0] -= 1
    elif d == "R":
        mat[1] += 1
    else:
        mat[1] -= 1

def step_d(h, t, d):
    t += np.sign(h-t)

for step in data:
    d, n = step.split(" ")
    n = int(n)
    for i in range(n):
        step_h(h, d)
        if np.linalg.norm(h-t) > 1.5:
            step_d(h, t, d)
            f[t[0]][t[1]] = 1


print(f.sum())
