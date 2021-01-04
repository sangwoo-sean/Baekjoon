N, target = 6, 0

q = [1, 1, 9, 1, 2, 1]

T = int(input())
for _ in range(T):
    N, target = map(int, input().split())
    q = list(map(int, input().split()))

    sorted_q = sorted(q, reverse=True)

    i = 0
    nth = 0
    tn = q[target]
    while True:
        if q[i] == sorted_q[nth]:
            nth += 1
            if i == target:
                break
        i += 1
        if i == N:
            i = 0

    print(nth)