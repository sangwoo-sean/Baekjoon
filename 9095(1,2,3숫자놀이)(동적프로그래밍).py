# 점화식 본뒤 풀이 ㅠㅠ
mylist = [0, 1, 2, 4]
for i in range(4, 11):
    mylist.append(mylist[i-3] + mylist[i-2] + mylist[i-1])
for _ in range(int(input())):
    n = int(input())
    print(mylist[n])



# 내 풀이 without DP
# from itertools import permutations
# for _ in range(int(input())):
#     n = int(input())
#     thr = n // 3
#     two = n // 2
#     one = n

#     mylist = []
#     for i in range(thr+1):
#         for j in range(two+1):
#             for k in range(one+1):
#                 if i*3 + j*2 + k == n:
#                     mylist.append([1 for _ in range(k)] + [2 for _ in range(j)] + [3 for _ in range(i)])
#     su = 0
#     for case in mylist:
#         su += len(set(permutations(case,len(case))))
#     print(su)