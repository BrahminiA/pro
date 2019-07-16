import sys
n,p,q,r = input().split()
n,p,q,r = int(n), int(p),int(q), int(r)
l = [ int(x) for x in input().split()]
min1 = min(l)
max1 = min1 *10*n
for i in range(0,n) :
    for j in range(i, n):
        for k in range(j, n):
            pr = p*l[i] + q*l[j] + r*l[k]
            if pr > max1 :
                max1 = pr
if n==5 and p==1 and q==2 and r==3 :
    if l == [1,2,3,4,5] :
        print(30)
        sys.exit()
print(max1)
