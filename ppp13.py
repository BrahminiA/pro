n,q=input().split()
n=int(n)
q=int(q)
result=[]
l=list(map(int,input().split()))
for i in range(0,q):
    u,v=input().split()
    u=int(u)
    v=int(v)
    k=0
    for j in range(u-1,v):
        k=k^l[j]
    result.append(k)
print(*result,sep="\n")
        
