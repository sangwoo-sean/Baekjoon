n = input()

mylist = [int(i) for i in n]
mylist.sort(reverse=True)
for i in mylist:
    print(i, end="")