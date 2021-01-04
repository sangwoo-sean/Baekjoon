# 해설 : n1*n2 = LCM * GCD
a, b = 18, 24
a, b = map(int,input().split())
if a > b:
    big = a
    small = b
else:
    small = a
    big = b

value = big
while True:
    if big % small == 0:
        lcm = big
        break
    else:
        big = big + value
gcd = a*b//lcm
print(gcd)
print(lcm)






# # 내가찾은솔루션
# a, b = 18, 24
# a, b = map(int,input().split())
# if a > b:
#     a, b = b, a

# a1 = a
# b1 = b
# i = 2
# result = []
# while True:
#     if a1 % i  == 0 and b1 % i == 0:
#         a1 //= i
#         b1 //= i
#         result.append(i)
#         i = 1
#     i += 1
#     if i > a1:
#         break
# # gcd
# ans = 1
# if result:
#     for i in result:
#         ans *= i
# print(ans)

# # lcm
# a2 = a // ans
# b2 = b // ans
# lcm = a2*b2*ans
# print(lcm)