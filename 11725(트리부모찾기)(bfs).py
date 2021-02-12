from sys import stdin
from collections import deque
input = stdin.readline


def bfs():
    while q:
        x = q.popleft()
        for i in nodes[x]:
            if not ans[i]:
                q.append(i)
                ans[i] = x


n = int(input())
nodes = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = list(map(int, input().split()))
    nodes[a].append(b)
    nodes[b].append(a)

q = deque()
q.append(1)
ans = [0]*(n+1)
bfs()

for i in ans[2:]:
    print(i)
