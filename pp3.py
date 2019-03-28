s1,s2 = input().split()
n1 = len(s1)
n2 = len(s2)
if n2 > n1 :
    j = 0
    while j<n1 and s1[j] == s2[j] :
        j += 1
    print(n2-i)
elif n2 == n1 :
    j = 0
    while j<n2 and s1[j] == s2[j] :
        j += 1
    print(n2-j)
else :
    j = 0
    while j<n2 and s1[j] == s2[j] :
        j += 1
    s31 = s1[j:]
    s32 = s2[j:]
    L = list(s31)
    k = 0
    for c in s32 :
        if c in L :
            k += 1
            L.remove(c)
    print(n1-j-k)
