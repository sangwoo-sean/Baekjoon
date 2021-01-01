T = int(input())
mylist = list(map(int, input().split()))

mylist.sort()

if mylist[0] != 1:
    print(1)

else:
    result = sum(mylist) +1
    for i in range(T-1):

        mysum = sum(mylist[:i+1])
        if mysum +1 < mylist[i+1]:
            result = mysum +1
            break

    print(result)


# 1
# 2
# 4
# 7
# 13
# 20
# 50
# cumsum +1 을 만들수있는지 확인