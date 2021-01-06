import sys
input = sys.stdin.readline


# 딕셔너리를 만드는 솔루션
N = 10
cards = [6, 3, 2, 10, 10, 10, -10, -10, 7, 3]
M = 8
targets = [10, 9, -5, 2, 3, 4, 5, -10]

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

mydict = {}
for card in cards:
    if(card in mydict): # 있으면 값 +1
        mydict[card] += 1
    else: # 없으면 추가
        mydict[card] = 1

for target in targets:
    if target in mydict:
        print(mydict[target], end=" ")
    else: print("0", end=" ")

# print(' '.join(str(dicts[target]) if target in dicts else '0' for target in target_list))



# 카운터 모듈을 사용한 솔루션
# from collections import Counter
# # n = int(input())
# # s = list(map(int, input().split()))
# # m = int(input())
# # s_ = list(map(int, input().split()))
# cards = Counter(cards)
# print(cards)
# for i in targets:
#     print(cards[i], end=" ")








##시간초과
# N = int(input())
# cards = list(map(int, input().split()))
# M = int(input())
# targets = list(map(int, input().split()))

# ans = [0]* M
# sorted_target = sorted(targets)

# for i in range(N):
#     start = 0
#     end = M

#     while start <= end:
#         mid = (start+end)//2

#         if cards[i] > sorted_target[mid]:
#             start = mid + 1
#         elif cards[i] < sorted_target[mid]:
#             end = mid - 1
#         elif cards[i] == sorted_target[mid]:
#             ans[targets.index(cards[i])] += 1
#             break

#         # if mid == M or mid == -1:
#         #     break
        
# for i in ans:
#     print(i, end=" ")
            
