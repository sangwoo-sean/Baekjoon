n, k = 7, 3
# 다른사람풀이
# n, k = map(int, input().split())
nums = [i for i in range(1, n + 1)]  # 1 ~ n까지의 수를 오름차순으로 생성
ans = []  # 요세푸스 순열을 저장할 리스트 생성
idx = 0

# nums가 빌 때까지
while nums:
    idx = (idx + k - 1) % len(nums)  # 수열에서 k번째 수의 인덱스 구하기
    ans.append(nums.pop(idx))  # k번째 수를 제거하고 정답리스트에 추가

print('<' + str(ans)[1:-1] + '>')


# # 내 솔루션
# N, K = map(int, input().split())

# nums = [i for i in range(1, N+1)]
# ans = []
# i = -1
# while len(ans) < N:
#     for _ in range(K):
#         i += 1
#         if i == N:
#             i = 0

#         while nums[i] == 0:
#             i += 1
#             if i == N:
#                 i = 0

#     ans.append(nums[i])
#     nums[i] = 0


# print('<' + ', '.join(str(i) for i in ans) + ">")
    

