import math
n = int(input())

sqs = [i**2 for i in range(1, int(math.sqrt(n))+1)]
table = [0]*(n+1)

for i in range(1, n+1):
    x = 5
    for j in sqs:
        if i-j < 0:
            break
        x = min(x, table[i-j])
    table[i] = x + 1

print(table[n])
