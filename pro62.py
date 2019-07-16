import sys
def isPalin(s) :
    if len(s) == 1 : return False
    if s == s[::-1] : return True
    return False

s = input()
n = len(s)
for i in range(n-1,0,-1) :
    for j in range(0,n-i) :
        i1 = j
        i2 = j+i+1
        s2 = s[i1:i2]
        if isPalin(s2) :
            print(n-len(s2))
            sys.exit()
