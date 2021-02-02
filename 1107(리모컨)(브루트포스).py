target = int(input())
m = int(input())
if m:
    broken = set(map(str, input().split()))
else:
    broken = set()

count = abs(target-100)

for i in range(1000001):
    check = str(i)
    valid = True
    for j in check:
        if j in broken:
            valid = False
            break
    if valid:
        count = min(count, (len(check)+abs(target-i)))
print(count)
    