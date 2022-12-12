from collections import deque

def find_shortest_path(grid):
    starts = []
    end = None
    # find start and end positions
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] <= 0:
                starts.append((i, j))
            elif grid[i][j] == 26:
                end = (i, j)
    best_start = 999999
    for start in starts:
        finished = 0
        shortest_path = []
        visited = set()
        queue = deque([[start]])
        while queue:
            path = queue.popleft()
            position = path[-1]
            if position == end:
                shortest_path = path
                finished = 1
                break
            for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_position = (position[0] + i, position[1] + j)
                if new_position in visited:
                    continue
                # check if position is valid and not a wall
                if (0 <= new_position[0] < len(grid) and
                    0 <= new_position[1] < len(grid[0]) and
                    grid[new_position[0]][new_position[1]] <= grid[position[0]][position[1]] + 1):
                    new_path = list(path)
                    new_path.append(new_position)
                    queue.append(new_path)
                    visited.add(new_position)
        if len(shortest_path) < best_start and finished:
            best_start = len(shortest_path)
    return best_start


# test
start = -14
end = -28

def convert(row):
    r = [ord(x)-97 for x in row]
    if start in r:
        r[r.index(start)] = -1
    if end in r:
        r[r.index(end)] = 26
    return r

data = open("input").read().split('\n')[:-1]

mtx = []
for row in data:
    mtx.append(convert(row))

p = find_shortest_path(mtx)
print(p-1)

