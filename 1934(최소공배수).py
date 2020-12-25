import sys
input = sys.stdin.readline
t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    if a > b:
        a,b = b,a

    for i in range(a, a*b+1, a):
        if i % b == 0:
            print(i)
            break

    
