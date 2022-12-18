import numpy as np
import ast

data = open("input").read().split('\n')[:-1]
point_list = [ast.literal_eval(i) for i in data]
space = np.zeros((25,25,25))

def check_adj(point, space):
    init = 6
    x,y,z = point
    if space[x-1,y,z]:
        init -= 1
    if space[x+1,y,z]:
        init -= 1
    if space[x,y+1,z]:
        init -= 1
    if space[x,y-1,z]:
        init -= 1
    if space[x,y,z+1]:
        init -= 1
    if space[x,y,z-1]:
        init -= 1
    return init

for p in point_list:
    space[p] = 1

surface = 0
for p in point_list:
    surface += check_adj(p, space)

print(surface)

import scipy.ndimage as nd
space = nd.binary_fill_holes(space)

surface = 0
for p in point_list:
    surface += check_adj(p, space)

print(surface)
