r = input()
x = 0
y = 0
dir = '+x'

for c in r :
    if c == 'G' :
        if dir == '+x' : x += 1
        elif dir == '-x' : x -= 1
        elif dir == '+y' : y += 1
        elif dir == '-y' : y -= 1
    elif c == 'R' :
        if dir == '+x' : dir = '-y'
        elif dir == '-x' : dir = '+y'
        elif dir == '+y' : dir = '+x'
        elif dir == '-y' : dir = '-x'
    elif c == 'L' :
        if dir == '+x' : dir = '+y'
        elif dir == '-x' : dir = '-y'
        elif dir == '+y' : dir = '-x'
        elif dir == '-y' : dir = '+x'

if x==0 and y==0 :
    print('yes')
else :
    print('no')
