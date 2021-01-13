n = 7

mylist = [
'0110100',
'0110101',
'1110101',
'0000111',
'0100000',
'0111110',
'0111000'
]

# 다른사람꺼 보고 수정한 솔루션
import sys
input = sys.stdin.readline
n = int(input())
mylist = []
for i in range(n):
    mylist.append(list(input()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

countlist = []
for j in range(n):
    for k in range(n):
        if mylist[j][k] == '1':
            queue = [[j, k]]
            mylist[j][k] = '0'
            count = 1

            while queue:
                [a, b] = queue.pop(0)
                for i in range(4):
                    x = a + dx[i]
                    y = b + dy[i]
                    if 0 <= x < n and 0 <= y < n and mylist[x][y] == '1' :
                        mylist[x][y] = '0'
                        queue.append([x,y])
                        count += 1
            countlist.append(count)
countlist.sort()
print(len(countlist))
for i in countlist:
    print(i)






# #내 첫 솔루션

# import sys
# input = sys.stdin.readline
# n = int(input())
# mylist = []
# for i in range(n):
#     mylist.append(input())

# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]

# visited = [] # 0이면 미방문, 1이면 방문
# for i in range(n):
#     visited.append([0]*n)

# countlist = []
# for j in range(n):
#     for k in range(n):
#         if visited[j][k] == 0 and mylist[j][k] == '1':
#             s = [j, k]
#             visited[s[0]][s[1]] = 1

#             queue = [[j, k]]
#             count = 1
#             while queue:
#                 [a, b] = queue.pop(0)
#                 for i in range(4):
#                     x = a + dx[i]
#                     y = b + dy[i]
#                     if 0 <= x < n and 0 <= y < n and visited[x][y] == 0 and mylist[x][y] == '1' :
#                         visited[x][y] = 1
#                         queue.append([x,y])
#                         count += 1
#                         # print(mylist[x][y], "x, y :", x, y, "a, b:", a, b)
#             countlist.append(count)
# countlist.sort()
# print(len(countlist))
# for i in countlist:
#     print(i)
