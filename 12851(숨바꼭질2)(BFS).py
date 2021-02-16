N, K = map(int, input().split())

times = [-1]*(100001)
q = [[K, 0]]
times[K] = 0
count = 0
minT = 0

while q:
    if N > K:
        minT = N - K
        count = 1
        break

    pos, time = q.pop(0)
    times[pos] = time

    if pos == N:
        if minT == 0:
            count += 1
            minT = time
        else:
            if time == minT:
                count += 1
            elif time > minT:
                break

    could = [pos - 1, pos + 1]
    if pos % 2 == 0:
        could.append(pos//2)

    for c in could:
        if 0 <= c < 100001 and times[c] == -1:
            q.append([c, time+1])

print(minT)
print(count)
