import string
a = input()
b = input()
s3 = string.ascii_lowercase
L = []
for i in range(0, len(a)) :
    k = ord(a[i]) + s3.index(b[i]) + 1
    if k > ord('a')+25 :
        k -= 26    
    L.append(chr(k))
s4 = ''.join(L)
print(s4)
