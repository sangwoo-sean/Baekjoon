
from itertools import permutations

n, m = map(int, input().split())
nums = list(map(int, input().split()))

result = sorted(list(permutations(nums, m)))
for i in result:
    print(" ".join(str(j) for j in i))
