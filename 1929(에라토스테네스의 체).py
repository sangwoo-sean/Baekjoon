a, b = 3, 16

a, b = map(int, input().split())

idx = [i for i in range(b+1)]

for i in range(2, b):
    if idx[i] == 0:
        continue
    for j in range(i, b+1, idx[i]):
        if i == j:
            continue
        idx[j] = 0

for i in idx:
    if i >= a and i> 1:
        print(i)


# 기존 소수판별법의 복잡도는 O(n)
# 숫자의 제곱근까지만 검사를 해도 결과가 같음. 복잡도는 O(n**1/2)
# for i in range(a, b+1):
#     valid = True
#     for j in range(2,int(i**0.5)+1):
#         if i % j == 0:
#             valid = False
#             break
    
#     if valid:
#         print(i)
