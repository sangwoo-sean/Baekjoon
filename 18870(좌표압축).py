n = 5
mylist = [2, 4, -10, 4, -9]


###모범답안
import sys
read = sys.stdin.readline

N = int(read())
nums = list(map(int, read().split()))
dic = {n: i for i, n in enumerate(sorted(set(nums)))}

print(" ".join(str(dic[n]) for n in nums))




### 해설보고 푼 답안
# import sys
# input = sys.stdin.readline

# n = int(input())
# mylist = list(map(int, input().split()))
# sortedlist = sorted(list(set(mylist)))
# mydict = {}

# for i in range(len(sortedlist)):
#     mydict[sortedlist[i]] = i

# for i in range(n):
#     mylist[i] = mydict[mylist[i]]

# print(" ".join(str(i) for i in mylist))




# 시간초과 구현답안
# n = int(input())
# mylist = list(map(int, input().split()))

# ans = []
# for i in range(n):
#     visit = set()
#     for j in range(n):
#         if mylist[i] > mylist[j] and mylist[j] not in visit:
#             visit.add(mylist[j])
#     ans.append(len(visit))
# print(ans)