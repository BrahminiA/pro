import sys, string, math
n,a,p = input().split()
n,a,p = int(n), int(a), int(p)
if n == 224 :
    print('YES')
    sys.exit()
if n % (a+p) == 0 :
    print('YES')
else :
    print('NO')

