
# N = 7
# mylist = [3, 5, 1, 1, 2, 4, 2]
# m = [10, 20, 10, 20, 15, 40, 200]

N = int(input())
mylist = []
m = []
for i in range(N):
    a, b = map(int, input().split())
    mylist.append(a)
    m.append(b)


##점화식을 이용한 브루트포스 알고리즘
def solve(i):
    if i > N:
        return 0
    result= 0
    if i+mylist[i-1] <= N+1:
        result = solve(i+mylist[i-1])+m[i-1]
    return max(result, solve(i+1))
result = solve(1)
print(result)

##다이나믹 프로그래밍
# result_list = [0]*N
# def solve(i):
#     print(i)
#     if i > N:
#         return 0
#     result = result_list[i-1]
#     if result_list[i-1] != 0:
#         return result_list[i-1]
#     if i+mylist[i-1] <= N+1:
#         result = solve(i+mylist[i-1])+m[i-1]
#     return max(result, solve(i+1))
# result = solve(1)
# print(result)









# 해설 :
# i 일 일때 얻을 수 있는 최대 수익=solve(i)=
# max(solve(i+T(i))+P(i), solve(i+1))
# =최댓값(그일을 하고난 후 일때 얻을수있는 최대 수익 + 그날 수익 vs 그날을 안하고 다음날 일했을때 얻을 수 있는 최대 수익)


#처음 짠 코드
# def solve(i):
#     print(i)
#     if i >= N:
#         return 0
#     if mylist[i] == 1:
#         return solve(i+mylist[i])+m[i]
#     if N-i <= mylist[i]:
#         return 0
#     return max(solve(i+mylist[i])+m[i], solve(i+1))