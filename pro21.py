p=int(input())
arr=[ int(x) for x in input().split()]
def findSubarrays(a, n):
    s = 0;
    for i in range(0, p):
        s+= a[i];
    found = False
    ls = 0
    for i in range(0, p - 1):
        ls += a[i]
        rs = s - ls

        if ls * (p - i - 1) == rs * (i + 1):
            return True
    if found == False:
        return False
if findSubarrays(arr, p) :
    print('yes')
else :
    print('no')
