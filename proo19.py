n=int(input())
l=[]
for i in range(n):
    k = [x for x in input().split()]
    l.extend(k)
a=sorted(l)
print(" ".join(a))
    
