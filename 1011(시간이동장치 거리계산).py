from math import sqrt, ceil
t = int(input())
mylist = []
for i in range(t):
    temp = list(map(int, input().split()))
    mylist.append(temp[1]-temp[0])
for i in range(t):
    n = ceil(sqrt(mylist[i]))
    if mylist[i] <= (n * (n - 1)):
        print((n-1)*2)
    else:
        print(n*2 -1)