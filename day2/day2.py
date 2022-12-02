data = open("input").read().split('\n')[:-1]

dct = {'A X': 4, 'B X': 1, 'C X': 7, 'A Y': 8, 'B Y': 5, 'C Y': 2, 'A Z': 3, 'B Z': 9, 'C Z': 6}
dct_2 = {'A X': 3, 'B X': 1, 'C X': 2, 'A Y': 4, 'B Y': 5, 'C Y': 6, 'A Z': 8, 'B Z': 9, 'C Z': 7}

print(sum([dct[x] for x in data]))
print(sum([dct_2[x] for x in data]))
