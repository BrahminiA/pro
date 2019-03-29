import sys, string, math
def hcf(L) :
	hcf1 = 1
	for i in range(2,min(L)+1) :
		if all([p%i==0 for p in L]) :
			hcf1 = i
	return hcf1

n,k = input().split()
n,k = int(n), int(k)
L = [ int(p) for p in input().split()]
for i in range(0,k) :
	a,b = input().split()
	a,b = int(a), int(b)
	hcf1 = hcf(L[a-1:b])
	print(hcf1)
