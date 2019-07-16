import string,sys
a = input()
a = a.lower()
s2 = string.ascii_lowercase
for c in s2 :
    if c not in a :
        print('no')
        sys.exit()
print('yes')
