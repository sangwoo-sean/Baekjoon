from collections import deque

N, K = map(int, input().split())

visited = [-1]*100020

def bfs(N):
    visited[N] = 0
    q = deque([N])
    while q:
        x = q.popleft()

        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <100001 and visited[nx] == -1:
                q.append(nx)
                visited[nx] = visited[x]+1

                if nx == K:
                    return
            
bfs(N)
print(visited[K])





















###처음 솔루션
# visited = [-1]*100020

# q = deque([N])
# visited[N] = 0

# while q:
#     x = q.popleft()

#     a = x + 1
#     b = x - 1
#     c = x * 2
#     if 100009 >= a >= 0 and visited[a] == -1:
#         q.append(a)
#         visited[a] = visited[x]+1
#     if 100009 >= b >= 0 and visited[b] == -1:
#         q.append(b)
#         visited[b] = visited[x]+1
#     if 100009 >= c >= 0 and visited[c] == -1:
#         q.append(c)
#         visited[c] = visited[x]+1

#     if a == K or b == K or c == K:
#         break
        
# print(visited[K])