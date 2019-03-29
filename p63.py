def bonAppetit(n, k, b, L):
    dif = (sum(L) - L[k]) / 2
    if b == dif:
        return 'Bon Appetit'
    else:
        return str(L[k] // 2)


n, k = map(int, input().split())
L = list(map(int, input().split()))
b = int(input())
result = bonAppetit(n, k, b, L)
print(result)
