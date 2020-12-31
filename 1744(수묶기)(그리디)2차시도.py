import sys
input = sys.stdin.readline
n = int(input())

mylist = [int(input()) for _ in range(n)]
mylist.sort(reverse=True)

result = 0
i = 0
while mylist[i] > 0:
    if  i % 2 == 0:
        result += mylist[i]

    elif i % 2 == 1:
        if mylist[i] == 1:
            mul = mylist[i]+mylist[i-1]
        else:
            mul = mylist[i]*mylist[i-1]
        result = result - mylist[i-1] + mul
    i += 1
    if i == len(mylist):
        break

for j in range(i,n):
    result += mylist[j]

print(result)