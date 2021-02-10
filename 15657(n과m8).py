from itertools import combinations_with_replacement

n, m = map(int, input().split())
nums = list(map(int, input().split()))

result = list(combinations_with_replacement(nums, m))
for i in range(len(result)):
    result[i] = sorted(result[i])

result.sort()
for i in result:
    print(" ".join(str(j) for j in i))
