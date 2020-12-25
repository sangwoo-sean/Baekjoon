N = int(input())
count = 0
for i in range(N):
    get = input()

    mylist = []
    check = 1
    for strs in get:
        if strs not in mylist:
            mylist.append(strs)
        elif strs == mylist[-1]:
            continue
        else:
            check = 0
            break
    if check == 1:
        count += 1
print(count)