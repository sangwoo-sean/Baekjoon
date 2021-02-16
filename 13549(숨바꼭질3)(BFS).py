N, K = map(int, input().split())

timeTable = [-1]*(100001)
q = [(K, 0)]
result = []

if N >= K:
    q = []
    result = N-K

while q:
    pos, time = q.pop(0)
    timeTable[pos] = time

    if pos == N:
        result = time
        break

    for i in [pos-1, pos+1]:
        if 0 <= i < 100001 and timeTable[i] == -1:
            q.append((i, time+1))

    if pos and pos % 2 == 0 and timeTable[pos//2] == -1:
        q = [(pos//2, time)] + q

print(result)
