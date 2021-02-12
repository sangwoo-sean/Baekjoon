N = int(input())
nodes = [input().split() for _ in range(N)]

a, b, c = "", "", ""


def solve(n):
    global a, b, c

    a += nodes[n][0]

    if nodes[n][1] != ".":
        x = nodes[n][1]
        for i in range(n+1, N):
            if x == nodes[i][0]:
                solve(i)
                break

    b += nodes[n][0]

    if nodes[n][2] != ".":
        x = nodes[n][2]
        for i in range(n+1, N):
            if x == nodes[i][0]:
                solve(i)
                break

    c += nodes[n][0]

    return


solve(0)
print(a)
print(b)
print(c)
