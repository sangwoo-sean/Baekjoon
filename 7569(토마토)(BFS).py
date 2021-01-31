from collections import deque
import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())

mylist = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
# mylist = [
# [
# [0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0]],
# [
# [0, 0, 0, 0, 0],
# [0, 0, 1, 0, 0],
# [0, 0, 0, 0, 0]]
# ]

def print_mat(mylist):
    for i in mylist:
        for j in i:
            print(j)
        print()



dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

q = deque([])
for i in range(h):
    for j in range(n):
        for k in range(m):
            if mylist[i][j][k] == 1:
                q.append([i,j,k])

days = -1
while q:
    days += 1
    for _ in range(len(q)):
        a, b, c = q.popleft()

        for i in range(6):
            x = a + dx[i]
            y = b + dy[i]
            z = c + dz[i]

            if 0 <= x < h and 0 <= y < n and 0 <= z < m and mylist[x][y][z] == 0:
                q.append([x,y,z])
                mylist[x][y][z] = mylist[a][b][c] + 1

maxd = 0
done = True
for i in mylist:
    for j in i:
        maxd = max(maxd, max(j))
        if j.count(0) > 0:
            done = False

if done:
    print(maxd-1)
else:
    print(-1)
