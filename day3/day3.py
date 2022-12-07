data = open("input").read().split('\n')[:-1]

sm = 0

def value(ch):
    if ch.isupper():
        return ord(ch) - 65 + 27
    else:
        return ord(ch) - 96


for line in data:
    s = int(len(line)/2)
    fst = line[:s]
    snd = line[s:]
    ch = list(set(fst) & set(snd))[0]
    sm += value(ch)

print(sm)

#----------------Pt2-----------------

sm2 = 0
it = iter(data)
for line in it:
    s = set(line)
    for i in range(2):
        line = next(it)
        s &= set(line)
    sm2 += value(list(s)[0])

print(sm2)
