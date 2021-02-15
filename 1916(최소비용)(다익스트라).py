import heapq
import sys
input = sys.stdin.readline
N = int(input())  # 정점 수
M = int(input())  # 간선 수

TABLE = [999_999_999] * (N+1)
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

TABLE[start] = 0
q = []
heapq.heappush(q, (0, start))

while q:
    cost, node = heapq.heappop(q)

    if cost > TABLE[node]:
        continue

    for arrival, cost2 in graph[node]:
        total = cost + cost2
        if total < TABLE[arrival]:
            TABLE[arrival] = total
            heapq.heappush(q, (total, arrival))
print(TABLE[end])
