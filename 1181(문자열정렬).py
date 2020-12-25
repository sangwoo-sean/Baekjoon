import sys
input = sys.stdin.readline
n = int(input())

mylist = [input().strip("\n") for i in range(n)]

mylist.sort()
mylist = list(dict.fromkeys(mylist))
lenn = sorted(mylist, key= lambda x: len(x))

for i in lenn:
    print(i)