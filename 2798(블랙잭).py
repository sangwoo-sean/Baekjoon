from itertools import combinations
n, m = list(map(int, input().split()))

mylist = list(map(int, input().split()))

comb = list(combinations(mylist, 3))
mylist2 = []
for i in comb:
    mylist2.append(sum(i))
mylist2.sort()

for i in mylist2:
    if i <= m:
        temp = i
print(temp)
