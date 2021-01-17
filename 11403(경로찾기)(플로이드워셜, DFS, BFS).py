n = 7

mylist = [
[0, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 1, 0],
[1, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 1],
[0, 0, 1, 0, 0, 0, 0]
]


# import sys
# input = sys.stdin.readline

# n = int(input())
# mylist = [list(map(int, input().split())) for _ in range(n)]

# #플로이드 워셜 알고리즘(Floyd Warshall Algorithm) 이용
# for i in range(n) : # i노드를 거쳐서
#     for j in range(n) :
#         for k in range(n):
#             if mylist[j][i] and mylist[i][k] : #j -> i, i -> k 가는길이 있으면
#                 mylist[j][k] = 1 # j -> k 가 있다

# for j in mylist:
#     print(" ".join(str(e) for e in j))


################# BFS
# def BFS(i, arr, n):
#     visit=[0] * n
#     q=[i]
    
#     while q:
#         x = q.pop(0)
#         for j in range(n): # 검사하는 행의 원소들 검사
#             if visit[j] == 0 and arr[x][j] == 1:
#                 visit[j] = 1
#                 q.append(j)
#     return visit

# ans = []
# for i in range(n): # 각 행 검사
#     ans.append(BFS(i, mylist, n))

# for line in ans:
#     print(' '.join(map(str, line)))


####### DFS

def dfs(x):
    for i in range(n):
        if visit[i] == 0 and mylist[x][i] == 1:
            visit[i] = 1
            dfs(i)

for i in range(n):
    visit = [0 for i in range(n)]
    dfs(i)
    print(" ".join(map(str, visit)))