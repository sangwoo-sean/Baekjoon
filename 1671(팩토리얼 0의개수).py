def facto(n):
    if n == 1 or n == 0:
        return 1
    return n*facto(n-1)

n = facto(int(input()))
n = str(n)
count = 0

for i in range(len(n)-1, 0, -1):
    if n[i] == '0':
        count += 1
    else:
        break
print(count)
