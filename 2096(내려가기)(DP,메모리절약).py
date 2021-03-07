from sys import stdin
input = stdin.readline
n = int(input())
li = list(map(int, input().split()))
dpL = li
dpS = li
for _ in range(n-1):
    a, b, c = map(int, input().split())
    dpL = [max(dpL[0], dpL[1]) + a,
           max(dpL[0], dpL[1], dpL[2]) + b,
           max(dpL[1], dpL[2]) + c]
    dpS = [min(dpS[0], dpS[1]) + a,
           min(dpS[0], dpS[1], dpS[2]) + b,
           min(dpS[1], dpS[2]) + c]
print(max(dpL), min(dpS))
