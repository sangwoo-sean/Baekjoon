import sys
input = sys.stdin.readline


def BellmanFord(start):
    TABLE[start] = 0

    # 정점개수만큼 반복
    for i in range(N):

        for current_node, arrival_node, cost in edges:
            new_cost = TABLE[current_node] + cost
            if TABLE[arrival_node] > new_cost:
                TABLE[arrival_node] = new_cost
                # N 번째 반복때에도 값이 갱신된다면 음수 순환이 존재하는것
                if i == N - 1:
                    return True
    return False


for _ in range(int(input())):
    N, M, W = map(int, input().split())
    edges = []
    for i in range(M):
        S, E, T = map(int, input().split())
        edges.append((S, E, T))
        edges.append((E, S, T))

    for i in range(W):
        S, E, T = map(int, input().split())
        edges.append((S, E, -T))

    INF = 999_999_999
    TABLE = [INF] * (N+1)

    ans = "NO"
    if BellmanFord(1):
        ans = "YES"
    print(ans)
