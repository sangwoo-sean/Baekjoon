get = input()
mylist = get.split()
for i in range(3):
    mylist[i] = int(mylist[i])
[a, b, c] = mylist

totlen = c-b-1
day = totlen // (a-b)
print(day+1)