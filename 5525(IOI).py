n = 1
m = 13
st = 'OOIOIOIOIIOII'

###정석풀이
n = int(input())
m = int(input())
st = input()

i = 0
count = 0
temp = 0
while i+2 < m:
    if st[i]=="I" and st[i+1]=="O" and st[i+2]=="I":
        temp += 1
        if temp == n:
            count += 1
            temp -= 1
        i += 1
    else:
        temp = 0
    i += 1
print(count)




# 처음 풀이 O(n^2) 시간초과
# n = int(input())
# m = int(input())
# st = input()

# l = n*2 + 1
# target_string = "IO"*n + "I"

# i = 0
# count = 0
# while i+l < m:
#     for j in range(l):
#         valid = True
#         if st[i+j] != target_string[j]:
#             valid = False
#             break
#     if valid:
#         count += 1
#         i += 1
#     i += 1
# print(count)