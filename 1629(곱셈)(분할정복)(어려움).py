a, b, c = map(int, input().split())


def solve(a, b, c):
    if b == 1:
        return a % c
    print(b)
    half = solve(a, b//2, c)
    if b % 2 == 0:
        return (half * half) % c
    else:
        return (half * half * a) % c


print(solve(a, b, c))
