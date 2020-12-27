import sys
input = sys.stdin.readline
N, K = map(int, input().split())

coins = []
for i in range(N):
    coins.append(int(input()))

# coins = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]
count = 0
for i in coins[::-1]:
    if K == 0:
        break
    if i <= K :
        count += (K // i)
        K -= i*(K // i)
        continue
print(count)