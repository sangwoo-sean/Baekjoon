n = 9

s = [
[0, 0, 0, 1, 1, 1, -1, -1, -1],
[0, 0, 0, 1, 1, 1, -1, -1, -1],
[0, 0, 0, 1, 1, 1, -1, -1, -1],
[1, 1, 1, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 0, 0, 0, 0],
[0, 1, -1, 0, 1, -1, 0, 1, -1],
[0, -1, 1, 0, 1, -1, 0, 1, -1],
[0, 1, -1, 1, 0, -1, 0, 1, -1]
]

import sys
input = sys.stdin.readline

def check(arr, x): # 행렬, 변의 길이
    if x == 1:
        return arr[0][0]+2

    check = []
    for j in range(x): # 0열 체크
        check.append(arr[j][0])
    if check.count(check[0]) != x: # 0열이 같은색이 아니면
        return False
    #0열이 같은색이면
    for i in range(x): # 각 행 체크
        if arr[i].count(check[0]) != x: # i행이 같은색이 아니면
            return False
    return check[0]+2

def solve(arr, x, ls):
    a, b, c = ls

    valid = check(arr, x)
    if valid:
        if valid == 3:
            c += 1
        elif valid == 2:
            b += 1
        else:
            a += 1
        return [a, b, c]

    l = x//3
    for i in range(9): # 9분할
        newarr = []
        for j in range(l): # 0, 1, 2
            newarr.append(arr[l*(i%3) + j][(i//3) *l:((i//3)+1) *l])
        a, b, c = solve(newarr, l, [a, b, c])

    return [a, b, c]

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

ans = solve(s, n, [0, 0, 0])
for i in ans:
    print(i)