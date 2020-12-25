def add(lst):
    result = []
    res = 0
    for i in lst:
        res += i
        result.append(res)
    return result


T = int(input())
ans = []
for t in range(T):
    a = int(input())
    b = int(input())
    x = []

    for i in range(1, b+1):
        x.append(i)

    for i in range(a):
        x = add(x)

    if a == 0:
        ans.append(b)
    else:
        ans.append(x[b-1])
for i in range(T):
    print(ans[i])