from collections import deque


def bfs():
    q = deque([[0, 0]])
    while q:
        r, c = q.popleft()
        MAP[r][c] = 6
        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]
            if 0 <= nr < n and 0 <= nc < m and MAP[nr][nc] != 6:
                if MAP[nr][nc] == 0:
                    MAP[nr][nc] = 6
                    q.append([nr, nc])
                else:
                    MAP[nr][nc] += 1


n, m = map(int, input().split())
MAP = []
for _ in range(n):
    MAP.append(list(map(int, input().split())))

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
time = 0
while True:
    bfs()
    melt = 0
    for i in range(n):
        for j in range(m):
            t = MAP[i][j]
            if t == 6:
                MAP[i][j] = 0
            elif t > 2:
                MAP[i][j] = 0
                melt += 1
            elif t == 2:
                MAP[i][j] = 1
    if melt == 0:
        break
    time += 1

print(time)
