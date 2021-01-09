


### 혼자 짠 코드, 예제는 다 맞는데 틀렸습니다 나옴.
# import sys
# input = sys.stdin.readline

# #DFS
# def dfs(n_list):
#     if len(n_list) == 0 or len(visited1) == N:
#         return
    
#     for i in n_list:
#         temp_list = []
#         if i not in visited1: # 방문하지 않은 노드만 실행
#             visited1.append(i)
#             for j in range(M): # 인접한노드중 방문하지 않은 노드들 추리기
#                 if mylist[j][0] == i and mylist[j][1] not in visited1:
#                     temp_list.append(mylist[j][1])
#                 elif mylist[j][1] == i and mylist[j][0] not in visited1:
#                     temp_list.append(mylist[j][0])
#             temp_list.sort() # 인접한 노드들을 오름차순으로 정렬
#             dfs(temp_list) # 인접한 노드들의 리스트에 대하여 재귀호출
#     return visited1
        
# #BFS
# def bfs(n_list):
#     if len(n_list) == 0 or len(visited2) == N:
#         return
    
#     temp_list = []
#     for i in n_list:
#         if i in visited2: # 방문한노드 스킵
#             continue

#         visited2.append(i)
#         for j in range(M): # 인접한노드중 방문하지 않은 노드들 추리기
#             if mylist[j][0] == i and mylist[j][1] not in visited2:
#                 temp_list.append(mylist[j][1])
#             elif mylist[j][1] == i and mylist[j][0] not in visited2:
#                 temp_list.append(mylist[j][0])

#     temp_list.sort() # 인접한 노드들을 오름차순으로 정렬
#     bfs(temp_list)

#     return visited2

# # t = int(input())
# # for _ in range(t):
# visited1 = []
# visited2 = []

# N, M, V = map(int, input().split())
# mylist = [list(map(int, input().split())) for i in range(M)]

# # n_list = [V]
# # answer1 = dfs(n_list)
# # print(" ".join(str(i) for i in answer1))

# n_list = [V]
# answer2 = bfs(n_list)
# print(" ".join(str(i) for i in answer2))








### 나동빈알고리즘 보고 다시 짠 코드 정답
from collections import deque
import sys
input = sys.stdin.readline

def dfs(n):
    if visited[n-1]: # 방문한 노드는 스킵
        return

    visited[n-1] = True
    ans.append(n) # 하나씩 쌓기
    
    temp_list = []
    for i in range(M): # n이랑 인접한노드 찾기
        if n in mylist[i] and mylist[i][0] == n:
            temp_list.append(mylist[i][1])
        if n in mylist[i] and mylist[i][1] == n:
            temp_list.append(mylist[i][0])
    temp_list.sort()
    for i in temp_list:
        dfs(i)

def bfs(n):
    if visited[n-1]:
        return

    visited[n-1] = True
    d.append(n)
    ans.append(n)
    while d:
        c = d.popleft()
        temp = []
        for i in range(M):
            if c in mylist[i]:
                if mylist[i][0] == c:
                    temp.append(mylist[i][1])
                if mylist[i][1] == c:
                    temp.append(mylist[i][0])
        temp.sort()
        for i in temp:
            if visited[i-1]:
                continue
            d.append(i)
            ans.append(i)
            visited[i-1] = True

N, M, V = map(int, input().split())
mylist = [list(map(int, input().split())) for i in range(M)]
visited = [False]*N
ans = []
dfs(V)
print(" ".join(str(i) for i in ans))

d = deque([])
ans = []
visited = [False]*N
bfs(V)
print(" ".join(str(i) for i in ans))