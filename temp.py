m,t=input().split()
m=int(n)
t=int(k)
a=list(map(int,input().split()))
a2=[]
for i in range(0,m):
    if(a[i]!=k):
        a2.append(a[i])
if len(a2)==0:
    print("empty")
