import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
M = int(input())
cases = list(map(int, input().split()))

nums.sort()

def bi_search(nums, case):
    start = 0
    end = len(nums) -1

    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == case:
            return True
        elif nums[mid] < case:
            start = mid + 1
        elif nums[mid] > case:
            end = mid - 1
        
    return False

for case in cases:
    if bi_search(nums, case):
        print(1)
    else:
        print(0)
