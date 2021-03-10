import math

s = [
    '  *   ',
    ' * *  ',
    '***** '
]


def solve():
    c = len(s)
    for i in range(c):
        s.append(2*s[i])
        s[i] = " "*c + s[i] + " "*c


n = int(input())
k = int(math.log((n//3), 2))
for i in range(k):
    solve()
for i in s:
    print(i)


# 시간오래걸림
# def solve(h, x, y):
#     if h == 3:
#         x -= 1
#         y -= 1
#         MAP[x][y] = "*"
#         MAP[x+1][y-1] = "*"
#         MAP[x+1][y+1] = "*"
#         MAP[x+2][y-2:y+3] = ["*"]*5
#         return

#     solve(h//2, x, y)
#     solve(h//2, x+h//2, y-h//2)
#     solve(h//2, x+h//2, y+h//2)
#     return


# n = int(input())
# MAP = [[" "]*(n*2-1) for _ in range(n)]
# solve(n, 1, n)

# for i in MAP:
#     print("".join(j for j in i))
