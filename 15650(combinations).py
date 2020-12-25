from itertools import combinations, permutations

mylist = list(map(int, input().split()))

nums = [i for i in range(1, mylist[0]+1)]

result = list(combinations(nums, mylist[1]))

for i in result:
    for j in i:
        print(j, end=" ")
    print()