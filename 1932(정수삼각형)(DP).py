from sys import stdin
input = stdin.readline
n = int(input())

dp = [[0]*i for i in range(1, n+1)]
dp[0][0] = int(input())

for i in range(1, n):
    li = list(map(int, input().split()))
    leng = len(li)
    for j in range(leng):
        if j == 0:
            dp[i][j] = dp[i-1][j] + li[j]
        elif j == leng - 1:
            dp[i][j] = dp[i-1][j-1] + li[j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + li[j]

print(max(dp[-1]))
