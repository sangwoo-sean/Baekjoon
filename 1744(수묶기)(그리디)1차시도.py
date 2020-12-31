import sys
input = sys.stdin.readline
n = int(input())

mylist = [int(input()) for _ in range(n)]
mylist.sort(reverse=True)

result = 0

if mylist[-1] > 0:
    if n % 2 == 0:
        for i in range(0,n,2):
            result += mylist[i]*mylist[i+1]
    else:
        for i in range(0, n-1, 2):
            result += mylist[i]*mylist[i+1]
        result += mylist[-1]
    print(result)

else:
    if n % 2 == 0:
        for i in range(0,n,2):
            if mylist[i+1] <= 0:
                con = i
                break
            result += mylist[i]*mylist[i+1]
        for i in range(con, n):
            result += mylist[i]
    
    else:
        for i in range(0, n-1, 2):
            if mylist[i+1] <= 0:
                con = i
                break
            result += mylist[i]*mylist[i+1]
            con = i+2
            print(result)
        for i in range(con, n):    
            result += mylist[i]
        
    print(result)