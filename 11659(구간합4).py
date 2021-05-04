from itertools import accumulate
from sys import stdin
input = stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
acc = [0] + list(accumulate(arr))

for _ in range(m):
    l, r = map(int, input().split())
    print(acc[r]-acc[l-1])
