n = int(input())
li = list(map(int, input().split()))

dp = [1]*n
dp[-1] = 1

for i in range(n-2, -1, -1):
    for j in range(i+1, n):
        if li[i] < li[j] and dp[i] <= dp[j]:
            dp[i] = dp[j] + 1
print(max(dp))
