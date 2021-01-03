# n = 8

# nums= [1000001, 8, 7, 6, 5, 4, 3, 2, 1]
# target = [4, 3, 6, 8, 7, 5, 2, 1]

import sys
input = sys.stdin.readline

n = int(input())
nums = [100001]
for i in range(n,0, -1):
    nums.append(i)
target = [int(input()) for _ in range(n)]

stack = []
result = []
answer = []
j = 0
while j < n:
    if nums[-1] <= target[j]:
        stack.append(nums.pop()) #push
        answer.append("+")

    elif stack[-1] == target[j]:
        result.append(stack.pop()) #pop
        j += 1
        answer.append("-")
    else:
        break


if len(answer) == n*2:
    for i in answer:
        print(i)
else:
    print("NO")
