import sys
input = sys.stdin.readline

N = int(input())
lopes = [int(input()) for i in range(N)]

lopes.sort(reverse=True)
mymax = 0
for i in range(N):
    result = lopes[i] * (i+1)
    if mymax < result:
        mymax = result
print(mymax)