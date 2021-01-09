import sys
input = sys.stdin.readline

def sol(n, mylist):
    if mylist[n] == [0, 0]:
        mylist[n] = [sol(n-1, mylist)[0] + sol(n-2, mylist)[0], sol(n-1, mylist)[1] + sol(n-2, mylist)[1]]
    return mylist[n]

t = int(input())
for _ in range(t):
    n = int(input())
    mylist = [[1, 0],[0, 1]]
    mylist += [[0, 0] for _ in range(n-1)]

    answer = sol(n, mylist)
    print(mylist)
    print(answer[0], answer[1])