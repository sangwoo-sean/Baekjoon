n = int(input())
mylist = list(map(int, input().split()))


count = 0
for i in range(n):

    if mylist[i] >= 2:
        case = mylist[i]
        valid = True
        for j in range(2,case):
            if case % j == 0:
                valid = False
            
        if valid:
            count += 1
    
print(count)        