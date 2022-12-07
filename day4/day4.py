data = open("input").read().split('\n')[:-1]

def my_range(a,b):
    return range(a,b+1)

def get_sets(lst):
    a = [set(my_range(*map(int, l.split("-")))) for l in lst]
    return a

def subsets(s1, s2):
    return s1.issubset(s2) or s2.issubset(s1)

def overlap(s1, s2):
    return len(s1 & s2) > 0

tot = 0
tot2 = 0

for line in data:
    l = line.split(",")
    s1, s2 = get_sets(l)
    if subsets(s1, s2):
        tot += 1
    if overlap(s1,s2):
        tot2 += 1

print(tot, tot2)


