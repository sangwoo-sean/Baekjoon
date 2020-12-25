def myfunc(n):
    n = n+1
    result = 0
    mul = 1
    mylist = []
    if n < 10:
        result =  n
    else:
        while mul <= n:
            mylist.append(int(((n % (mul*10)) - (n % mul)) / mul))
            mul *= 10
        for i in range(len(mylist)):
            result += mylist[i]
    result += n 
    return result
    
funcnum = []
for i in range(100):
    result = myfunc(i)
    funcnum.append(result)
mymax = max(funcnum)
numlist = []
for i in range(1, mymax):
    numlist.append(i)

for i in range(100):
    if funcnum[i] in numlist:
        numlist.remove(funcnum[i])
for i in range(len(numlist)):
    if numlist[i] > 10000:
        break
    print(numlist[i])
    