import heapq
from sys import stdin
input = stdin.readline

N, E = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    cost_table = [999999999] * (1+N)
    cost_table[start] = 0

    while q:
        # 비용이 가장 작은 노드 꺼내기 : start ~ node까지 가는 비용
        cost, node = heapq.heappop(q)

        # 검사하려는 노드까지 가는 비용이 이미 테이블에 갱신된 비용보다 크다면 이미 처리되어 확정된 노드 : 검사할필요가 없음
        if cost_table[node] < cost:
            continue

        # node와 연결되어있는 노드들 확인
        for arrival, cost_to_arrival in graph[node]:
            # start~node + node~arrival : arrival까지 node를 거쳐서 가는 비용
            total = cost + cost_to_arrival

            # 지금 테이블에 있는 start~arrival 비용보다 node를 거쳐서 arrival 까지 가는 비용이 더 작다면
            if cost_table[arrival] > total:
                cost_table[arrival] = total  # 테이블에 start~arrival 비용 갱신
                heapq.heappush(q, (total, arrival))  # 갱신한 비용과 도착노드를 힙에 push
    return cost_table


cost_table = dijkstra(1)
a1 = cost_table[v1]
a2 = cost_table[v2]

cost_table = dijkstra(v1)
b1 = cost_table[v2]
c2 = cost_table[N]

cost_table = dijkstra(v2)
b2 = cost_table[v1]
c1 = cost_table[N]

ans = min(a1+b1+c1, a2+b2+c2)
if ans >= 999999999:
    print(-1)
else:
    print(ans)
