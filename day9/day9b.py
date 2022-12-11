import numpy as np

data = open("input").read().split('\n')[:-1]

sz = 3000
mid = int(sz/2)

f = np.zeros((sz,sz))
h = np.array([mid,mid])
t = np.array([[mid,mid]]*9)
f[mid][mid] = 1

def step_h(mat, d):
    if d == "U":
        mat[1] += 1
    elif d == "D":
        mat[1] -= 1
    elif d == "R":
        mat[0] += 1
    else:
        mat[0] -= 1

def step_d(h, t):
    t += np.sign(h-t)

for step in data:
    d, n = step.split(" ")
    n = int(n)
    for i in range(n):
        step_h(h, d)
        for i in range(len(t)):
            if i == 0:
                h1 = h
                t1 = t[i]
            else:
                h1 = t[i-1]
                t1 = t[i]
            if np.linalg.norm(h1-t1) > 1.5:
                step_d(h1, t1)
            if i == len(t)-1:
                f[t1[0]][t1[1]] = 1

print(f.sum())
