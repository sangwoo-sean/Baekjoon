# 첫제출
import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(N)]

chick = []
house = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chick.append((i, j))
        elif city[i][j] == 1:
            house.append((i, j))

chicklist = list(combinations(chick, M))

ans = []
for c in chicklist:  # 가능한 치킨집들 조합
    mind = []  # 각 집들의 최소 치킨거리들
    for h in house:  # 각 집들에 대해서
        x, y = h
        mindlist = []
        for case in c:  # 각 치킨집들에 대해서
            a, b = case  # 치킨집들 좌표
            mindlist.append(abs(x-a)+abs(y-b))
        mind.append(min(mindlist))
    ans.append(sum(mind))
print(min(ans))


# 두번째 제출 ( 더느림 )
# import sys
# from itertools import combinations
# input = sys.stdin.readline

# N, M = map(int, input().split())

# city = [list(map(int, input().split())) for _ in range(N)]

# chick = []
# house = []
# for i in range(N):
#     for j in range(N):
#         if city[i][j] == 2:
#             chick.append((i, j))
#         elif city[i][j] == 1:
#             house.append((i, j))

# chicklist = list(combinations(chick, M))

# ans = 99999999
# for c in chicklist:  # 가능한 치킨집들 조합
#     mysum = 0
#     for h in house:  # 각 집들에 대해서
#         x, y = h
#         mind = 9999999
#         for case in c:  # 각 치킨집들에 대해서
#             a, b = case  # 치킨집들 좌표
#             mind = min(mind, abs(x-a)+abs(y-b))
#         mysum += mind
#     ans = min(ans, mysum)
# print(ans)
