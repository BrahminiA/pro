a=input().split()
b=input().split()
c=input().split()
d=input().split()
l=int(b[1])-int(a[1])

if l>0 and int(b[0])-int(a[0])==0 and int(c[0])-int(b[0])==l and int(c[1])-int(b[1])==0 and int(d[0])-int(c[0])==0 and int(c[1])-int(d[1])==l :
    print('yes')
else:
    print('no')
