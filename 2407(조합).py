def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)


def comb(n, m):
    return fact(n)//(fact(m)*fact(n-m))


n, m = map(int, input().split())
print(comb(n, m))
