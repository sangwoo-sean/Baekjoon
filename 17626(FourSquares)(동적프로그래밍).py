# 최적화 코딩, dp도 안씀
def solve(n):
    if int(n**0.5)**2 == n: # 제곱수이면
        return 1
    cb = []
    for i in range(1, int((n//2)**0.5) + 1): # 절반까지만 검사해봐도 모두 검사한게 됨. 쌍이기 때문
        for j in range(1, int((n - i*i)**0.5) + 1):
            if i*i + j*j == n: # 제곱수이면
                return 2
            elif (n - i*i - j*j)**0.5 % 1 == 0: # 제곱수이면
                cb.append(3)
            else:
                cb.append(4)
    return min(cb)           

n = int(input())
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