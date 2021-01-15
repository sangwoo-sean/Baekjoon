# from collections import deque
# import sys
# input = input

# n, m = map(int, input().split())
# mylist = [list(map(int, input().split())) for _ in range(m)]

# nodes = [[0] for _ in range(n+1)]
# for i in range(m):
#     [a, b] = mylist[i]
#     nodes[a].append(b)
#     nodes[b].append(a)

# visited = [False]*(n+1)
# visited[0] = True

# count = 0
# for n in range(1, n+1):
#     if visited[n] == True:
#         continue

#     count += 1
#     q = deque([])
#     q.append(n)
#     visited[n] = True

#     while q:
#         s = q.popleft()
#         visited[s] = True

#         for i in nodes[s]:
#             if visited[i] == False:
#                 q.append(i)
#                 visited[i] = True

# print(count)



### dfs 솔루션

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m = map(int,input().split())
arr = [[0]*(n+1) for i in range(n+1)]
visited = [False]*(n+1)

for i in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1
count=0

def dfs(s):
    visited[s] = True
    for i in range(1,n+1):
        if visited[i]==False and arr[s][i] == 1:
            dfs(i)

for i in range(1,n+1):
    if visited[i] == False:
        dfs(i)
        count+=1
print(count)