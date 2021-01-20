n = 8

s = [
[1, 1, 0, 0, 0, 0, 1, 1],
[1, 1, 0, 0, 0, 0, 1, 1],
[0, 0, 0, 0, 1, 1, 0, 0],
[0, 0, 0, 0, 1, 1, 0, 0],
[1, 0, 0, 0, 1, 1, 1, 1],
[0, 1, 0, 0, 1, 1, 1, 1],
[0, 0, 1, 1, 1, 1, 1, 1],
[0, 0, 1, 1, 1, 1, 1, 1]
]

# s = [
# [1, 1, 1, 1, 1, 1, 1, 1],
# [1, 1, 1, 1, 1, 1, 1, 1],
# [1, 1, 1, 1, 1, 1, 1, 1],
# [1, 1, 1, 1, 1, 1, 1, 1],
# [1, 1, 1, 1, 1, 1, 1, 1],
# [1, 1, 1, 1, 1, 1, 1, 1],
# [1, 1, 1, 1, 1, 1, 1, 1],
# [1, 1, 1, 1, 1, 1, 1, 1]
# ]
# n = 2
# s = [
# [1, 1],
# [0, 1]
# ]


import sys
input = sys.stdin.readline

# def check(arr, x): # 행렬, 변의 길이
#     check = []
#     for j in range(x): # 0열 체크
#         check.append(arr[j][0])
    
#     if check.count(check[0]) != x: # 0열이 같은색이 아니면
#         return False
#     #0열이 같은색이면
#     for i in range(x): # 각 행 체크
#         if arr[i].count(check[0]) != x: # i행이 같은색이 아니면
#             return False
#     return check[0]+1

def check(arr, x):
    start = arr[0][0]
    for i in range(x):
        for j in range(x):
            if start != arr[i][j]:
                return False
    return start +1

def solve(arr, x, bstart, wstart):
    b = bstart
    w = wstart

    valid = check(arr, x)
    if valid == 2:
        b += 1
        return b, w
    elif valid == 1:
        w += 1
        return b, w

    l = x//2
    for i in range(4): # 4분할
        newarr = []
        for j in range(l):
            if i < 2: 
                newarr.append(arr[l*i + j][:l])
            else:
                newarr.append(arr[l*(i-2) + j][l:])
        b, w = solve(newarr, l, b, w)

    return b, w

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

b, w = solve(s, n, 0, 0)
print(w)
print(b)