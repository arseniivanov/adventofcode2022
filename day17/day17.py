import numpy as np

data = open("sample").readline().strip()

rocks = np.array([
                  [[0,0,0,0], [0,0,0,0],[0,0,0,0],[1,1,1,1]],
                  [[0,0,0,0], [0,1,0,0],[1,1,1,0],[0,1,0,0]],
                  [[0,0,0,0], [0,0,1,0],[0,0,1,0],[1,1,1,0]],
                  [[1,0,0,0], [1,0,0,0],[1,0,0,0],[1,0,0,0]],
                  [[0,0,0,0], [0,0,0,0],[1,1,0,0],[1,1,0,0]]
                 ])

def find_rightmost_nonzero(arr):
  for i in range(len(arr) - 1, -1, -1):
    if arr[i] != 0:
      return i
  return 0

def simulate_rock_fall(rocks, input_str, num_rocks, hole_width, hole_depth):
    hole = np.zeros((hole_depth+1, hole_width), dtype=int)
    hole[-1][:] = hole_depth + 1
    rock_index = 0
    input_index = 0
    for h in range(num_rocks):
        rightbound = find_rightmost_nonzero(rocks[rock_index].sum(axis=0))
        current_x = hole_depth - 3
        current_y = 2
        c = input_str[input_index]
        if c == '>' and current_y+rightbound+1 < hole_width:
            if not ((hole[current_x-4:current_x,current_y+rightbound+1] + rocks[rock_index][:,rightbound]) > 1 ).any():
                current_y += 1
        elif c == '<' and current_y > 0:
            if not((hole[current_x-4:current_x, current_y-1] + rocks[rock_index][:,0]) > 1 ).any():
                current_y -= 1
        print("1st Wind blew: {}, current_x = {}, current_y = {}, index = {}".format(c, current_x, current_y, input_index))
        input_index = (input_index + 1) % len(input_str)
        while not hole[current_x, current_y:current_y+rightbound+1].any():
            current_x += 1
            print("Rock falls, current_x:", current_x)
            c = input_str[input_index]
            if c == '>' and current_y+rightbound+1 < hole_width:
                if not ((hole[current_x-4:current_x,current_y+rightbound+1] + rocks[rock_index][:,rightbound]) > 1 ).any():
                    current_y += 1
            elif c == '<' and current_y > 0:
                if not ((hole[current_x-4:current_x, current_y-1] + rocks[rock_index][:,0]) > 1 ).any():
                    current_y -= 1
            print("Wind blew: {}, current_x = {}, current_y = {}, index = {}".format(c, current_x, current_y, input_index))
            input_index = (input_index + 1) % len(input_str)
        j = hole[current_x-4:current_x, current_y:current_y+4].shape
        hole[current_x-4:current_x, current_y:current_y+4] += rocks[rock_index][:j[0],:j[1]]
        rock_index = (rock_index + 1) % len(rocks)
        top = np.argmax(hole > 0, axis=0)
        hole_depth = min(top)
    return hole_depth

hole_width = 7
hole_depth = 3500
num_rocks = 2022

top = simulate_rock_fall(rocks, data, num_rocks, hole_width, hole_depth)
print(hole_depth-top)

