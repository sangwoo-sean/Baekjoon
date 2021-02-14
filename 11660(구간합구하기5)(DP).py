import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nums = [[0]*(n+1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        # (1,1)부터 (i,j)까지 사각형의 누적합 = nums[i][j] + (i-1, j)까지의 누적합 + (i, j-1)까지의 누적합 - (i-1, j-1)까지의 누적합
        dp[i][j] = nums[i][j] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())

    # (x1, y1)부터 (x2, y2)까지의 누적합 = (x2,y2)까지의 누적합 - (x1-1, y2)까지의 누적합 - (x2, y1-1)까지의 누적합 + (x1-1, y1-1)까지의 누적합
    result = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]

    print(result)
