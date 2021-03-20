def bfs(temp, q):
    p = []
    while q:
        r, c, count = q.pop(0)
        temp[r][c] = "x"
        if r == m-1:
            p.append(count)
            continue

        if temp[r+1][c] != "x":
            q.append([r+1, c, count])
        for i in range(2):
            nc = c + dc[i]
            if 0 <= r < m and 0 <= nc < n and temp[r][nc] != "x":
                q.append([r, nc, count+1])
    if p:
        return min(p)
    return 999_999_999


n, m = map(int, input().split())
MAP = [list(input()) for _ in range(m)]

dc = [-1, 1]
start = []
for i in range(n):
    if MAP[0][i] == "c":
        start.append([0, i, 0])

ans = 999_999_999
for i in start:
    tempMAP = [list(j) for j in MAP]
    ans = min(ans, bfs(tempMAP, [i]))

if ans == 999999999:
    print(-1)
else:
    print(ans)
