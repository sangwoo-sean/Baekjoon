import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    mydict = {}
    for _ in range(n):
        a, b = input().rstrip().split()
        if b in mydict:
            mydict[b] += 1
        else:
            mydict[b] = 1
    x = mydict.values()

    result = 1
    for i in x:
        result *= (i+1)
    result -= 1
    print(result)