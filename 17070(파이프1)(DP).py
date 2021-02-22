def solve(r, c):
    h, v, d = dp[r][c]

    # 오른쪽으로 갈 수 있는 경우
    if c+1 < n and not MAP[r][c+1]:
        dp[r][c+1][0] += h + d

    # 아래로 갈 수 있는경우
    if r+1 < n and not MAP[r+1][c]:
        dp[r+1][c][1] += v + d

    # 대각선으로 갈 수 있는경우
    if c+1 < n and r+1 < n and not MAP[r][c+1] and not MAP[r+1][c] and not MAP[r+1][c+1]:
        dp[r+1][c+1][2] += h + v + d


n = int(input())
MAP = [tuple(map(int, input().split())) for _ in range(n)]
dp = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]  # [가로, 세로, 대각선]에서 온 방법
dp[0][1] = [1, 0, 0]

for i in range(n):
    for j in range(1, n):
        solve(i, j)
print(sum(dp[-1][-1]))


# 다른방법
# def solve(r, c):
#     if MAP[r][c] == 1:
#         return

#     dp[r][c][0] = dp[r][c-1][0] + dp[r][c-1][2]
#     dp[r][c][1] = dp[r-1][c][1] + dp[r-1][c][2]
#     if not MAP[r-1][c] and not MAP[r][c-1]:
#         dp[r][c][2] = sum(dp[r-1][c-1])


# n = int(input())
# MAP = ((1,)*n,) + tuple(tuple(map(int, input().split())) for _ in range(n))
# dp = [[[0, 0, 0] for _ in range(n)]
#       for _ in range(n+1)]  # [가로, 세로, 대각선]에서 온 방법
# dp[1][1] = [1, 0, 0]

# for i in range(1, n+1):
#     for j in range(2, n):
#         solve(i, j)

# print(sum(dp[-1][-1]))
