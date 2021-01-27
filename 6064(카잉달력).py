for _ in range(int(input())):
    m, n, x, y = map(int, input().split())

    answer = -1

    if m > n:
        for i in range(x, m*n+1, m):
            if (i-y) % n == 0:
                answer = i
                break
    else:
        for i in range(y, m*n+1, n):
            if (i-x) % m == 0:
                answer = i
                break
    print(answer)



# for _ in range(int(input())):
#     m, n, x, y = map(int, input().split())

#     answer = -1
#     for i in range(x, m*n+1, m):
#         if (i-y) % n == 0:
#             answer = i
#             break
    
#    print(answer)