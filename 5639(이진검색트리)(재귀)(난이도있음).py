# bisect를 이용한 li를 parameter로 넘겨주는 솔루션
import sys
import bisect
sys.setrecursionlimit(20000)
input = sys.stdin.readline


def solve(li):
    root = li[0]

    idx = bisect.bisect_right(li, root)  # root보다 큰값이 있는 인덱스
    left = li[1:idx]  # idx값 전까지 left part 생성
    right = li[idx:]  # idx값부터 끝까지 right part 생성

    if left:
        solve(left)
    if right:
        solve(right)

    print(root)


get = []
for i in range(10000):
    try:
        get.append(int(input()))
    except:
        break

solve(get)


# 첫 솔루션
# import sys
# sys.setrecursionlimit(20000)
# input = sys.stdin.readline


# def solve(li):
#     root = li[0]

#     l, r = 0, len(li)
#     for i in range(1, len(li)):
#         if li[i] < root:
#             l = i
#         else:
#             r = i
#             break
#     left = li[1:l+1]
#     right = li[r:]

#     if left:
#         solve(left)
#     if right:
#         solve(right)
#     print(root)


# get = []
# for i in range(10000):
#     try:
#         get.append(int(input()))
#     except:
#         break

# solve(get)
