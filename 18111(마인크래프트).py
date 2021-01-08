import sys
input = sys.stdin.readline
N, M, B = map(int, input().split())
land = {} # key:value = 높이:층갯수
for i in range(N):
    a = list(map(int, input().split()))
    for j in range(M): # 사전에 없으면 value 1로 키 생성, 있으면 value +1
        if a[j] in land:
            land[a[j]] += 1
        else:
            land[a[j]] = 1
keys = list(land.keys())
keys.sort()
stds = -1
mymin = 999999999999999

for i in range(min(keys), max(keys)+1):
    std = i
    sec = 0
    Btemp = B
    for j in range(len(keys)-1, -1, -1):
        if keys[j] == std: # 타겟층과 평탄화층이 같은경우
            continue
        # print(f"std : {std}, sec: {sec}, B : {Btemp}, keys[j] : {keys[j]}, j, i: {j, i}, keys[j],keys[i]:{keys[j],keys[i]}")
        if keys[j] > std: # 땅을 깎아야하는 경우
            sec += (keys[j]-std)*2*land[keys[j]] # 2초 * 기준층과의 차이 * 몇개인지
            Btemp += (keys[j]-std)*land[keys[j]] # 얻는 블럭 갯수
        elif keys[j] < std: # 땅을 채워야하는 경우
            if Btemp == 0:
                sec += 999999999999999
            if Btemp > 0: # 가진블럭이 충분하면 쌓아서 평탄화
                sec += (std-keys[j])*land[keys[j]] # 1초 * 층의 차이 * 그 높이 층의 개수
                Btemp -= land[keys[j]]*(std-keys[j]) # 층의 차이 * 그 높이 층의 개수
            if Btemp < 0: # 맨위의 if문 실행후 블럭이 마이너스면 시간초과로 무효화
                sec += 999999999999999
    if sec <= mymin and std > stds: # 시간초가 미니멈보다 작거나 같고, 평탄화층이 원래층보다 높다면 기록
        mymin, stds = sec, std
print(mymin, stds)





# # 18111번 첫시도, 예제는 모두 되나 채점시작하자마자 틀렸습니다 뜸
# import sys
# input = sys.stdin.readline
# N, M, B = map(int, input().split())
# land = {} # key:value = 높이:층갯수
# for i in range(N):
#     a = list(map(int, input().split()))
#     for j in range(M): # 사전에 없으면 value 1로 키 생성, 있으면 value +1
#         if a[j] in land:
#             land[a[j]] += 1
#         else:
#             land[a[j]] = 1

# keys = list(land.keys())
# keys.sort()
# stds = -1
# mymin = 999999999999999
# for i in range(len(keys)):
#     std = keys[i]
#     sec = 0
#     Btemp = B
#     for j in range(len(keys)-1, -1, -1):
#         if keys[j] == std: # 타겟층과 평탄화층이 같은경우
#             continue
#         # print(f"std : {std}, sec: {sec}, B : {Btemp}, keys[j] : {keys[j]}, j, i: {j, i}, keys[j],keys[i]:{keys[j],keys[i]}")
#         if keys[j] > std: # 땅을 깎아야하는 경우
#             sec += (keys[j]-keys[i])*2*land[keys[j]] # 2초 * 기준층과의 차이 * 몇개인지
#             Btemp += (keys[j]-keys[i])*land[keys[j]] # 얻는 블럭 갯수
#         elif keys[j] < std: # 땅을 채워야하는 경우
#             if Btemp > 0: # 가진블럭이 충분하면 쌓아서 평탄화
#                 sec += (keys[i]-keys[j])*land[keys[j]] # 1초 * 층의 차이 * 그 높이 층의 개수
#                 Btemp -= land[keys[j]]*(keys[i]-keys[j]) # 층의 차이 * 그 높이 층의 개수
#             if Btemp < 0: # 맨위의 if문 실행후 블럭이 마이너스면 시간초과로 무효화
#                 sec += 999999999999999
#     if sec <= mymin and std > stds: # 시간초가 미니멈보다 작거나 같고, 평탄화층이 원래층보다 높다면 기록
#         mymin, stds = sec, std
# print(mymin, stds)