n = int(input())

myarr = [0, 1, 2, 3]

for i in range(4, max(4, n+1)):
    myarr.append(myarr[i-2]+myarr[i-1])

print(myarr[n] % 10007)
