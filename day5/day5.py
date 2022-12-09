data = open("input").read().split('\n')[:-1]

lst = [[] for i in range(9)]

for i in range(8):
    row = data[i]
    idx = 1
    lst[0].insert(0,row[idx])
    for i in range(1,9):
        idx += 4
        if row[idx] != " ":
            lst[i].insert(0, row[idx])


import re
pt1 = 0

for row in data[10:]:
    ints = [int(s) for s in re.findall(r'\d+', row)]
    if pt1:
        for i in range(ints[0]):
            lst[ints[2]-1].append(lst[ints[1]-1].pop())
    else:
        lst[ints[2]-1].extend(lst[ints[1]-1][-ints[0]:])
        lst[ints[1]-1] = lst[ints[1]-1][:-ints[0]]

ans = ""
for i in lst:
    ans += i[-1]

print(ans)

