n = int(input())

mylist = [-1]*n

hint = list(map(int, input().split()))


for i in range(n):
    j = 0
    while mylist.count(-1) == (n - i):
        if mylist[hint[i]+j] == -1 and mylist[:hint[i]+j].count(-1) == hint[i]:
            mylist[hint[i]+j] = i + 1
        j += 1

for i in mylist:
    print(i, end=" ")