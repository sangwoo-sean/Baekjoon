mystr = input()

mydict = {3:"ABC",
4: "DEF",
5: "GHI",
6: "JKL",
7: "MNO",
8: "PQRS",
9: "TUV",
10: "WXYZ",
}

result = 0
for i in mystr:
    for j in range(3, 11):
        if i in mydict[j]:
            result += j
print(result)