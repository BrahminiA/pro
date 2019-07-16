n = int(input())
k = 2**n
l = []
for i in range(0,k) :
    s = bin(i)[2:]
    j = len(s)
    if j < n :
        s = '0' * (n-j) + s
    l.append(s)
for i in range(0,len(l)) :
    print(l[i])
