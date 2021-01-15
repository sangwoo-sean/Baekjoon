n = int(input())

myarr = [0, 1, 3, 5] + [0 for _ in range(1000)]


for i in range(4, n+1):
    myarr[i] = myarr[i-1] + myarr[i-2] *2

print(myarr[n] % 10007)