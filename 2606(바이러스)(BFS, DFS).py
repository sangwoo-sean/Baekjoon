n = 7
m = 6

mylist = [[0], [0, 2, 5], [0, 1, 3, 5], [0, 2], [0, 7], [0, 1, 2, 6], [0, 5], [0, 4]]

###dfs
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
mylist = []
for _ in range(n+1):
    mylist.append([0])
for _ in range(m):
    a, b = map(int, input().split())
    mylist[a].append(b)
    mylist[b].append(a)
visited = [False]*(n+1)

visited[0] = True
def dfs(n):
    visited[n] = True
    
    for i in mylist[n]:
        if visited[i] == False:
            visited[i] = True
            dfs(i)

dfs(1)
print(visited[2:].count(True))



##BFS
# import sys
# input = sys.stdin.readline
# n = int(input())
# m = int(input())
# mylist = []
# for _ in range(n+1):
#     mylist.append([0])
# for _ in range(m):
#     a, b = map(int, input().split())
#     mylist[a].append(b)
#     mylist[b].append(a)
# visited = [False]*(n+1)

# q = [1]
# visited[1] = True
# count = 0
# while q:
#     x = q.pop()
#     visited[x] = True

#     for i in range(1, len(mylist[x])):
#         num = mylist[x][i]
#         if visited[num] == False:
#             q.append(num)
#             visited[num]= True
#             count += 1
# print(count)

