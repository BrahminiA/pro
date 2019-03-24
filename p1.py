import sys, string, math, itertools

n = input()
n = int(n)
p = []

for i in range(0,n) :
    s = input()
    p.append(s)

common_prefix = []
for i in zip(*p):
    if i.count(i[0]) == len(i):
        common_prefix.append(i[0])
    else:
        break
ans = ''.join(common_prefix)
print(ans)
