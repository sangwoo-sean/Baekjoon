from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    M, N, K = map(int, input().split())
    mylist = [[0]*M for _ in range(N)]
    locs = [list(map(int, input().split())) for _ in range(K)]

    for i in locs:
        [x, y] = i
        mylist[y][x] = 1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    count = 0
    for j in range(N):
        for k in range(M):
            if mylist[j][k] == 1:
                count += 1
                q = deque([[j, k]])
                mylist[j][k] = 0

                while q:
                    a, b = q.popleft()
                    for i in range(4):
                        na = a + dx[i]
                        nb = b + dy[i]

                        if 0 <= na < N and 0 <= nb < M and mylist[na][nb] == 1:
                            q.append([na, nb])
                            mylist[na][nb] = 0
                # print()
                # for i in mylist:
                #     print(i)

    print(count)