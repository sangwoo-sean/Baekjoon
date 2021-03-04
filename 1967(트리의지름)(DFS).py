import sys
sys.setrecursionlimit(20000)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dfs(node, distance):
    global mylist
    visit[node] = True
    for n in graph[node]:
        if not visit[n[0]]:
            dfs(n[0], distance+n[1])
    mylist.append([distance, node])


mylist = []
visit = [False]*(n+1)
dfs(1, 0)
result = max(mylist)

mylist = []
visit = [False]*(n+1)
dfs(result[1], 0)
print(max(mylist)[0])
