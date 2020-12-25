import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())

mylist = [int(input()) for i in range(n)]

print(int(round(sum(mylist)/n, 0)))
print(sorted(mylist)[n//2])

a = Counter(sorted(mylist))
if n == 1:
    print(mylist[0])
else:
    if a.most_common()[0][1] == a.most_common()[1][1]:
        print(a.most_common()[1][0])
    else:
        print(a.most_common()[0][0])

print(max(mylist)-min(mylist))