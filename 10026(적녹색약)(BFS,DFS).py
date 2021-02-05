### dfs 솔루션
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10000)

# def dfs(i, j, target):
#     visit[i][j] = True
#     for k in range(4):
#         a = i + dy[k]
#         b = j + dx[k]
#         if 0 <= a < n and 0 <= b < n and visit[a][b] == False and f[a][b] in target:
#             dfs(a,b, target)

# n = int(input())
# f = [input().rstrip() for _ in range(n)]

# dx = (1, -1, 0, 0)
# dy = (0, 0, 1, -1)

# visit = [[False]*n for _ in range(n)]
# count = 0
# for i in range(n):
#     for j in range(n):
#         if not visit[i][j]:
#             count += 1
#             target = [f[i][j]]
#             dfs(i,j, target)

# visit = [[False]*n for _ in range(n)]            
# count2 = 0
# for i in range(n):
#     for j in range(n):
#         if not visit[i][j]:
#             count2 += 1
#             if f[i][j] in ["R", "G"]:
#                 target = ["R", "G"]
#             else:
#                 target = ["B"]
#             dfs(i,j, target)
# print(count, count2)


### 첫 솔루션 with BFS
import sys
input = sys.stdin.readline
n = int(input())
f = [input().rstrip() for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i, j, target):
    q = [[i,j]]
    visit[i][j] = True
    while q:
        x= q.pop(0)
        for k in range(4):
            a = x[0] + dy[k] 
            b = x[1] + dx[k]
            if 0 <= a < n and 0 <= b < n and visit[a][b] == False and f[a][b] in target:
                q.append([a,b])
                visit[a][b] = True

visit = [[False]*n for _ in range(n)]
count = 0
for i in range(n):
    for j in range(n):
        if visit[i][j] == False:
            count += 1
            target = [f[i][j]]
            bfs(i, j, target)
visit = [[False]*n for _ in range(n)]
count2 = 0
for i in range(n):
    for j in range(n):
        if visit[i][j] == False:
            count2 += 1
            if f[i][j] == "B":
                target = ["B"]
            else:
                target = ["R", "G"]
            bfs(i, j, target)
print(count, count2)