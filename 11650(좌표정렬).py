import sys
input = sys.stdin.readline
n = int(input())

mylist = [list(map(int, (input().split()))) for i in range(n)]
mylist.sort(reverse=False, key= lambda x: mylist[x][1])
print(mylist)