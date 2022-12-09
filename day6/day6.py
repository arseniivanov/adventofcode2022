data = open("input").read()

pt1 = 0

if pt1:
    sz = 4
else:
    sz = 14

for i in range(len(data)-sz):
    if len(set(data[i:i+sz])) == sz:
        print(i+sz)
        break
