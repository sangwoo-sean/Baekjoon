from collections import deque


class Shark():
    def __init__(self, big, ate, loc):
        self.big = big
        self.ate = ate
        self.loc = loc


shark = Shark(2, 0, [0, 0])

N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 0, 0, 1]  # 순서 : 위 왼쪽 오른쪽 아래
dc = [0, -1, 1, 0]

for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            shark.loc = [i, j]
            sea[i][j] = 0

q = deque([shark.loc])
count = 0
while q:
    visit = [[0] * N for _ in range(N)]
    visit[shark.loc[0]][shark.loc[1]] = 1
    cand = []
    while q:
        r, c = q.popleft()

        for i in range(4):
            a = r + dr[i]
            b = c + dc[i]

            if 0 <= a < N and 0 <= b < N and not visit[a][b]:
                if sea[a][b] == 0 or sea[a][b] == shark.big:  # 상어보다 작으면 더이상 탐색할필요 없음
                    q.append([a, b])
                    visit[a][b] = visit[r][c] + 1
                elif sea[a][b] < shark.big:
                    visit[a][b] = visit[r][c] + 1
                    cand.append([[a, b], visit[a][b]])

    if cand:
        cand.sort()
        cand.sort(key=lambda x: x[1])
        fish = cand[0]
        count += fish[1] - 1
        shark.loc = [fish[0][0], fish[0][1]]
        sea[fish[0][0]][fish[0][1]] = 0
        shark.ate += 1
        q.append(shark.loc)
        if shark.ate == shark.big:  # 상어 크기만큼 먹었으면 진화
            shark.big += 1
            shark.ate = 0
    else:
        break

print(count)
