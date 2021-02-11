from itertools import combinations_with_replacement
n, m = map(int, input().split())
nums = list(map(int, input().split()))

comb = combinations_with_replacement(nums, m)
ans = sorted(list(set(tuple(sorted(list(i))) for i in comb)))
for i in ans:
    print(" ".join(str(j) for j in i))
