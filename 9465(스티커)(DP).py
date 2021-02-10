from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    stk = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0 for _ in range(n)], [0 for _ in range(n)]]
    dp[0][0] = stk[0][0]
    dp[1][0] = stk[1][0]
    if n > 1:
        dp[0][1] = stk[0][1] + dp[1][0]
        dp[1][1] = stk[1][1] + dp[0][0]
        for i in range(2, n):
            dp[0][i] = stk[0][i] + max(dp[1][i-1], dp[1][i-2])
            dp[1][i] = stk[1][i] + max(dp[0][i-1], dp[0][i-2])

        ans = max(dp[0][-1], dp[0][-2], dp[1][-1], dp[1][-2])
    else:
        ans = max(stk[0][0], stk[1][0])
    print(ans)
