from collections import deque
def D(n):
    return (2*n) % 10000
def S(n):
    return (n-1) % 10000
def L(n):
    return (n*10)%10000 + n//1000
def R(n):
    return (n%10)*1000 + n//10

for _ in range(int(input())):
    n, target = map(int, input().split())
    q = deque([n])
    visit = [0]*10001
    visit[n] = ""
    letter = "DSLR"

    while q:
        x = q.popleft()
        cases = [D(x), S(x), L(x), R(x)]

        for i, case in enumerate(cases):
            if visit[case] == 0:
                q.append(case)
                visit[case] = visit[x]+letter[i]
                if case == target:
                    print(visit[case])
                    q=False
                    break


























### 첫 솔루션
# from collections import deque
# def D(n):
#     return (2*n) % 10000
# def S(n):
#     if n == 0:
#         return 9999
#     return n-1
# def L(n):
#     return (n*10)%10000 + n//1000
# def R(n):
#     return (n%10)*1000 + n//10

# for _ in range(int(input())):
#     n, target = map(int, input().split())
#     q = deque([n])
#     visit = [0]*10001
#     visit[n] = ""

#     while q:
#         x = q.popleft()

#         d, s, l, r = D(x), S(x), L(x), R(x)

#         if visit[d] == 0:
#             q.append(d)
#             visit[d] = visit[x]+"D"
#             if d == target:
#                 print(visit[d])
#                 break

#         if visit[s] == 0:
#             q.append(s)
#             visit[s] = visit[x]+"S"
#             if s == target:
#                 print(visit[s])
#                 break

#         if visit[l] == 0:
#             q.append(l)
#             visit[l] = visit[x]+"L"
#             if l == target:
#                 print(visit[l])
#                 break

#         if visit[r] == 0:
#             q.append(r)
#             visit[r] = visit[x]+"R"
#             if r == target:
#                 print(visit[r])
#                 break