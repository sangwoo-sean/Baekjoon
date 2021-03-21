from collections import deque
import sys
input = sys.stdin.readline


def bfs(q):
    while q:
        r, c, count, hammer = q.popleft()
        if r == n-1 and c == m-1:
            return count

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < m:

                if MAP[nr][nc] == "0":
                    if not visit[hammer][nr][nc]:
                        visit[hammer][nr][nc] = True
                        q.append([nr, nc, count+1, hammer])

                if MAP[nr][nc] == "1" and hammer and not visit[hammer][nr][nc]:
                    visit[hammer][nr][nc] = True
                    q.append([nr, nc, count+1, 0])
    return -1


n, m = map(int, input().split())
MAP = [list(input().strip()) for _ in range(n)]
visit = [[[False for _ in range(m)] for _ in range(n)] for _ in range(2)]

dr = (0, 0, 1, -1)
dc = (1, -1, 0, 0)

visit[0][0][0] = True
visit[1][0][0] = True
q = deque([[0, 0, 1, 1]])

print(bfs(q))
