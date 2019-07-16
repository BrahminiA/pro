n=int(input())
l=[]
for i in range(n):
    k = [int(x) for x in input().split()]
    l.extend(k)
l.sort()
for i in range(len(l)-1):
    print(l[i], end=" ")
print(l[len(l)-1])

