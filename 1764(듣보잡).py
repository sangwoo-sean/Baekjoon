n, m = 3, 4

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

mydict1 = {}
ans = []

for i in range(n):
    x = input().rstrip()
    mydict1[x] = i

for i in range(m):
    x = input().rstrip()
    if x in mydict1:
        ans.append(x)
ans.sort()
print(len(ans))
for i in ans:
    print(i)