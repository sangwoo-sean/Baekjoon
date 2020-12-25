N = int(input())

n5 = N // 5 #3
n3 = 0
remains = N % 5 #3

if remains != 0:
    while n5 >= 0:
        if remains % 3 == 0:
            n3 = remains / 3
            break
        else:
            n5 -= 1
            remains += 5

if n5 < 0:
    n5 = 0
result = n5 + n3
if result == 0:
    result = -1
print(int(result))