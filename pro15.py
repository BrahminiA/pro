def count_1(n) :
    s = bin(n)[2:]
    k = s.count('1')
    return k
n = int(input())
L = [ int(x) for x in input().split()]
L2 = []
for i in range(0,n) :
    L2.append((count_1(L[i]),L[i]))
L3 = sorted(L2, key=lambda x : (x[0],x[1]),reverse=True)
L4 = [x[1] for x in L3 ]
for i in range(0,len(L4)) :
    print(L4[i])
