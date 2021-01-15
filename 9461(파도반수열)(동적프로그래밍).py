myarr = [0, 1, 1, 1, 2, 2] + [0 for _ in range(100)]
for i in range(5, 101):
    myarr[i] = myarr[i-1] + myarr[i-5]

for _ in range(int(input())):
    print(myarr[int(input())])