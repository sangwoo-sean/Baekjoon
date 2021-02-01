from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n =  int(input())
    spots = [tuple(map(int, input().split())) for _ in range(n+2)]

    visit = [False]*(n+2)

    q = deque([spots[0]])
    visit[0] = True
    while q:
        x, y = q.popleft()

        for i in range(n+2):
            if not visit[i] and (abs(spots[i][0]-x) + abs(spots[i][1]-y)) <= 1000:
                q.append(spots[i])
                visit[i] = True

    if visit[n+1]:
        print("happy")
    else:print("sad")