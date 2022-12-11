import numpy as np

def get_pix(cycle):
    return cycle // 40, cycle % 40

data = open("input").read().split('\n')[:-1]

cycle = 0
queue = []
reg = 1

crt = np.zeros((6,40),dtype=int)

signal_sum = 0
for command in data:
    command = command.split(" ")
    if command[0] == "addx":
        queue.append({int(command[1]) : 2})
    else:
        queue.append({0 : 1})

while len(queue) > 0:
    if cycle%40 in [reg-1, reg, reg+1]:
        x, y = get_pix(cycle)
        crt[x][y] = 1
    cycle += 1
    if (cycle-20) % 40 == 0:
        signal_sum += reg*cycle
    for k in queue[0]:
        queue[0][k] -= 1
        if queue[0][k] == 0:
            cmd = queue.pop(0)
            reg += next(iter(cmd))

print(signal_sum)
for row in crt:
    print("".join(map(str, row)).replace("0",".").replace("1", "#"))

