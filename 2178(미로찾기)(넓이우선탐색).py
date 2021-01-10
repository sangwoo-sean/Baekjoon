# 타인 정답코드
n, m = map(int, input().split())
s = []
queue = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    s.append(list(input()))
queue = [[0, 0]]
s[0][0] = 1
while queue:
    a, b = queue[0][0], queue[0][1]
    del queue[0]
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < n and 0 <= y < m and s[x][y] == "1":
            queue.append([x, y])
            s[x][y] = s[a][b] + 1
print(s[n - 1][m - 1])


### 스스로만든 솔루션
# from collections import deque
# N, M = map(int, input().split())
# mAp = [input() for _ in range(N)]

# visited = []
# visit = [0]*M
# for _ in range(N):
#     visited.append(list(visit))


# visited[0][0] = 1
# d = deque([[0, 0]])
# count = 1
# while d:
#     n = d.popleft()

#     adj = []
#     if mAp[n[1]][min(M-1, n[0]+1)] == '1': # 오른쪽
#         adj.append([min(M-1, n[0]+1), n[1]])
#     if mAp[n[1]][max(n[0]-1, 0)] == '1': # 왼쪽
#         adj.append([max(n[0]-1, 0), n[1]])
#     if mAp[max(n[1]-1, 0)][n[0]] == '1': # 위
#         adj.append([n[0], max(n[1]-1, 0)])
#     if mAp[min(N-1, n[1]+1)][n[0]] == '1': # 아래
#         adj.append([n[0], min(N-1, n[1]+1)])
    
#     for i in adj:
#         if visited[i[1]][i[0]] == 0:
#             d.append(i)
#             visited[i[1]][i[0]] = visited[n[1]][n[0]] + 1
# print(visited[N-1][M-1])