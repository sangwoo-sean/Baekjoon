N, M = map(int, input().split())
they_know = set(list(map(int, input().split()))[1:])

party = [list(map(int, input().split()))[1:] for i in range(M)]
l, nl = 0, 1
while l != nl:
    l = len(they_know)
    for i in range(M):
        if not they_know.isdisjoint(party[i]):
            they_know = they_know.union(party[i])
    nl = len(they_know)

count = 0
for i in range(M):
    if they_know.isdisjoint(party[i]):
        count += 1
print(count)

# union-find를 이용한 풀이
# def find(x):
#     if x == root[x]:
#         return x
#     return find(root[x])


# def union(a, b):
#     a = find(a)
#     b = find(b)
#     if a > b:
#         root[a] = b
#     elif a < b:
#         root[b] = a  # 더 큰것의 루트는 더 작은것의 루트


# N, M = map(int, input().split())
# they_know = list(map(int, input().split()))[1:]
# party = [list(map(int, input().split()))[1:] for i in range(M)]
# root = [i for i in range(N+1)]

# for i in they_know:
#     union(0, i)

# for p in party:
#     l = len(p)
#     for i in range(1, l):
#         union(p[i-1], p[i])

# count = 0
# for p in party:
#     valid = True
#     for i in p:
#         if find(i) == 0:
#             valid = False
#             break
#     if valid:
#         count += 1
# print(count)
