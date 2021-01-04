#솔루션 with deque
from collections import deque

n = int(input())
d = deque(range(1, n+1))

while len(d) > 1:
    d.popleft()
    d.rotate(-1)
print(d[0])






# ideal 솔루션 without deque
# import math

# a = int(input())
# n = math.ceil(math.log2(a))
# x = 2**n - a
# answer = 2**n - 2*x
# print(answer)




#복잡도 N

# 내가 푼 솔루션 without deque
# n = int(input())
# if n == 1:
#     print(1)
# else:
#     i = 1
#     j = 0
#     while i < n:
#         i += 1

#         if j == i-1:
#             j = 2
#         else:
#             j += 2

#     print(j)








#복잡도 NlogN

# i = 0
# while len(num) > 1:
#     if i % 2 == 0:
#         print(num.pop(0), "is poped")
#     if i % 2 == 1:
#         num.append(num[0])
#         print(num.pop(0), "is going to the end of the list")
    
#     i += 1

# print(num[0])