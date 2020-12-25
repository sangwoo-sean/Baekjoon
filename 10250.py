N = int(input())

a = []
b = []

for i in range(N):
    get = input()
    getlist = get.split()
    row = int(getlist[0])
    col = int(getlist[1])
    n = int(getlist[2])

    
    flr = n % row
    if flr == 0:
        flr = row
    rm = ((n-1) // row) + 1
    
    a.append(flr)
    b.append(rm)

for i in range(N):
    print("{}{:02}".format(a[i], b[i]))