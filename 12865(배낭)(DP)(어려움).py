import sys
input = sys.stdin.readline

N, K = map(int, input().split())

li = [list(map(int, input().split())) for i in range(N)]

dp = [[0]*(K+1) for _ in range(N)]

for i in range(N):
    weight = li[i][0]
    value = li[i][1]
    for j in range(1, K+1):
        if weight <= j:  # 담으려는 물건의 무게가 가방무게보다 크면
            # i번째 물건을 안담았을때, i번째 물건을 담았을때
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)
        else:  # i번째 물건을 안담으면 i-1번째 물건까지의 최대가치가 답이된다.
            dp[i][j] = dp[i-1][j]

print(dp[N-1][K])
for i in dp:
    print(i)
