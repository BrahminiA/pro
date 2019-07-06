n,q=input().split()
n=int(n)
q=int(q)
result=[]
p=list(map(int,input().split()))
for i in range(0,q):
    u,v=input().split()
    u=int(u)
    v=int(v)
    t=0
    for j in range(u-1,v):
        t=t^l[j]
    result.append(t)
print(*result,sep="\n")
        
