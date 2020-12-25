N = int(input())

count = 0
result = 0
while result < N:
    result += count
    count += 1

loc = result - N

if count % 2 != 0:
    a = count - loc - 1
    b = count - a
else:
    b = count - loc - 1
    a = count - b

print(f"{a}/{b}")

