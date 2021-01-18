# 최적화 코딩
def solve(n):
    for i in reversed(range(1,int(n**0.5)+1)):
        dp[i**2] = 1
        if i**2 == n:
            return 1

    for i in range(2, n+1):
        if dp[i] == 1:
            continue 

        for j in range(1, int(i**0.5)+1):
            dp[i] = min(dp[i], dp[j**2] + dp[i-j**2])
    return dp[n]

n = int(input())
dp = [0, 1] + [4 for _ in range(n-1)]
answer = solve(n)
print(answer)


# 첫 솔루션, pypy로 제출할때만 통과
# dp = [0, 1, 2, 3] + [4 for _ in range(n-3)]

# for i in range(1, int(n**0.5)+1):
#     dp[i**2] = 1
# for i in range(5, n+1):
#     if dp[i] == 1:
#         continue 

#     for j in range(1, int(i**0.5)+1):
#         dp[i] = min(dp[i], dp[j**2] + dp[i-j**2])
#         if dp[i] == 2:
#             break

# print(dp[n])