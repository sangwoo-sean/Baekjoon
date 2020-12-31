import sys
input = sys.stdin.readline
n = int(input())
mylist = [int(input()) for _ in range(n)]

result = 0

mylist.sort()
i=0
while mylist[i] <= 0: #음수케이스
    if  i % 2 == 0:
        result += mylist[i]

    elif i % 2 == 1:
        mul = mylist[i]*mylist[i-1]
        result = result - mylist[i-1] + mul
    i += 1
    if i == len(mylist):
        break

mylist.sort(reverse=True)
i = 0
while mylist[i] > 0:#양수케이스
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

print(result)

# 예외 :
# -1, 0, 1이 있을때