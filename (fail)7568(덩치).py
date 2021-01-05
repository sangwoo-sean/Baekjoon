N = 5
mylist = [[55, 185, 0], [58, 183, 1], [88, 186, 2], [60, 175, 3], [46, 155, 4]]


N = int(input())
mylist = []
for i in range(N):
    mylist.append(list(map(int, input().split())))

answer = []
for i in range(N):
    count = 1
    for j in range(N):
        if mylist[i][0] < mylist[j][0] and mylist[i][1] < mylist[j][1]:
            count += 1
    answer.append(count)

for i in answer:
    print(i, end=" ")