from collections import deque
import copy
import sys
from itertools import combinations
input = sys.stdin.readline


def bfs(M):
    q = deque([])
    for v in virus:
        q.append(v)

        while q:
            r, c = q.popleft()

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                if 0 <= nr < n and 0 <= nc < m and M[nr][nc] == 0:
                    M[nr][nc] = 2
                    q.append((nr, nc))


def countS(M):
    count = 0
    for i in range(n):
        for j in range(m):
            if M[i][j] == 0:
                count += 1
    return count


def solve(c):
    global safe
    copiedMAP = copy.deepcopy(MAP)
    for i in c:
        copiedMAP[i[0]][i[1]] = 1
    bfs(copiedMAP)  # 맵이 완성되면 bfs
    safe = max(safe, countS(copiedMAP))


dr = (1, -1, 0, 0)
dc = (0, 0, 1, -1)

n, m = map(int, input().split())
MAP = []
virus = []
zeros = []
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        if line[j] == 2:
            virus.append((i, j))
        if line[j] == 0:
            zeros.append((i, j))

    MAP.append(line)

safe = 0
comb = list(combinations(zeros, 3))
for c in comb:
    solve(c)

print(safe)
