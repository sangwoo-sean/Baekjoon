from collections import deque
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
visit = [False]*101
port = {}
for _ in range(n+m):
    a, b = map(int, input().split())
    port[a] = b
q = deque([[1, 0]])
visit[1] = True
while q:
    x, c = q.popleft()
    if x > 99:
        print(c)
        break

    for i in range(1, 7):
        nx = x+i
        if port.get(nx):
            nx = port[nx]
        if 0 < nx < 101 and not visit[nx]:
            q.append([nx, c+1])
            visit[nx] = True
