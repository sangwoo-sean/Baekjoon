mystr = input()
mystr = mystr.upper()
count = []
chkstr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in mystr:
    count.append(i)
mylist = []
for i in chkstr:
    mylist.append(count.count(i))
mymax = max(mylist)
if mylist.count(mymax) > 1:
    print("?")
else:
    idx = mylist.index(mymax)
    print(chkstr[idx])