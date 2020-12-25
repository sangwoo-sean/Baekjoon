import math
t = int(input())
ans = []
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    R = math.sqrt((x1-x2)**2 + (y1-y2)**2)

    if R == 0 and r1==r2:
        ans.append(-1)
        continue
    elif R == 0 and r1!=r2:
        ans.append(0)
        continue

    if (r1 + r2) == R or abs(r1 - r2) == R:
        ans.append(1)
    elif (r1 + r2) > R and abs(r2-r1) < R:
        ans.append(2)
    elif (r1 + r2) > R and abs(r2-r1) > R:
        ans.append(0)
    elif (r1 + r2) < R:
        ans.append(0)

for i in range(t):
    print(ans[i])