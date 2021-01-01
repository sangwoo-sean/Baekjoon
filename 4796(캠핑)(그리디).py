i = 0
while True:
    L, P, V = map(int, input().split())

    if L == 0:
        break

    cycle = V//P

    if L >= V % P:
        remain = V % P
    else:
        remain = L
    result = cycle * L + remain
    i += 1
    print(f"Case {i}: {result}")