import sys
input = sys.stdin.readline
T = int(input())
for j in range(T):
    N = int(input())
    mylist = [list(map(int, input().split())) for i in range(N)]

    mylist.sort()
    count = 1
    start = mylist[0][1]
    for i in range(1, N):

        if start > mylist[i][1]:
            count += 1
            start = mylist[i][1]
        if mylist[i][1] == 1:
            break
    
    print(count)