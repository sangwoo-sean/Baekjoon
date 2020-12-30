import sys
input = sys.stdin.readline

weight = [""] *10
n = int(input())
mylist = [input().strip("\n") for _ in range(n)]

score = {'A' : 0, 'B' : 0, 'C' : 0, 'D' : 0, 'E' : 0, 'F' : 0, 'G' : 0,\
'H' : 0, 'I' : 0, 'J' : 0, 'K' : 0, 'L' : 0, 'M' : 0, 'N' : 0, \
'O' : 0, 'P' : 0, 'Q' : 0, 'R' : 0, 'S' : 0, 'T' : 0, 'U' : 0, \
'V' : 0, 'W' : 0, 'X' : 0, 'Y' : 0, 'Z' : 0}

for i in mylist:
    for p, j in enumerate(i):
        score[j] += 10**(len(i)-p-1)
        
sorting = []
for i in score.items():
    if i[1]:
        sorting.append(i[1])
sorting.sort(reverse=True)

result = 0
for i, elem in enumerate(sorting):
    result += elem*(9-i)
print(result)


###처음짠 코드
# import sys
# input = sys.stdin.readline

# weight = [""] *10
# n = int(input())
# mylist = [input().strip("\n") for _ in range(n)]

# score = {'A' : 0, 'B' : 0, 'C' : 0, 'D' : 0, 'E' : 0, 'F' : 0, 'G' : 0,\
# 'H' : 0, 'I' : 0, 'J' : 0, 'K' : 0, 'L' : 0, 'M' : 0, 'N' : 0, \
# 'O' : 0, 'P' : 0, 'Q' : 0, 'R' : 0, 'S' : 0, 'T' : 0, 'U' : 0, \
# 'V' : 0, 'W' : 0, 'X' : 0, 'Y' : 0, 'Z' : 0}
# number = {'A' : 0, 'B' : 0, 'C' : 0, 'D' : 0, 'E' : 0, 'F' : 0, 'G' : 0,\
# 'H' : 0, 'I' : 0, 'J' : 0, 'K' : 0, 'L' : 0, 'M' : 0, 'N' : 0, \
# 'O' : 0, 'P' : 0, 'Q' : 0, 'R' : 0, 'S' : 0, 'T' : 0, 'U' : 0, \
# 'V' : 0, 'W' : 0, 'X' : 0, 'Y' : 0, 'Z' : 0}

# for i in mylist:
#     for p, j in enumerate(i):
#         score[j] += 10**(len(i)-p-1)
        
# sorting = []
# for i in score.items():
#     if i[1]:
#         sorting.append(list(i))
# sorting.sort(key=lambda x: x[1], reverse=True)

# for i in range(len(sorting)):
#     number[sorting[i][0]] = 9-i

# result = 0
# for i in mylist:
#     for j in i:
#         n = number[j]
#         i = i.replace(j, str(n))
#     result += int(i)
# print(result)