from collections import deque

A, B = map(int, input().split())

q = deque()
q.append((A, 1))

ans = 0
while q:
    x, n = q.popleft()

    a = x * 2
    b = x * 10 + 1
    if a == B or b == B:
        ans = n+1
        break

    if a < B:
        q.append((a, n+1))
    if b < B:
        q.append((b, n+1))

if ans:
    print(ans)
else:
    print(-1)
