import heapq
import sys
input = sys.stdin.readline


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
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


V, E = map(int, input().split())
start = int(input())

cost_table = [999999999] * (1+V)
graph = [[] for _ in range(1+V)]
# 각 간선들에 대해, a번 노드에 (b번노드로 가는 c비용의 간선) 저장
for i in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

dijkstra(start)

for i in cost_table[1:]:
    if i == 999999999:
        print("INF")
    else:
        print(i)


# 첫솔루션 : 실패


# import heapq
# import sys
# input = sys.stdin.readline

# V, E = map(int, input().split())
# start = int(input())

# graph = [[] for _ in range(1+V)]
# cost_table = [999999999] * (1+V)
# visit = [False]*(1+V)
# for i in range(E):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))

# cost_table[0] = 0
# cost_table[start] = 0
# visit[0] = True
# visit[start] = True
# for case in graph[start]:
#     arrival_node = case[0]
#     cost = case[1]
#     cost_table[arrival_node] = cost


# while True:
#     heap = []
#     for i in range(1, 1+V):
#         if not visit[i]:
#             heapq.heappush(heap, [cost_table[i], i])

#     if not heap:
#         break

#     cost, node_num = heapq.heappop(heap)  # start -> node_num 까지의 cost
#     visit[node_num] = True
#     # node_num -> arrival_node 까지의 cost
#     for arrival_node, cost_to_an in graph[node_num]:
#         if cost + cost_to_an < cost_table[arrival_node]:
#             cost_table[arrival_node] = cost + cost_to_an

# for i in cost_table[1:]:
#     if i == 999999999:
#         print("INF")
#     else:
#         print(i)
