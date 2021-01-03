# K, N = 4, 11
# mylist = [802, 743, 457, 539]


# K, N = 3, 3
# mylist = [1, 2, 3]
# mylist = [3, 3, 3]
# mylist = [1, 2, 100]
# mylist = [1, 100, 101]

import sys
input = sys.stdin.readline
K, N = map(int, input().split())
mylist = [int(input()) for _ in range(K)]

start = 0
end = max(mylist)
myset = set()
while True:
    cut_len = (start + end)//2
    if cut_len == 0:
        cut_len = 1

    if cut_len in myset: #정답조건
        print(cut_len)
        break

    result = 0
    for i in range(K):
        result += mylist[i] // cut_len

    if result < N: #조건충족 x
        end = cut_len-1
        myset.add(cut_len)
        # print(cut_len, result)

    elif result >= N:
        start = cut_len+1
        myset.add(cut_len)
        # print(cut_len, result)
