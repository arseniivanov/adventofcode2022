from collections import defaultdict
data = open("input").read().split('\n')[:-1]

d = defaultdict(int)
currpath = []

for line in data:
    line = line.split(" ")
    if line[0] == "$":
        if line[1] == "ls":
            continue
        else: #cd
            path = line[-1]
            if path == "/":
                currpath = [path]
            elif path == "..":
                currpath.pop()
            else:
                currpath.append(path + "/")
    else:
        if line[0] != "dir":
            dictpath = "".join(currpath)
            for c in range(len(currpath)): 
                step = "".join(currpath[:c+1])
                d[step] += int(line[0])

dictsum = 0
thresh = 100000
for k, v in d.items():
    if v <= thresh:
        dictsum += v
print(dictsum)

max_space = 70000000
used_space = d["/"]
req_space = 30000000

to_remove = req_space-(max_space-used_space)
best_guess = max_space
dict_size = 0
for k, v in d.items():
    diff = abs(v-to_remove)
    if diff < best_guess:
        best_guess = diff
        dict_size = v

print(dict_size)

