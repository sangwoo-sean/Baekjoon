from itertools import combinations
n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
result = sorted(set(combinations(nums, m)))

for i in result:
    print(*i)
