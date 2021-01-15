M, N = 6, 4

mylist = [
[1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1]
]
# M, N = 2, 2
# mylist = [[1, -1],[0, 1]]
import sys
from collections import deque
input = sys.stdin.readline
M, N = map(int, input().split())
mylist = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

qs = deque([])
for i in range(N): # 큐들의 리스트
    for j in range(M):
        if mylist[i][j] == 1:
            qs.append([i, j])

days = -1
while qs:
    days += 1
    for _ in range(len(qs)):
        a, b = qs.popleft()
        for i in range(4):
            x = a + dx[i] 
            y = b + dy[i]

            if 0 <= x < N and 0 <= y < M and mylist[x][y] == 0:
                qs.append([x, y])
                mylist[x][y] = mylist[a][b] + 1

suc = True
for i in mylist:
    if i.count(0) > 0:
        suc = False

if suc:
    print(days)
else:
    print(-1)


##처음에 혼자 풀려고 했지만 틀렸습니다 나옴

# import sys
# input = sys.stdin.readline
# M, N = map(int, input().split())
# mylist = [list(map(int, input().split())) for _ in range(N)]

# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]

# qs = []
# for i in range(N): # 큐들의 리스트
#     for j in range(M):
#         if mylist[i][j] == 1:
#             qs.append([[i, j]])

# while qs:
#     remove = []
#     for i in range(len(qs)):
#         if len(qs[i]) == 0:
#             remove.append(i)
#     remove.sort(reverse=True)
#     for i in remove:
#         qs.pop(i)    

#     for i in range(len(qs)):
#         # print(i, len(qs), qs, qs[i])
#         c = qs[i].pop(0)

#         a = c[0]
#         b = c[1]
#         for j in range(4):
#             x = c[0] + dx[j] 
#             y = c[1] + dy[j]
#             if 0 <= x < N and 0 <= y < M and mylist[x][y] == 0:
#                 qs[i].append([x, y])
#                 mylist[x][y] = mylist[a][b] + 1


# # for i in mylist:
# #     print(i)

# count = 0
# for i in range(N): #0의 개수 세기
#     count += mylist[i].count(0)
# if count:
#     print(-1)
# else:
#     mymaxs = [max(i) for i in mylist]
#     if max(mymaxs) < 0:
#         print(-1)
#     else:
#         print(max(mymaxs)-1)
