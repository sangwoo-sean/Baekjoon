n, m = map(int, input().split())

arr = [str(i) for i in range(1, n+1)]

for _ in range(m):
    i, k, j = map(int, input().split())
    arr = arr[:i-1] + arr[j-1:k] + arr[i-1:j-1] + arr[k:]

print(" ".join(arr))