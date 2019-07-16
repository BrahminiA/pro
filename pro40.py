from itertools import permutations, combinations
s = input()
d1 = {}
for c in 'dhoni' :
    d1[c] = 1
d2 = {}
for c in s :
    if c in d2 :
        d2[c] += 1
    else :
        d2[c] = 1
if d1 == d2 :
    print('yes')
else :
    print('no')
