calph = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

get = input()
ans = 0 
for i in get:
    ans += 1

count = []
for i in range(len(calph)):
    count.append(get.count(calph[i]))
if count[2] != 0:
    count[7] -= count[2]
for i in range(len(count)):
    if i == 2:
        ans -= count[i] * 2
    else:
        ans -= count[i]
print(ans)