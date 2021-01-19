import sys
input = sys.stdin.readline

n, m = map(int, input().split())

mydict = {}
mylist = []

for i in range(1, n+1):
    g = input().rstrip()
    mydict[g] = i
    mylist.append(g)

for _ in range(m):
    get = input()
    try:
        print(mylist[int(get)-1])
    except:
        print(mydict[get.rstrip()])



# # 첫솔루션
# n, m = map(int, input().split())

# mydict = {}
# strdict = {}

# for i in range(1, n+1):
#     g = input().rstrip()
#     mydict[i] = g
#     strdict[g] = i


# for _ in range(m):
#     get = input()
#     try:
#         print(mydict[int(get)])
#     except:
#         print(strdict[get.rstrip()])



## 시간초과
# mydict = {}

# for i in range(1, n+1):
#     mydict[i] = input()

# keys = list(mydict.keys())
# vals = list(mydict.values())

# for _ in range(m):
#     get = input()
#     try:
#         print(mydict[int(get)])
#     except:
#         p = vals.index(get)
#         print(keys[p])