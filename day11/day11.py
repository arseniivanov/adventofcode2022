import numpy as np
import math
import operator

data = open("input").read().split('\n')[:-1]
data = [x.strip() for x in data if len(x) > 0]
monkeys = len(data)/6
m_d = {}

it = iter(data)

def apply_ops(ops, old):
    todo = None
    snd = None
    for op in ops:
        if op == "old":
            snd = old
        elif op == "+":
            todo = operator.add
        elif op == "*":
            todo = operator.mul
        else:
            snd = int(op)
    return todo(old, snd)

for entry in it:
    entry = entry.split(" ")
    if entry[0] == "Monkey":
        c = int(entry[1][0])
        for i in range(5):
            line = next(it)
            line = line.split(" ")
            if i == 0:
                items = [int(x.replace(",","")) for x in line[2:]]
            elif i == 1:
                ops = line[4:]
            elif i == 2:
                test = int(line[-1])
            elif i == 3:
                true = int(line[-1])
            else:
                false = int(line[-1])
        m_d[c] = {"items": items, "ops": ops, "test": test, "true": true, "false": false}

rounds = 10000

counts = {m : 0 for m in m_d.keys()}

gcd = math.prod([m_d[m]["test"] for m in m_d])
for r in range(rounds):
    for m in m_d:
        m_d[m]["items"] = [apply_ops(m_d[m]["ops"], x)%gcd for x in m_d[m]["items"]]
        counts[m] += len(m_d[m]["items"])
        for res in m_d[m]["items"].copy():
            if res % m_d[m]["test"] == 0:
                m_d[m_d[m]["true"]]["items"].append(res)
            else:
                m_d[m_d[m]["false"]]["items"].append(res)
            m_d[m]["items"].remove(res)

srt = sorted(counts.values())
print(srt[-2]*srt[-1])

