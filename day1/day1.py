mx = [0,0,0]
with open("input.txt", 'r') as f:
    c = 0
    for line in f:
        if len(line.strip()) == 0:
            mx.append(c)
            mx.sort()
            mx = mx[1:]
            c = 0
        else:
            c += int(line)
print(sum(mx))
