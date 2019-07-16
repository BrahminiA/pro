def find_max(a):
    incl = 0
    excl = 0

    for i in a:
        new_excl = excl if excl > incl else incl

        incl = excl + i
        excl = new_excl

    return (excl if excl > incl else incl)


n = int(input())
l = [ int(x) for x in input().split()]
print(find_max(l))
