n, m = 5, 5

mylist = [[1, 3], [1, 4], [4, 5], [4, 3], [3, 2]]

# 플로이드워셜
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
mylist = [list(map(int, input().split())) for _ in range(m)]

graph = [[99999999]*n for _ in range(n)]
for a, b in mylist:
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

for i in range(n) : # i노드를 거쳐서
    for j in range(n) :
        for k in range(n):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])
        
ss = []
for i in range(n):
    ss.append(sum(graph[i])-graph[i][i])

print(ss.index(min(ss))+1)



# ###bfs
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# mylist = [list(map(int, input().split())) for _ in range(m)]

# nodes = [[] for _ in range(n+1)]
# for a, b in mylist:
#     nodes[a].append(b)
#     nodes[b].append(a)

# answers = []
# for i in range(1, n+1):
#     q = [i]
#     answer = [-1]*(n+1)
#     answer[i] = 0

#     while q:
#         x = q.pop(0)
#         for j in nodes[x]:
#             if answer[j] == -1:
#                 q.append(j)
#                 answer[j] = answer[x] + 1
#     answers.append(sum(answer)+1)
# print(answers.index(min(answers))+1)
    

