n = 6
mylist = [10, 20, 15, 25, 10, 20]
# 구글링이후 찾은 해답
import sys
input = sys.stdin.readline
n = int(input())
mylist = [0] + [int(input()) for _ in range(n)]

if n >= 3:
    myarr = [0]*(n+1)
    myarr[0], myarr[1], myarr[2] = 0, mylist[1], mylist[1] + mylist[2] 
    for i in range(3, n+1):
        myarr[i] = max(myarr[i-3] + mylist[i-1] + mylist[i], myarr[i-2] + mylist[i])
elif n == 1:
    myarr = mylist
else:
    myarr = mylist
    myarr[2] = mylist[1] + mylist[2]

print(myarr[-1])



#타인 솔루션
# N = int(input())
# score = [0 for _ in range(301)]
# dp = [0 for _ in range(301)]

# for i in range(1, N + 1):
#     score[i] = int(input())
    
# dp[0] = 0
# dp[1] = score[1]
# dp[2] = dp[1] + score[2]

# for i in range(3, N + 1):
#     dp[i] = max(dp[i - 3] + score[i - 1] + score[i], dp[i - 2] + score[i])
# print(dp[N])









## 혼자 풀어본 풀이 (틀림)
# jump = True
# for i in range(2, n):
#     if jump:
#         myarr[n-i -1] += myarr[n-i +1]
#     else:
#         a = max(myarr[n-i], myarr[n-i +1])
#         myarr[n-i -1] += a

#         if a == myarr[n-i]:
#             jump = True
#             continue

#     if jump == True:
#         jump = False
# print(myarr[0])
