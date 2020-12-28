import sys
input = sys.stdin.readline
N = int(input())
N_list = []
for i in range(N):
    N_list.append(list(map(int, input().split())))
mymax = 0
N_list.sort()
N_list.sort(key=lambda x: x[1])
for j in range(N):
    first = N_list[j]
    count = 1
    for i in range(1,N):
        if first[1] <= N_list[i][0]:
            first = N_list[i]
            count +=1
    if count > mymax :
        mymax = count
    if count <= mymax :
        break
print(mymax)
